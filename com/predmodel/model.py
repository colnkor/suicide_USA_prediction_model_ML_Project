import joblib
import os

model_dir = os.path.dirname(os.path.abspath(__file__))
MODEL_PATH = os.path.join(model_dir, 'models/USA_suicide_pred_model_1.pkl')

def get_model():
    """Loads the trained DecisionTreeRegressor model."""
    try:
        model = joblib.load(MODEL_PATH)
        return model
    except FileNotFoundError:
        print(f"Error: Model file not found at {MODEL_PATH}")
        return None

# Load the model once when the module is imported
LOADED_MODEL = get_model()
