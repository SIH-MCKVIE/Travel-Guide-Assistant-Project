# ✈️ Travel Guide Assistant (RAG-Powered)
<p align="center"> <img src="https://img.shields.io/badge/Status-Active-success?style=for-the-badge" /> <img src="https://img.shields.io/badge/Project-Type%3A%20AI%20Web%20App-blueviolet?style=for-the-badge" /> <img src="https://img.shields.io/badge/Level-Intermediate-orange?style=for-the-badge" /> </p> <p align="center"> <strong>Your AI-powered companion for planning unforgettable journeys 🌍</strong> </p>




## 🚀 Project Overview

Travel Guide Assistant is a smart travel recommendation web application that suggests destinations based on budget and interests, enriched with RAG (Retrieval-Augmented Generation), automated itineraries, and map-based exploration.

It blends AI reasoning, search, and modern UI to deliver personalized travel planning in seconds.




## ✨ Key Features

- 💰 Budget-aware destination recommendations

- 🎯 Interest-based filtering (beach, adventure, culture, nature)

- 📚 RAG-powered destination knowledge search

- 🗓️ Auto-generated multi-day itineraries

- 🗺️ Google Maps location preview

- 🖼️ Dynamic destination images

- ⚡ Fast & lightweight Flask backend

- 🎨 Modern responsive UI



## 🧠 RAG (Retrieval-Augmented Generation)

- This project uses RAG to improve recommendation quality:

- Destination guides stored as .txt files

- User interest is matched using semantic relevance

- Results are ranked, not just filtered

- Helps scale to thousands of destinations efficiently



## 🛠️ Tech Stack

### 🎨 Frontend
<p align="left"> <img src="https://cdn.jsdelivr.net/gh/devicons/devicon/icons/react/react-original.svg" width="42" alt="React"/> &nbsp;&nbsp; <img src="https://cdn.jsdelivr.net/gh/devicons/devicon/icons/javascript/javascript-original.svg" width="42" alt="JavaScript"/> &nbsp;&nbsp; <img src="https://cdn.jsdelivr.net/gh/devicons/devicon/icons/css3/css3-original.svg" width="42" alt="CSS3"/> </p>

### ⚙️ Backend
<p align="left"> <img src="https://cdn.jsdelivr.net/gh/devicons/devicon/icons/python/python-original.svg" width="42" alt="Python"/> &nbsp;&nbsp; <img src="https://cdn.jsdelivr.net/gh/devicons/devicon/icons/flask/flask-original.svg" width="42" alt="Flask"/> </p>

## 🧠 AI / Intelligence
<p align="left">
  <img src="https://cdn.jsdelivr.net/gh/devicons/devicon/icons/python/python-original.svg" width="38"/>
  &nbsp;&nbsp;
  <img src="https://raw.githubusercontent.com/simple-icons/simple-icons/develop/icons/openai.svg" width="38"/>
  &nbsp;&nbsp;
  <img src="https://img.icons8.com/color/48/artificial-intelligence.png" width="38"/>
</p>

- Retrieval Augmented Generation (RAG)
- Intelligent destination ranking
- Context-aware itinerary generation


## 🔗 APIs & Services
<p align="left">
  <img src="https://img.icons8.com/color/48/google-maps-new.png" width="38"/>
  &nbsp;&nbsp;
  <img src="https://img.icons8.com/ios-filled/50/fa314a/marker.png" width="38"/>
  &nbsp;&nbsp;
  <img src="https://img.icons8.com/fluency/48/api.png" width="38"/>
</p>

- Google Maps Embed API
- Location-based destination preview
- External image & data services



## 📂 Project Structure
```text
Travel-Guide-Assistant/
│
├── backend/
│   ├── app.py
│   ├── config.py
│   ├── requirements.txt
│   ├── data/
│   │   ├── destinations.json
│   │   └── guides/
│   ├── routes/
│   ├── services/
│   └── utils/
│
├── static/
│   ├── style.css
│   └── main.js
│
├── templates/
│   └── index.html
│
└── README.md
```



## ▶️ How to Run the Project

### 1️⃣ Clone the Repository
```bash
git clone https://github.com/SIH-MCKVIE/Travel-Guide-Assistant-Project.git
cd Travel-Guide-Assistant-Project
```

### 2️⃣ Go to Backend Folder
```bash
cd backend
```

### 3️⃣ Create Virtual Environment
```bash
python -m venv tassistant
```

### 4️⃣ Activate Virtual Environment

**Windows (PowerShell):**
```powershell
Set-ExecutionPolicy -Scope Process -ExecutionPolicy Bypass
.\tassistant\Scripts\Activate.ps1
```

**Windows (CMD):**
```cmd
tassistant\Scripts\activate
```

### 5️⃣ Install Dependencies
```bash
pip install -r requirements.txt
```

### 6️⃣ Run the Flask Server
```bash
python app.py
```

### 7️⃣ Open in Browser
```text
http://127.0.0.1:5000
```

## 💡 Sample Inputs
```
| Budget (₹) | Interest   |
|-----------:|------------|
| 15000      | beach      |
| 20000      | adventure  |
| 10000      | culture    |
| 18000      | nature     |
| 25000      | mountain   |
```

## 🌟 Creative Highlights
- AI + RAG based ranking instead of simple filters

- Modular backend architecture

- Clean, visually appealing UI

- Scalable design for large destination datasets


## 📌 Future Enhancements

- 🔐 User login & saved itineraries  
- ✈️ Booking integrations  
- 🌐 Multilingual support  
- 📊 Budget tracking dashboard  
- 🤖 LLM-based conversational travel assistant  

