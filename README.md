# Insurance Premium Predictor – Complete Application

This project predicts the **insurance premium category** (High, Medium, Low) based on user details such as age, weight, height, income, smoker status, city, and occupation.  

It is built with a **FastAPI backend** (serving the ML model) and a **Streamlit frontend** (user interface). Both are hosted online and connected, making this a complete end-to-end deployed application.

---

## 🚀 Features
- User-friendly **Streamlit UI**
- **FastAPI backend** with a trained ML model (Random Forest Classifier)
- Input validation using **Pydantic**
- Clean JSON API responses
- Fully deployed: **Frontend (Streamlit) + Backend (Railway)**

---

## 🌐 Live Demo
You can try the complete working app here:  
👉 **[Insurance Premium Predictor App](https://qmlhufcarxtbpdkrlxew2s.streamlit.app/)**  

*(This app is fully functional — the Streamlit frontend is connected to the FastAPI backend running on Railway.)*

---

## 🛠️ Tech Stack
- **Frontend:** Streamlit  
- **Backend:** FastAPI  
- **ML Model:** Random Forest Classifier (trained in Google Colab, saved as `model.pkl`)  
- **Other Tools:** Pydantic (validation), Requests (API calls), Railway (backend hosting), Streamlit Cloud (frontend hosting)  

---

## 📌 Repositories
- **Frontend Repo (this one)** – Streamlit UI code  
- **Backend Repo** – FastAPI + ML model code:  
  👉 [Insurance Premium Predictor – Backend](https://github.com/LakshyaMittal1/Insurance-Premium-Predictor-Backend-)
