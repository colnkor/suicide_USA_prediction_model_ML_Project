from flask import (
    Blueprint, render_template, request, jsonify
)
from .predmodel.model import LOADED_MODEL as DecisionTreeRegressor
from .predmodel.dataprep import data_prep
from .validation.model_data_validation import model_data_validation as data_valid
import pandas as pd

bp = Blueprint('prediction', __name__, url_prefix='/predict')

@bp.route('/', methods=('GET', 'POST'))
def suic_pred():
    if request.method == 'POST':
        data = request.get_json()

        try:
            # Wrap each value in a list to satisfy pandas' requirements
            list_data = {key: [value] for key, value in data.items()}
            
            data_valid(list_data)

            df = pd.DataFrame(list_data)

            print("Before data_prep")
            ndf = data_prep(df)
            print("Before prediction")
            predictions = DecisionTreeRegressor.predict(ndf)

            print("WE ARE RETURNING VALUE")
            return jsonify({'prediction': predictions.tolist()})
        except Exception as e:
            print(e)
            return jsonify({'error': 'Server Error'}), 400

    return render_template('prediction/index.html')