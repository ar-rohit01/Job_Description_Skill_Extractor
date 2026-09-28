import streamlit as st

from model import get_model


st.set_page_config(
    page_title="Job Description Skill Extractor",
    page_icon="📄",
    layout="centered",
)


st.title("📄 Job Description Skill Extractor")

st.write(
    "Extract skills, experience, and education from a job description "
    "without assuming missing information."
)


job_description = st.text_area(
    "Paste the Job Description",
    height=250,
    placeholder="Paste a job description here...",
)


if st.button("Extract Information"):
    if not job_description.strip():
        st.warning("Please enter a job description.")
    else:
        try:
            model = get_model()
            result = model(job_description)

            st.subheader("Extracted Information")

            st.write("### Skills")

            if result.skills:
                for skill in result.skills:
                    st.write(f"- {skill}")
            else:
                st.write("No skills mentioned")

            st.write("### Experience")
            st.write(result.experience)

            st.write("### Education")
            st.write(result.education)

        except Exception as e:
            st.error(f"An error occurred: {e}")