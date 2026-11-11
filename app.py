import streamlit as st
import matplotlib.pyplot as plt

from analysis import load_data, summary, correlations
from predictor import train_model, predict_score

st.set_page_config(page_title="Student Performance Predictor")
st.title("🎓 Student Performance Predictor")
st.write("Predict the **semester exam score (out of 100)** from internal marks, assignment, study hours and attendance.")

df = load_data()

tab1, tab2, tab3 = st.tabs(["🔮 Predict", "📊 Insights", "📁 Data"])

# ---------- Tab 1: Predict ----------
with tab1:
    st.subheader("Enter student details")
    col1, col2 = st.columns(2)
    with col1:
        study_hours = st.slider("Study hours per day", 0.0, 12.0, 5.0, 0.5)
        attendance = st.slider("Attendance (%)", 0, 100, 75)
        assignment = st.slider("Assignment and project (out of 20)", 0.0, 20.0, 14.0, 0.5)
    with col2:
        internal1 = st.slider("Internal 1 (out of 30)", 0.0, 30.0, 18.0, 0.5)
        internal2 = st.slider("Internal 2 (out of 30)", 0.0, 30.0, 18.0, 0.5)

    if st.button("Predict semester score"):
        try:
            score = predict_score(study_hours, attendance,
                                  internal1, internal2, assignment)
            st.success(f"Predicted semester score: {score} / 100")
        except FileNotFoundError:
            st.error("Model not found. Run `python predictor.py` first.")

# ---------- Tab 2: Insights ----------
with tab2:
    st.subheader("What affects the semester score?")
    corr = correlations(df)
    fig, ax = plt.subplots()
    corr.plot(kind="barh", ax=ax)
    ax.set_xlabel("Correlation with semester score")
    st.pyplot(fig)

    st.subheader("Score distribution")
    fig2, ax2 = plt.subplots()
    ax2.hist(df["semester_score"], bins=15)
    ax2.set_xlabel("Semester score")
    ax2.set_ylabel("Number of students")
    st.pyplot(fig2)

    st.subheader("Class summary")
    st.dataframe(summary(df))

# ---------- Tab 3: Data ----------
with tab3:
    st.subheader("All students")
    st.dataframe(df)
    st.download_button("Download data as CSV",
                       df.to_csv(index=False),
                       file_name="students.csv")