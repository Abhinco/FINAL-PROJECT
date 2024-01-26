
from flask import Flask, request, redirect , jsonify
from flask_restful import Resource, Api
from flask_cors import CORS
import os
import prediction
import json
app = Flask(__name__)
cors = CORS(app, resources={r"*": {"origins": "*"}})
api = Api(app)

def serialize(obj):
    """Custom serialization function to handle non-serializable types."""
    if isinstance(obj, TypeError):
        return str(obj)
class GetPredictionOutput(Resource):
    def get(self):
        return {"error":"Invalid Method."}

    def post(self):
        try:
            data = request.get_json()
            predict_output = prediction.predict_mpg(data)
            ptr=predict_output[1:-1]
            
            response_dict = {'predict': ptr}
            return response_dict

        except Exception as error:
            return {'error': error}

api.add_resource(GetPredictionOutput,'/getPredictionOutput')

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host='0.0.0.0', port=port)