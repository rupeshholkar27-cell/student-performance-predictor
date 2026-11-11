import os
import subprocess
import sys

from database import Database


def load_data():
    if not os.path.exists("data/students.csv"):
        subprocess.run([sys.executable, "generate_data.py"], check=True)
    db = Database()
    if db.get_all().empty:
        db.load_csv("data/students.csv")
    df = db.get_all()
    df = df[df["name"] != "Test User"]
    return df


def summary(df):
    cols = ["study_hours", "attendance", "internal1",
            "internal2", "assignment", "semester_score"]
    return df[cols].describe().round(2)


def correlations(df):
    cols = ["study_hours", "attendance", "internal1",
            "internal2", "assignment", "semester_score"]
    corr = df[cols].corr()["semester_score"]
    return corr.drop("semester_score").sort_values(ascending=False).round(3)


if __name__ == "__main__":
    data = load_data()
    print("Number of students:", len(data))
    print()
    print("=== Summary (average, min, max...) ===")
    print(summary(data))
    print()
    print("=== What affects semester score? ===")
    print(correlations(data))