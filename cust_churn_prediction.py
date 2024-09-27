import pandas as pd
import numpy as np
from pycaret.classification import *

# Step 2: Create DataFrame
df = pd.read_csv('C:/Users/VSCA/Desktop/customer/custdata.csv')

# Step 3: One-hot encode the categorical features
df_encoded = pd.get_dummies(df, columns=['Contract_Type'], drop_first=True)

# Step 4: Set up PyCaret for classification
# We drop 'Customer_ID' as it is not relevant to the model
clf = setup(df_encoded, target='Churn_Flag', silent=True, verbose=False, session_id=123)

# Step 5: Compare different models automatically
best_model = compare_models()

# Step 6: Display the best model
print(best_model)

# Step 7: Finalize the best model (train it on the full dataset)
final_model = finalize_model(best_model)

# Step 8: Evaluate the model using the test set (PyCaret automatically splits data)
# This step will give you accuracy, precision, recall, and other metrics
evaluate_model(final_model)