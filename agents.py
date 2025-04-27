from crewai import Agent,Task,Crew
from langchain_groq import ChatGroq
import os
from dotenv import load_dotenv

load_dotenv()


llm = ChatGroq(
    api_key=os.getenv("GROQ_API_KEY"),
    model="groq/llama3-70b-8192",
    temperature=0
)

resume_evaluator = Agent(
    role="Resume Evaluator",
    goal="Determine if the resume matches the job description",
    backstory="You are an HR Expert evaluating resumes for a job",
    verbose=True,
    llm=llm
)

def get_screening_tasks(resume_text, job_text):
    return [
        Task(
            description=f"""
### RESUME TEXT ###
{resume_text}

### JOB DESCRIPTION ###
{job_text}

### INSTRUCTIONS ###
Evaluate whether the resume matches the job.

Respond using EXACTLY this format:

Shortlisted: Yes or No  
Reason: <concise explanation>

DO NOT say anything else. Do not explain. Do not preface the answer.
Begin directly with 'Shortlisted:'.
""",
            agent=resume_evaluator,
            expected_output="""
Shortlisted: Yes or No
Reason: A concise explanation (1-3 sentences)
"""
        )
    ]