from django.shortcuts import render
import pandas as pd
import joblib

# Cargar modelo entrenado
model = joblib.load('prediccion/titanic_model.pkl')

def prediccion_titanic(request):
    resultado = None

    if request.method == "POST":
        pclass = int(request.POST.get("pclass"))
        sex = request.POST.get("sex")
        age = float(request.POST.get("age"))
        fare = float(request.POST.get("fare"))
        embarked = request.POST.get("embarked")

        input_data = pd.DataFrame({
            'Pclass':[pclass],
            'Sex':[sex],
            'Age':[age],
            'Fare':[fare],
            'Embarked':[embarked]
        })

        pred = model.predict(input_data)[0]
        proba = model.predict_proba(input_data)[0][1]*100

        resultado = {
            "sobrevive": "Sí" if pred==1 else "No",
            "probabilidad": f"{proba:.2f}%"
        }

    return render(request, "prediccion/formulario.html", {"resultado": resultado})