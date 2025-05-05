from django.shortcuts import render
from django.http import JsonResponse
import pandas as pd
import pickle
import numpy as np

# Load data and model
car = pd.read_csv("Cleaned_car.csv")
model = pickle.load(open("LinearRegressionModel.pkl", 'rb'))

def index(request):
    companies = sorted(car['company'].unique())
    car_models = sorted(car['name'].unique())
    years = sorted(car['year'].unique(), reverse=True)
    fuel_types = car['fuel_type'].unique()

    context = {
        'companies': companies,
        'car_models': car_models,
        'years': years,
        'fuel_types': fuel_types
    }
    return render(request, 'index.html', context)

def predict(request):
    if request.method == 'POST':
        company = request.POST.get('company')
        car_model = request.POST.get('car_model')
        year = int(request.POST.get('year'))
        fuel_type = request.POST.get('fuel_type')
        kms_driven = int(request.POST.get('kilo_driven'))

        prediction = model.predict(pd.DataFrame(
            [[car_model, company, year, kms_driven, fuel_type]],
            columns=['name', 'company', 'year', 'kms_driven', 'fuel_type']
        ))
        predicted_price = np.round(prediction[0], 2)
        return JsonResponse({'price': predicted_price})

def chatbot_page(request):
    return render(request, 'chatbot.html')