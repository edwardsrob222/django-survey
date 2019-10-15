from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.contrib.auth.decorators import user_passes_test
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse, reverse_lazy
from django.views import generic
from .models import Question, Choice
from .forms import QuestionForm, ChoiceFormSet

class IndexView(generic.ListView):
    model = Question
    template_name = 'survey/index.html'
    # instead of using object_list
    context_object_name = 'question_list'


# detial view is used to render details of one item in specified table
class DetailView(generic.DetailView):
    model = Question
    template_name = 'survey/detail.html'


# detial view is used to render details of one item in specified table
class ResultsView(generic.DetailView):
    model = Question
    template_name = 'survey/results.html'

class CreateView(generic.CreateView):
    model = Question
    template_name = 'survey/create.html'
    fields = '__all__'

    def get_context_data(self, **kwargs):
        context = super(CreateView, self).get_context_data(**kwargs)
        if self.request.POST:
            context['form'] = QuestionForm(self.request.POST)
            context['formset'] = ChoiceFormSet(self.request.POST)
        else:
            context['form'] = QuestionForm()
            context['formset'] = ChoiceFormSet()
        return context

    def form_valid(self, form):
        context = self.get_context_data()
        form = context['form']
        formset = context['formset']
        if all([form.is_valid(), formset.is_valid()]):
            form.instance.created_by = self.request.user
            question = form.save()
            for inline_form in formset:
                if inline_form.cleaned_data:
                    choice = inline_form.save(commit=False)
                    choice.question = question
                    choice.save()
            return HttpResponseRedirect(reverse('survey:index',))
