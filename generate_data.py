import numpy as np
import pandas as pd

np.random.seed(42)
n = 300

study_hours = np.random.uniform(1, 10, n)
attendance = np.random.uniform(50, 100, n)
internal1 = np.random.uniform(8, 30, n)
internal2 = np.random.uniform(8, 30, n)
assignment = np.random.uniform(8, 20, n)

semester_score = (
    0.9 * internal1
    + 0.9 * internal2
    + 1.0 * assignment
    + 3.0 * study_hours
    + 0.20 * attendance
    + np.random.normal(0, 5, n)
)
semester_score = np.clip(semester_score, 0, 100)

df = pd.DataFrame({
    "name": [f"Student_{i+1}" for i in range(n)],
    "study_hours": study_hours.round(1),
    "attendance": attendance.round(1),
    "internal1": internal1.round(1),
    "internal2": internal2.round(1),
    "assignment": assignment.round(1),
    "semester_score": semester_score.round(1),
})

import os
os.makedirs("data", exist_ok=True)
df.to_csv("data/students.csv", index=False)
print("Dataset created:", df.shape)