from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.contrib.auth.decorators import user_passes_test
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse, reverse_lazy
from django.views import generic
from .models import Question, Choice
# from .forms import QuestionForm

# Create your views here.
class IndexView(generic.ListView):
    template_name = 'survey/index.html'
    # instead of using object_list
    context_object_name = 'question_list'

    def get_queryset(self):
        """Return the last five published questions."""
        return Question.objects.all()

# class DetailView(generic.DetailView):
#     model = Question
#     template_name = 'survey/detail.html'

# class ResultsView(generic.DetailView):
#     model = Question
#     template_name = 'survey/results.html'

class CreateView(generic.CreateView):
    model = Question
    fields = '__all__'
    template_name = 'survey/create.html'

# def create_survey(request, question_id):
