import json, random
from django.shortcuts import render, redirect
from . models import Question, QuizSession
from . forms import QuizForm
from django.http import HttpResponse


def index(request):
    if request.method == 'POST':
        quiz_form = QuizForm(request.POST)
        if quiz_form.is_valid():
            num_questions = quiz_form.cleaned_data['num_questions']
            quiz_session = QuizSession.objects.create(no_of_questions=num_questions)
            quiz_session.questions.set(Question.objects.order_by('?')[:num_questions])
            quiz_session.save()
            
            return redirect('quiz', uuid=quiz_session.uuid)
        else:
            return render(request, 'quiz/index.html', {'form': quiz_form})
        
    return render(request, 'quiz/index.html')
    

def quiz(request, uuid):
    if request.method == 'GET':
        quiz_session = QuizSession.objects.get(uuid=uuid)
        questions_objects = list(quiz_session.questions.all())
        questions = []
        for question in questions_objects:
            options = [question.option1, question.option2, question.option3, question.option4]
            random.shuffle(options)
            question_dict = {
                'id': question.id,
                'question': question.question,
                'options': options,
            }
            questions.append(question_dict)
            
        questions_json = json.dumps(questions)
        return render(request, 'quiz/quiz.html', {'questions': questions_json})
    
def save_result(request, uuid):
    if request.method == 'POST':
        answers = json.loads(request.body)
        result = {
            "correct": 0,
            "incorrect": 0,
            "not_attempted": 0,
        }

        for answer in answers:
            question_id = answer['id']
            selected_option = answer['answer']
            question = Question.objects.get(id=question_id)
            if selected_option is not None:
                if selected_option == question.option1:
                    result["correct"] += 1
                else:
                    result["incorrect"] += 1 
            else:
                result["not_attempted"] += 1
                
                    
        quiz_session = QuizSession.objects.get(uuid=uuid)
        
        result["percentage"] = int((result["correct"] / quiz_session.no_of_questions) * 100)
        result["total"] = quiz_session.no_of_questions
        
        quiz_session.result = result
        quiz_session.save()
        return HttpResponse(json.dumps(result), content_type="application/json")
    
def result(request, uuid):
    if request.method == 'GET':
        quiz_session = QuizSession.objects.get(uuid=uuid)
        return render(request, 'quiz/result.html', {'result': quiz_session.result})