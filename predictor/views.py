import joblib
import os
from django.shortcuts import render,redirect
from .forms import StrokePredictionForm
from django.contrib import messages
import pandas as pd

# Load your pre-trained model and encoders
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
model_path = os.path.join(BASE_DIR, 'predictor', 'model', 'random_forest_model.pkl')

# Load the model
model = joblib.load(model_path)


def home(request):
    if request.method == 'POST':
        form = StrokePredictionForm(request.POST)

        if form.is_valid():
            input_data = form.cleaned_data
            
            # Define the feature names used during training
            feature_names = ['gender', 'age', 'hypertension', 'heart_disease', 'ever_married', 
                             'work_type', 'Residence_type', 'avg_glucose_level', 'bmi', 'smoking_status']

            # Create a DataFrame for the input data
            input_df = pd.DataFrame([[
                input_data['gender'],
                input_data['age'],
                input_data['hypertension'],
                input_data['heart_disease'],
                input_data['ever_married'],
                input_data['work_type'],
                input_data['residence_type'],  # Ensure this matches the trained model's feature
                input_data['avg_glucose_level'],
                input_data['bmi'],
                input_data['smoking_status']
            ]], columns=feature_names)

            # Make the prediction
            prediction = model.predict(input_df)[0]

            # Handle the prediction result
            if prediction == 1:
                messages.error(request, "The patient is likely to have a stroke.")
            else:
                messages.success(request, "The patient is not likely to have a stroke.")

            # Redirect to the same page to reset the form
            return redirect('home')  # Ensure 'home' is the name of your URL pattern
    else:
        form = StrokePredictionForm()  # Create an empty form for GET requests

    return render(request, 'home.html', {'form': form})
