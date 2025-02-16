# Air Quality Detector - Setup Guide

## 📁 Folder Structure
```
air-quality-webapp/
│── backend/                  # FastAPI Backend
│   ├── app/
│   │   ├── main.py           # FastAPI server & API endpoints
│   │   ├── config.py         # Configuration (API keys, settings)
│   │   ├── models.py         # Data models (if using DB)
│   │   ├── services.py       # External API calls (fetch air quality data)
│   │   ├── websocket.py      # WebSockets for real-time updates (optional)
│   │   ├── database.py       # Database setup (if using Firebase/PostgreSQL)
│   │   ├── utils.py          # Helper functions
│   ├── requirements.txt      # Dependencies for FastAPI
│   ├── Dockerfile            # Docker setup for deployment
│   ├── .env                  # API keys & environment variables
│── frontend/                 # Next.js Frontend
│   ├── public/               # Static files (icons, manifest.json)
│   ├── src/
│   │   ├── components/       # Reusable UI components
│   │   ├── pages/            # Next.js pages (index.tsx, about.tsx)
│   │   ├── hooks/            # Custom React hooks (e.g., useAirQuality.ts)
│   │   ├── utils/            # Helper functions
│   │   ├── services/         # API calls (fetch air quality data)
│   │   ├── styles/           # TailwindCSS styles
│   │   ├── contexts/         # Context API (if using global state)
│   ├── package.json          # Dependencies for Next.js
│   ├── next.config.js        # Next.js configuration
│   ├── tailwind.config.js    # TailwindCSS configuration
│   ├── .env.local            # Environment variables (API keys)
│   ├── tsconfig.json         # TypeScript configuration (optional)
│── README.md                 # Project documentation
│── .gitignore                # Files to ignore in Git
│── docker-compose.yml        # Docker Compose setup
```

---

## 🚀 Setup Instructions

### **1️⃣ Clone the Repository**
```bash
git clone https://github.com/mctrinity/air_quality_detector.git
cd air_quality_detector
```

### **2️⃣ Backend Setup (FastAPI)**
```bash
cd backend
python -m venv venv
source venv/bin/activate  # On Windows use: venv\Scripts\activate
pip install -r requirements.txt
```

#### **Run the FastAPI Server**
```bash
uvicorn app.main:app --host 0.0.0.0 --port 8000
```

---

### **3️⃣ Frontend Setup (Next.js)**
```bash
cd frontend
npm install  # or yarn install
```

#### **Run the Next.js Development Server**
```bash
npm run dev  # or yarn dev
```

---

## 🐳 Running with Docker

### **4️⃣ Build & Start with Docker Compose**
```bash
docker-compose up --build
```

### **5️⃣ Stop Docker Containers**
```bash
docker-compose down
```

---

## ✅ API Endpoints
| Method | Endpoint          | Description                   |
|--------|------------------|-------------------------------|
| GET    | `/air-quality?lat=xx&lon=yy` | Fetch air quality data |

---

## 🔥 Deployment (Optional)
For deployment, you can use:
- **Vercel** (for Next.js frontend)
- **Railway/Render** (for FastAPI backend)

Let me know if you need further customizations! 🚀
