# 🤖 AI-Powered Resume Screening App

A smart and efficient resume screening tool built using AI that evaluates resumes against job descriptions and determines if a candidate should be shortlisted, along with a concise summary or reasoning.

---

## 🚀 Features

- 📄 Upload **PDF or DOCX** resumes
- 📝 Input job descriptions
- 🤖 AI-powered screening using **CrewAI**, **LangChain**, and **LLaMA (Groq)**
- 📊 Get instant results with **shortlisting decision** and **summary feedback**
- 🌐 Clean and interactive **Streamlit** web interface

---

## 🧠 How It Works

1. **Upload a resume** (`.pdf` or `.docx`)
2. **Paste or type a job description**
3. The app uses:
   - `Fitz` and `python-docx` for document parsing
   - `CrewAI` + `LangChain` to coordinate evaluation logic
   - `Groq LLaMA` model for natural language understanding and reasoning
4. It returns:
   - ✅ Shortlist Decision (Yes/No)
   - 🧾 Concise Reason or Summary

---

## 🛠 Tech Stack

- **Frontend**: Streamlit
- **LLM Orchestration**: LangChain, CrewAI
- **Model**: LLaMA via Groq API
- **Parsing**: Fitz (PDF), python-docx (DOCX)
- **Language**: Python 3.10+

---

## 📦 Installation

```bash
git clone https://github.com/hemantkumarlearning/AI-Powered-HR.git
cd AI-Powered-HR
pip install -r requirements.txt
streamlit run app.py
```

## Configuration
Ensure you have the following environment variables set in a .env file:

```
GROQ_API_KEY=your_groq_api_key
```

## Demo

![Screenshot 2025-04-27 203608](https://github.com/user-attachments/assets/1acb47fc-a9c1-43f4-99d7-b9ab6f9c87cd)
