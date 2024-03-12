# questions.py
import os
import django

# Set the environment variable to specify the Django settings module
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "quiz_project.settings")
django.setup()
from quiz_app.models import Question

Question.objects.create(
    question_text="What is the capital of France?",
    option1="Paris",
    option2="Berlin",
    option3="Madrid",
    option4="Rome",
    correct_option="Paris"
)

Question.objects.create(
    question_text="Which planet is known as the Red Planet?",
    option1="Earth",
    option2="Mars",
    option3="Venus",
    option4="Jupiter",
    correct_option="Mars"
)

# Add more questions as needed
