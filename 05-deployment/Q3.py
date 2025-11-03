import pickle
import sklearn

print(sklearn.__version__)

with open('pipeline_v1.bin', 'rb') as f_in:
    pipeline = pickle.load(f_in)

record = {
    "lead_source": "paid_ads",
    "number_of_courses_viewed": 2,
    "annual_income": 79276.0
}

def predict_single(customer):
    result = pipeline.predict_proba(customer)[0, 1]
    return float(result)

result = predict_single(record)
print(f'Predicted probability of converting this customer: {result:.3f}')