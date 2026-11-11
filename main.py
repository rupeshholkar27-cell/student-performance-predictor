from database import Database
from models import Student

db = Database()

# Fill the cupboard only if it is empty
if db.get_all().empty:
    db.load_csv("data/students.csv")

# Add one new student (this should work)
db.add_student(Student("Test User", 6, 85, 22, 25, 17, 78))

# Try a wrong student (this should be caught)
try:
    Student("Bad Student", 30, 85, 22, 25, 17, 78)
except ValueError as e:
    print("Caught error:", e)

df = db.get_all()
print(df.shape)
print(df.tail())