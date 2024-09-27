import unittest
from churn_predictor import ChurnPredictor
import pandas as pd

class TestChurnPredictor(unittest.TestCase):
    def setUp(self):
        """
        Set up sample data and ChurnPredictor instance
        """
        data = pd.DataFrame({
            'Customer_ID': [1, 2],
            'Contract_Type': ['Month-to-Month', 'One-Year'],
            'Monthly_Charges': [30, 40],
            'Tenure': [10, 24],
            'Churn_Flag': [0, 1]
        })
        self.cp = ChurnPredictor(data)
        self.cp.train_model()

    def test_predict_churn(self):
        """
        Test churn prediction on new customer data
        """
        new_customer = [50, 12, 1, 0]  # Example features: Monthly_Charges, Tenure, Contract_Type_One-Year
        churn_prediction = self.cp.predict_churn(new_customer)
        self.assertIn(churn_prediction, [0, 1], "Prediction should be 0 (not churn) or 1 (churn)")

    def test_retention_rate(self):
        """
        Test retention rate calculation
        """
        retention_rate = self.cp.retention_rate()
        self.assertTrue(0 <= retention_rate <= 1, "Retention rate should be between 0 and 1")

if __name__ == '_main_':
    unittest.main()