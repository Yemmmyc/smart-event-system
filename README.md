# 🏟️ Smart Event Experience System

## 📌 Problem Statement
Large-scale sporting venues face challenges such as:
- Crowd congestion
- Long waiting times
- Poor real-time coordination

These issues reduce attendee satisfaction and can pose safety risks.

---

## 💡 Solution
The Smart Event Experience System improves the physical event experience by:

- Monitoring crowd levels in real time
- Recommending less crowded entry points
- Providing live alerts to attendees
- Displaying information via a web dashboard

---

## 🏗️ System Architecture
User (Browser)
↓
Frontend (Dashboard UI)
↓
Backend API (Flask)
↓
Crowd Data & Alerts

---

## ☁️ Google Cloud Integration

This solution is designed using Google Cloud services:

- **Cloud Run** → Hosts backend APIs  
- **Firestore** → Stores crowd and event data  
- **Pub/Sub** → Handles real-time alerts  
- **Firebase Hosting** → Hosts frontend dashboard  

---

## 💻 Development Environment

This project was developed and tested using **Google Antigravity IDE**.

---

## ⚙️ How to Run the Project

### Backend
cd backend
pip install flask flask-cors
python main.py

### Frontend
cd frontend
npx serve .


Then open:
http://localhost:3000


---

## 🚀 Features

- Real-time crowd monitoring
- Dynamic alert system
- Smart gate recommendations
- Modern dashboard UI

---

## 📎 Repository Link
https://github.com/Yemmmyc/smart-event-system