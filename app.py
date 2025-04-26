import streamlit as st
from resume_parser import extract_text_from_pdf,extract_text_from_docx
from agents import get_screening_tasks,Crew
from dotenv import load_dotenv

load_dotenv()

st.title("AI-Powered HR Screening System")

upload_resume = st.file_uploader("Upload Resume(pdf/docx)",type=['pdf','docx'])
job_description = st.text_area("Paste job description")

if st.button("Evaluate Candidate") and upload_resume and job_description:
    if upload_resume.name.endswith(".pdf"):
        resume_text = extract_text_from_pdf(upload_resume)

    else:
        resume_text = extract_text_from_docx(upload_resume)

    tasks = get_screening_tasks(resume_text,job_description)
    crew = Crew(agents=[tasks[0].agent],tasks=tasks,verbose=True)
    result = crew.kickoff()

    task_output = result.tasks_output[0]  
    raw_output = task_output.raw  

    if raw_output:
        st.subheader("Screening Result:")
        lines = raw_output.strip().split('\n')
        for line in lines:
            st.markdown(f"**{line.strip()}**")
    else:
        st.write("Could not extract screening result.")

