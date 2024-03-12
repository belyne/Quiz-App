from django.shortcuts import render, redirect
from .models import Question

def home(request):
  return render(request, 'home.html')

def quiz(request):
  if request.method == 'POST':
    score = 0
    questions = Question.objects.all()
    
    for question in questions:
      selected_option = request.POST.get(str(question.id))
      if selected_option == question.correct_option:
        score += 1
    
    request.session['score'] = score
    return redirect('home')
  
  questions = Question.objects.all()
  return render(request, 'quiz.html', {'questions': questions})
        