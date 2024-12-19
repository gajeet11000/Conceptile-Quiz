from django import forms

class QuizForm(forms.Form):
    num_questions = forms.IntegerField(label='Please enter the number of questions', min_value=5, max_value=20,
        required=True,  
        error_messages={ 
            'required': 'This field is required.',
            'min_value': 'No. of questions must be at least 5.',
            'max_value': 'No. of questions cannot be more than 20.',
            'invalid': 'Enter a valid integer.',
        })
