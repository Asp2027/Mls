from django.shortcuts import render
from .forms import GradeForm
import joblib
import pandas as pd

model = joblib.load("student_model.pkl")

def predict_view(request):
    prediction = None

    if request.method == "POST":
        form = GradeForm(request.POST)
        if form.is_valid():
            data = pd.DataFrame([[form.cleaned_data["math"], form.cleaned_data["english"], form.cleaned_data["science"]]],
                                columns=["Math", "English", "Science"])
            result = model.predict(data)[0]
            prediction = "Pass" if result == 1 else "Fail"
    else:
        form = GradeForm()

    return render(request, "appmlstudents/form.html", {
        "form": form,
        "prediction": prediction
    })