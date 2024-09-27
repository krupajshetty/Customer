
# ChurnPredictor

This project focuses on predicting customer churn using machine learning models. It provides a Python class, `ChurnPredictor`, to train and evaluate models using customer data, with support for AutoML to automatically select the best model. The project also implements data version control (DVC) for managing dataset versions and utilizes Git branching for efficient project management.

---

## Project Structure


ChurnPredictor/
│
├── data/                     
│   ├── customer_data.csv      # Customer dataset (DVC tracked)
│
├── src/                      
│   ├── __init__.py
│   ├── churn_predictor.py     # Main ChurnPredictor class
│   └── automl_predictor.py    # AutoML class using TPOT
│
├── tests/                    
│   ├── __init__.py
│   ├── test_churn_predictor.py # Unittests for ChurnPredictor class
│
├── .dvc/                     # DVC config files
├── .dvcignore                # DVC ignore file
├── .gitignore                # Git ignore file
├── dvc.yaml                  # DVC pipeline configuration
├── dvc.lock                  # DVC lock file
├── requirements.txt          # Python dependencies
├── README.md                 # Project documentation
├── main.py                   # Entry point to run the project
└── setup.py                  # Optional packaging


---

## Setup Instructions

### 1. Clone the Repository

bash
git clone <your-repo-url>
cd ChurnPredictor


### 2. Set Up Virtual Environment

bash
python -m venv venv
source venv/bin/activate      # For Windows: venv\Scripts\activate


### 3. Install Dependencies

bash
pip install -r requirements.txt


### 4. Initialize DVC

bash
dvc init
dvc add data/customer_data.csv
git add data/customer_data.csv.dvc .gitignore
git commit -m "Initialize DVC and track dataset"


### 5. Run the Project

bash
python main.py


---

## ChurnPredictor Class

The `ChurnPredictor` class provides the following methods:

- **Preprocess Data**: Encodes features and splits the dataset.
- **Train Model**: Trains a RandomForest classifier by default.
- **Predict Churn**: Predicts churn probability for new customers.
- **Calculate Retention/Churn Rates**: Calculates customer retention and churn rates.

---

## AutoML Support

The project also includes AutoML capabilities using `TPOTClassifier`. The `AutoMLChurnPredictor` class extends `ChurnPredictor` and automates model selection for customer churn prediction.

---

## Git Branching

Git branching is used to manage features related to different contract types:

- `main` branch holds the final `ChurnPredictor` class.
- Feature branches for contract types (e.g., `Month-to-Month`, `One-Year`) are merged into `main`.

Example:

bash
git checkout -b feature-month-to-month
git add .
git commit -m "Added Month-to-Month contract logic"
git push origin feature-month-to-month


---

## DVC Workflow

Track the dataset with DVC:

bash
dvc add data/customer_data.csv
git add data/customer_data.csv.dvc
git commit -m "Update customer dataset"
git push
dvc push


---

## Unit Testing

Run unit tests for `ChurnPredictor`:

bash
python -m unittest discover tests/
