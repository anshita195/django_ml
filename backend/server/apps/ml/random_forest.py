import json
import numpy as np
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelEncoder
from sklearn.ensemble import RandomForestClassifier
from sklearn.ensemble import ExtraTreesClassifier
import joblib

class RandomForestClassifier:
    def __init__(self):
        path_to_artifacts="../../research/"
        self.value_fill_missing=joblib.load(path_to_artifacts+"train_mode.joblib")
        self.encoders=joblib.load(path_to_artifacts+"encoders.joblib")
        self.model=joblib.load(path_to_artifacts+"random_forest.joblib")

    def preprocessing(self,input_data):
        #JSON to pandas:
        input_data=pd.DataFrame(input_data,index=[0])
        input_data.fillna(self.value_fill_missing)
        for column in [
            "workclass",
            "education",
            "marital-status",
            "occupation",
            "relationship",
            "race",
            "sex",
            "native-country",
        ]:
            categorical_convert=self.encoders[column]
            input_data[column]=categorical_convert.transform(input_data[column])
        return input_data
    
    def predict(self,input_data):
        return self.model.predict_proba(input_data)
    
    def postprocessing(self,input_data):
        label="<=50K"
        if input_data[1]>0.5:
            label=">50K"
        return {"probability":input_data[1],"label":label,"status":"OK"}
    
    def compute_prediction(self,input_data):    
        try:
            input_data=self.preprocessing(input_data)
            prediction=self.predict(input_data)[0]
            prediction=self.postprocessing(prediction)
        except Exception as e:
            return {"status":"Error","message":str(e)}
        
        return prediction
    
    # def compute_prediction(self, input_data):
    #     try:
    #         input_data = self.preprocessing(input_data)
    #         print("Preprocessing successful:", input_data)
    #         prediction = self.predict(input_data)[0]
    #         print("Prediction successful:", prediction)
    #         prediction = self.postprocessing(prediction)
    #         print("Postprocessing successful:", prediction)
    #     except Exception as e:
    #         print("Error during compute_prediction:", str(e))
    #         return {"status": "Error", "message": str(e)}
        
    #     return prediction

