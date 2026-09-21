# Twitter Sentiment Analysis using Machine Learning

## 📌 Project Overview
This project performs sentiment analysis on Twitter data using Machine Learning and Natural Language Processing (NLP). The model classifies tweets into three sentiment categories: Positive, Neutral, and Negative. TF-IDF is used to convert text into numerical features, and Logistic Regression is used for sentiment classification. A Streamlit web application is also developed to allow users to enter a tweet and receive a sentiment prediction.

## 🛠️ Technologies Used
- Python
- Pandas
- NumPy
- Scikit-learn
- TF-IDF Vectorizer
- Logistic Regression
- Pickle
- Streamlit
- Jupyter Notebook

## 📂 Project Structure
Twitter-Sentiment-Analysis/
├── app.py
├── sentiment.ipynb
├── sentiment_model.pkl
├── tfid.pkl
├── requirements.txt
└── README.md

## 📊 Dataset
The project uses a Twitter sentiment dataset downloaded from Kaggle. The dataset contains tweets and their corresponding sentiment labels.

## 🔄 Project Workflow
Kaggle Twitter Dataset → Data Preprocessing → Train/Test Split → TF-IDF Vectorization → Logistic Regression → Model Evaluation → Save Model → Streamlit Deployment → Enter Tweet → Sentiment Prediction

## 🧹 Data Preprocessing
The dataset is prepared before training the model. Missing values are handled and the tweet text is converted into numerical features using TF-IDF.

## 🔢 TF-IDF
TF-IDF (Term Frequency-Inverse Document Frequency) converts text into numerical features that can be processed by a machine learning model.

Tweet → TF-IDF → Numerical Features → Logistic Regression → Sentiment

## 🤖 Machine Learning Model
Logistic Regression is used to classify tweets into three sentiment categories:
- Positive
- Neutral
- Negative

## 📈 Model Evaluation
The model is evaluated using:
- Accuracy
- Precision
- Recall
- F1-score
- Classification Report

Accuracy: Add your actual accuracy here.

## 🌐 Streamlit Deployment
The trained Logistic Regression model and TF-IDF vectorizer are saved using Pickle. The Streamlit application loads these files and predicts the sentiment of new tweets.

Run the application using:

```bash
streamlit run app.py