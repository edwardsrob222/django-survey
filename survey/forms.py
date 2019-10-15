from django.forms import formset_factory
from django import forms
from .models import Question, Choice

class QuestionForm(forms.ModelForm):

    class Meta:
        model = Question
        fields = ('question_text',)


class ChoiceForm(forms.ModelForm):

    class Meta:
        model = Choice
        fields = ('choice_text',)

ChoiceFormSet = formset_factory(ChoiceForm, extra=0,
                                min_num=2, validate_min=True)
