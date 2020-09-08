from .models import Poll, Choices
from django import forms

class PollCreateForm(forms.ModelForm):
    class Meta:
        model = Poll
        fields = ['title', 'question', 'question_image']

class ChoiceCreateForm(forms.ModelForm):
    class Meta:
        model = Choices
        fields = ['choice_text', 'choice_image']
