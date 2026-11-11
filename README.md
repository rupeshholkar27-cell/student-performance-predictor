# 🎓 Student Performance Predictor

A web app that predicts a student's **semester exam score (out of 100)** from internal marks, assignment marks, study hours and attendance. It follows the marking pattern used in my college:

| Component | Marks |
|---|---|
| Internal 1 | 30 |
| Internal 2 | 30 |
| Assignment and project | 20 |
| Semester exam (predicted) | 100 |

> **Note:** The dataset is **synthetic** (generated with a script, 300 students). The model and code are real, and the project can be retrained on real anonymized class data.

## 🔗 Live demo
[Open the app](https://your-app-link.streamlit.app) *(replace this with your Streamlit link after deploying)*

## ✨ Features
- **Prediction:** linear regression model trained with scikit-learn
- **Validation:** an OOP `Student` class that rejects invalid inputs (e.g. internal marks above 30)
- **Storage:** student records stored in a SQLite database
- **Logging:** actions and errors written to a log file
- **Analysis:** summary statistics and correlation of each factor with the semester score
- **Dashboard:** interactive Streamlit app with sliders, charts and CSV download

## 🛠 Tech stack
Python, Pandas, NumPy, scikit-learn, SQLite3, Streamlit, Matplotlib, Joblib

## 📊 Results
Trained on 300 synthetic student records (80% train, 20% test):

| Metric | Value |
|---|---|
| R² score | **0.77** |
| Mean absolute error | **about 4 marks** |

**Key insight:** study hours had the strongest correlation with the semester score (0.58), followed by Internal 2 (0.47) and Internal 1 (0.36).

## 🖼 Screenshots
*(Add your screenshots to a `screenshots` folder, then remove this line.)*

![Predict](screenshots/predict.png)
![Insights](screenshots/insights.png)
![Data](screenshots/data.png)

## 🚀 How to run locally

```bash
# 1. Create and activate a virtual environment
python -m venv venv
venv\Scripts\activate          # Windows
# source venv/bin/activate     # Mac/Linux

# 2. Install dependencies
python -m pip install -r requirements.txt

# 3. Generate data, load it into SQLite, and train the model
python generate_data.py
python main.py
python predictor.py

# 4. Start the dashboard
python -m streamlit run app.py
```

## 📁 Project structure

```
student-performance-predictor/
├── app.py               # Streamlit dashboard
├── models.py            # Student class with input validation (OOP)
├── database.py          # SQLite operations
├── analysis.py          # Pandas statistics and correlations
├── predictor.py         # Model training and prediction
├── logger_config.py     # Logging setup
├── generate_data.py     # Creates the synthetic dataset
├── main.py              # Loads data and tests validation
├── data/students.csv    # Generated dataset
├── requirements.txt
└── README.md
```

## 🧠 What I learned
- Designing a small project with separate modules and classes
- Validating input and handling exceptions
- Storing and reading data with SQLite
- Statistical analysis (mean, standard deviation, correlation) with Pandas
- Training and evaluating a regression model (train/test split, R², MAE)
- Building and deploying an interactive app with Streamlit

## 🔮 Future work
- Train on real (anonymized) class data
- Compare with Random Forest and other models
- Add a feature to save new student records from the dashboard

## 👤 Author
**Rupesh Holkar**
GitHub: [rupeshholkar27-cell](https://github.com/rup
