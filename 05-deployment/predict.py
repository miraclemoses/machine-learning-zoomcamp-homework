from fastapi import FastAPI
import uvicorn
import pickle
from typing import Dict, Any
import os

app = FastAPI(title="lead-scoring-course-prediction")

def load_pipeline():
    for filename in ["pipeline_v2.bin", "pipeline_v1.bin"]:
        if os.path.exists(filename):
            with open(filename, "rb") as f_in:
                print(f"✅ Loaded model: {filename}")
                return pickle.load(f_in)
    raise FileNotFoundError("❌ Aucun modèle trouvé (pipeline_v1.bin ou pipeline_v2.bin)")

pipeline = load_pipeline()


def predict_single(customer):
    result = pipeline.predict_proba(customer)[0, 1]
    return float(result)

@app.post("/predict")
def predict(customer: Dict[str, Any]) -> Dict[str, Any]:
    prob = predict_single(customer)

    return dict(
        convert_probability=prob,
        converted=bool(prob >= 0.5)
    )


if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=9696)