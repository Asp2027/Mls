<<<<<<< HEAD
import pandas as pd
from sklearn.linear_model import LogisticRegression
from sklearn.preprocessing import LabelEncoder
import joblib

# 1. تحميل البيانات
df = pd.read_csv("grades.csv")

# 2. حساب متوسط الدرجات
df["Average"] = df[["Math", "English", "Science"]].mean(axis=1)

# 3. إنشاء عمود "Result" تلقائيًا
df["Result"] = df["Average"].apply(lambda x: "Pass" if x >= 60 else "Fail")

# 4. تجهيز البيانات
X = df[["Math", "English", "Science"]]
y = LabelEncoder().fit_transform(df["Result"])

# 5. تدريب النموذج
model = LogisticRegression()
model.fit(X, y)

# 6. حفظ النموذج
joblib.dump(model, "student_model.pkl")
print("✅ تم تدريب النموذج وحفظه بنجاح.")
=======
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
>>>>>>> bd892ca (Update requirement.txt)
