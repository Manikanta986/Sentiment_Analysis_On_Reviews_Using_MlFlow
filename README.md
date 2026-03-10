# 🛒 Flipkart Product Review Sentiment Analysis

A **Machine Learning + NLP + MLOps project** that analyzes Flipkart product reviews and predicts whether the sentiment is **Positive 😊 or Negative 😞**.

This project demonstrates a **complete end-to-end ML pipeline** including:

- Natural Language Processing (NLP)
- Machine Learning Model Training
- MLflow Experiment Tracking
- Prefect Workflow Automation
- Streamlit Web Application

---

# 📌 Project Overview

Customer reviews are extremely important for e-commerce platforms like Flipkart.  
However, manually analyzing thousands of reviews is time-consuming.

This project solves that problem by building an **automated sentiment analysis system**.

The system:

1. Cleans review text
2. Removes stopwords
3. Applies lemmatization
4. Converts text to TF-IDF vectors
5. Uses a Logistic Regression model
6. Predicts sentiment instantly

---

# 🚀 Features

✔ Real-time **sentiment prediction**  
✔ **Streamlit web application**  
✔ **TF-IDF feature extraction**  
✔ **Logistic Regression classifier**  
✔ **MLflow experiment tracking**  
✔ **Confusion matrix visualization**  
✔ **Hyperparameter tuning**  
✔ **Prefect workflow automation**  
✔ Scheduled **automatic training pipeline**

---

# 🧠 Machine Learning Workflow

User Review  
↓  
Text Cleaning  
↓  
Stopword Removal  
↓  
Lemmatization  
↓  
TF-IDF Vectorization  
↓  
Logistic Regression Model  
↓  
Sentiment Prediction

---

# ⚙️ MLOps Workflow

Dataset  
↓  
Training Script  
↓  
MLflow Experiment Tracking  
↓  
Model + Metrics Logging  
↓  
Prefect Workflow Automation  
↓  
Scheduled Model Training  
↓  
Streamlit Deployment

---

# 🛠️ Technologies Used

| Technology | Purpose |
|------------|--------|
| Python | Programming Language |
| Streamlit | Web Application |
| Scikit-learn | Machine Learning |
| NLTK | Natural Language Processing |
| MLflow | Experiment Tracking |
| Prefect | Workflow Automation |
| Joblib | Model Serialization |
| Pandas | Data Processing |
| Matplotlib | Visualization |

---

# 📂 Project Structure

Flipkart-Sentiment-Analysis

app.py  
train_mlflow.py  
pipeline.py  
sentiment_model.pkl  
tfidf_vectorizer.pkl  
cleaned_data.csv  
requirements.txt  
README.md  

---

# ⚙️ Installation

Clone the repository

git clone https://github.com/your-username/flipkart-sentiment-analysis.git

Move into project directory

cd flipkart-sentiment-analysis

Install dependencies

pip install -r requirements.txt

---

# ▶️ Run Streamlit Application

streamlit run app.py

Open browser

http://localhost:8501

---

# 🤖 Model Training with MLflow

Run training script

python train_mlflow.py

Start MLflow UI

mlflow ui

Open

http://localhost:5000

MLflow tracks:

- Parameters
- Metrics
- Model versions
- Confusion matrix
- Experiments

---

# 🔄 Prefect Workflow Automation

Run Prefect pipeline

python pipeline.py

The pipeline:

- Runs the MLflow training script
- Automates model training
- Schedules training every **1 hour**

---

# 🧹 Text Preprocessing Steps

The review text undergoes several preprocessing steps:

1. Convert text to lowercase  
2. Remove special characters  
3. Remove stopwords  
4. Apply lemmatization  
5. Convert text to TF-IDF vectors  

---

# 📊 Example Predictions

Review:  
This product is amazing and works perfectly  

Prediction:  
Positive 😊  

Review:  
Very bad quality and waste of money  

Prediction:  
Negative 😞  

---

# 📈 Model Metrics

Tracked using **MLflow**

- Accuracy
- F1 Score
- Confusion Matrix
- Hyperparameters
- Model versioning

---

# 🔮 Future Improvements

- Add **Deep Learning models (LSTM / BERT)**
- Deploy using **Streamlit Cloud**
- Add **real-time Flipkart review scraping**
- Build **sentiment dashboard**
- Add **Neutral sentiment class**
