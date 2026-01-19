# 🤖 AI Interview Coach

A GenAI-powered mock interview platform that simulates real interviews with 
**multi-round questions, difficulty levels, and AI evaluation** using Google Gemini.

---

## 🚀 Features

- 🧩 3-question interview flow  
- 🎯 Difficulty levels – Easy / Medium / Hard  
- 💼 Role-based questions (Product, Analytics, Consulting, Civil)  
- 🧠 AI evaluation with score & feedback  
- ✍ Model answers for improvement  
- 🌐 Clean Flask web interface

---

## 🛠 Tech Stack

- **Backend:** Flask (Python)  
- **AI Model:** Google Gemini  
- **Frontend:** HTML, Bootstrap  
- **Prompt Engineering**  
- **Session-based workflow**

---

## 📁 Project Structure

interview_coach/

│── app.py

│── config.py

│── requirements.txt

│── .env

│
├── utils/

│ └── engine.py

│

└── templates/

├── index.html

├── interview.html

└── result.html


---

## How to Run Locally

1. Clone Repository

```bash
git clone https://github.com/Sindhu2k3/ai-interview-coach.git
cd ai-interview-coach 
```

2. Install Dependencies

pip install -r requirements.txt

3. Create .env file

OPENAI_API_KEY=your_gemini_api_key

4. Run Application

python app.py


🧠 How It Works

User selects role + difficulty

System generates 3 interview questions

User answers sequentially

AI evaluates based on:

Communication

Structure

Domain knowledge

Provides:

Overall score

Question-wise feedback

Improved sample answers

💡 Learning Outcomes

Prompt engineering for structured output

Multi-step conversational flow

Flask session management

AI evaluation design

Frontend + backend integration

📌 Future Scope

Timer-based interviews

Voice input support

PDF report generation

Analytics dashboard
