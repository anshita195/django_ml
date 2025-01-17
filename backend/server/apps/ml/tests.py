from django.test import TestCase
from apps.ml.random_forest import RandomForestClassifier
from apps.ml.registry import MLRegistry
import inspect

class MLTests(TestCase):
    def test_rf_algorithm(self):
        input_data={
            "age": 37,
            "workclass": "Private",
            "fnlwgt": 34146,
            "education": "HS-grad",
            "education-num": 9,
            "marital-status": "Married-civ-spouse",
            "occupation": "Craft-repair",
            "relationship": "Husband",
            "race": "White",
            "sex": "Male",
            "capital-gain": 0,
            "capital-loss": 0,
            "hours-per-week": 68,
            "native-country": "United-States"
        }
        my_alg=RandomForestClassifier()
        response=my_alg.compute_prediction(input_data)
        # print(response)
        self.assertEqual('OK',response['status'])
        self.assertTrue('label' in response)
        self.assertEqual('<=50K',response['label'])

    def test_registry(self):
        registry=MLRegistry()
        self.assertEqual(len(registry.endpoints),0)
        endpoint_name="income_classifier"
        algorithm_object=RandomForestClassifier()
        algorithm_name="random forest"
        algorithm_status="production"
        algorithm_version="0.0.1"
        algorithm_owner="AJ"
        algorithm_description="Random Forest with simple processing"
        algorithm_code=inspect.getsource(RandomForestClassifier)
        registry.add_algorithm(endpoint_name,
                               algorithm_object,
                               algorithm_name,
                               algorithm_status,
                               algorithm_version,
                               algorithm_owner,
                               algorithm_description,
                               algorithm_code)
        self.assertEqual(len(registry.endpoints),1)