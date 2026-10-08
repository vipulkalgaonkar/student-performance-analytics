import pandas as pd
import numpy as np
from functions import calculate_total, calculate_average, assign_grade

df = pd.read_csv("students.csv")

df["Total"] = df.apply(calculate_total, axis=1)
df["Average"] = df.apply(calculate_average, axis=1)
df["Grade"] = df["Average"].apply(assign_grade)
df["Result"] = np.where(df["Average"] >= 40, "Pass", "Fail")

# Perform analysis
print("📊 Class Average:", df["Average"].mean())
print("✅ Total Passed:", (df["Result"] == "Pass").sum())
print("❌ Total Failed:", (df["Result"] == "Fail").sum())

print("\n Top 3 Students:")
print(df.nlargest(3, "Total")[["Name", "Total", "Grade"]])

print("\n📈 Subject-wise Averages:")
print(df[["Math", "Physics", "CS"]].mean())

print("\n🔝 Highest Total:", df["Total"].max())
print("🔻 Lowest Total:", df["Total"].min())
