from django import forms

class QuizForm(forms.Form):
    num_questions = forms.IntegerField(label='Please enter the number of questions', min_value=5, max_value=20)
