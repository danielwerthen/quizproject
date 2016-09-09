from quiz.models import Quiz
from django.shortcuts import render


#quizzes = [
	#{
		#"quiz_number": 1,
		#"name": "Klassiska böcker",
		#"description": "Hur bra kan du dina klassiker?",
		#"image": "/static/Eniac.jpg",
	#},
	#{
		#"quiz_number": 2,
		#"name": "Största 1slagen",
		#"description": "Kan du dina lag?",
		#"image":"/static/madonna.png",
	#},
	#{
		#"quiz_number": 3,
		#"name": "Världens mest kända hackare",
		#"description": "Hackerhistoria är viktigt, kan du den?",
		#"image":"/static/teknisk.jpg",
	#},
#]

def start(request):
	context = {
		"quizzes": Quiz.objects.all(),
	}
	return render(request, "quiz/start.html", context)

def quiz(request, quiz_number):
	context = {
		"quiz": Quiz.objects.get(quiz_number=quiz_number),
		"quiz_number": quiz_number,
	}
	return render(request, "quiz/quiz.html", context)

def question(request, quiz_number, question_number):
	quiz = Quiz.objects.get(quiz_number=question_number)
	questions = quiz.questions.all()
	question = questions[int(question_number) - 1]
	context = {
		"question_number": question_number,
		"question": question.question,
		"answer1": question.answer1,
		"answer2": question.answer2,
		"answer3": question.answer3,
		"quiz": quiz,
		"quiz_number": quiz_number,
	}
	return render(request, "quiz/question.html", context)

def results(request, quiz_number):
	context= {
		"correct": 12,
		"total": 20,
		"quiz_number": quiz_number
	}
	return render(request, "quiz/results.html", context)