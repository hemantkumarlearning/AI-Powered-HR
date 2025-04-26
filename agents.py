from crewai import Agent,Task,Crew
from langchain_groq import ChatGroq
import os
from dotenv import load_dotenv

load_dotenv()


llm = ChatGroq(
    api_key=os.getenv("GROQ_API_KEY"),
    model="groq/llama3-70b-8192"
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
Compare the following resume with the job description.

Resume:
{resume_text}

Job Description:
{job_text}

Decide whether this candidate should be shortlisted.
Respond **only** in the following format:

Shortlisted: Yes or No  
Reason: A concise explanation (1-3 sentences) based on skills, experience, and relevance to the job.
""",
            agent=resume_evaluator,
            expected_output="""
Shortlisted: Yes or No
Reason: A concise explanation (1-3 sentences)
"""
        )
    ]