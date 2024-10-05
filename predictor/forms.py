from django import forms

class StrokePredictionForm(forms.Form):
    GENDER_CHOICES = [
        ('', 'Select Gender'),  # Adding an empty option
        ('0', 'Female'),
        ('1', 'Male'),
        ('2', 'Other'),
    ]
    EVER_MARRIED_CHOICES = [
        ('', 'Select...'),  # Adding an empty option
        ('0', 'No'),
        ('1', 'Yes'),
    ]
    WORK_TYPE_CHOICES = [
        ('', 'Select Work Type'),  # Adding an empty option
        ('0', 'Govt_job'),
        ('1', 'Never_worked'),
        ('2', 'Private'),
        ('3', 'Self-employed'),
        ('4', 'Children'),
    ]
    RESIDENCE_TYPE_CHOICES = [
        ('', 'Select Residence'),  # Adding an empty option
        ('0', 'Rural'),
        ('1', 'Urban'),
    ]
    SMOKING_STATUS_CHOICES = [
        ('', 'Select Smoking Status'),  # Adding an empty option
        ('0', 'Unknown'),
        ('1', 'formerly smoked'),
        ('2', 'never smoked'),
        ('3', 'smokes'),
    ]

    gender = forms.ChoiceField(choices=GENDER_CHOICES, label='Select Gender:')
    ever_married = forms.ChoiceField(choices=EVER_MARRIED_CHOICES, label='Are you married?')
    work_type = forms.ChoiceField(choices=WORK_TYPE_CHOICES, label='What is your work type?')
    residence_type = forms.ChoiceField(choices=RESIDENCE_TYPE_CHOICES, label='Residence Type:')
    smoking_status = forms.ChoiceField(choices=SMOKING_STATUS_CHOICES, label='Smoking Status:')
    age = forms.IntegerField(label='Enter your age:')
    avg_glucose_level = forms.FloatField(label='Average glucose level:')
    bmi = forms.FloatField(label='Body Mass Index (BMI):')
    hypertension = forms.ChoiceField(choices=[('', 'Select Hypertension Status'), ('0', 'No'), ('1', 'Yes')], label='Do you have hypertension?')
    heart_disease = forms.ChoiceField(choices=[('', 'Select Heart Disease Status'), ('0', 'No'), ('1', 'Yes')], label='Do you have heart disease?')


    def __init__(self, *args, **kwargs):
        super(StrokePredictionForm, self).__init__(*args, **kwargs)
        # Reset all fields to their initial state
        for field in self.fields:
            self.fields[field].initial = None
