# train_model.py
import pandas as pd
from sklearn.linear_model import LogisticRegression
from sklearn.preprocessing import LabelEncoder
from sklearn.model_selection import train_test_split
import joblib

df = pd.read_csv("grades.csv")

X = df[["Math", "English", "Science"]]
y = LabelEncoder().fit_transform(df["Result"])

model = LogisticRegression()
model.fit(X, y)

# حفظ النموذج
joblib.dump(model, "student_model.pkl")
print("✅ النموذج تم حفظه.")
