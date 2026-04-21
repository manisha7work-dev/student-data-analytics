import pandas as pd
import matplotlib.pyplot as plt

# Load dataset
df = pd.read_csv("students.csv")

# ---- DATA CLEANING ----
print("\n--- Checking Missing Values ---")
print(df.isnull().sum())

# ---- ADD TOTAL & AVERAGE ----
df["Total"] = df["Math"] + df["Science"] + df["English"]
df["Average"] = df["Total"] / 3

# ---- GRADE FUNCTION ----
def assign_grade(avg):
    if avg >= 90:
        return 'A'
    elif avg >= 75:
        return 'B'
    elif avg >= 60:
        return 'C'
    else:
        return 'D'

df["Grade"] = df["Average"].apply(assign_grade)

# ---- BASIC ANALYSIS ----
print("\n--- BASIC ANALYSIS ---")
print("Average Marks:", df["Average"].mean())
print("Highest Marks:", df["Average"].max())
print("Lowest Marks:", df["Average"].min())

# ---- TOP STUDENTS ----
top_students = df.sort_values(by="Average", ascending=False).head(3)
print("\nTop 3 Students:\n", top_students[["Name", "Average"]])

# ---- SUBJECT-WISE AVERAGE ----
subject_avg = df[["Math", "Science", "English"]].mean()
print("\nSubject-wise Average:\n", subject_avg)

# ---- VISUALIZATION ----
plt.figure()
df.set_index("Name")["Average"].plot(kind="bar", title="Student Average Marks")
plt.xlabel("Students")
plt.ylabel("Average Marks")
plt.xticks(rotation=45)
plt.show()

plt.figure()
subject_avg.plot(kind="bar", title="Subject-wise Average Marks")
plt.xlabel("Subjects")
plt.ylabel("Marks")
plt.show()