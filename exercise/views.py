from django.contrib.auth import authenticate, login, logout
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.db import IntegrityError
from django.contrib import messages
from .models import Exercise
from django.utils import timezone
from datetime import timedelta
from .forms import CppForm
from .utils import run_cpp
from django.http import HttpResponse


@login_required(login_url="login")
def exercise_view(request):
    exercises = Exercise.objects.all()
    context = {"exercises": exercises}
    return render(request, "exercise.html", context)


@login_required(login_url="login")
def exercise_detail_view(request, exercise_id):
    context = {}
    exercise = Exercise.objects.get(id=exercise_id)
    answer = exercise.answer

    if request.method == "POST":
        form = CppForm(request.POST)
        if form.is_valid():
            cpp_code = form.cleaned_data["cpp"]
            correct_msg = ""
            correct = False
            try:
                output, error = run_cpp(cpp_code)
                if str(output).strip() == str(answer).strip():
                    correct_msg = f"Answer Is Correct, Congrats!"
                    correct = True
                else:
                    if error:
                        correct_msg = "Compilation Error"
                    else:
                        correct_msg = f"Answer Is Not Correct.\nExpected:\n{answer}\nBut Found:\n{output}"
                context = {
                    "form": form,
                    "error": error,
                    "correct_msg": correct_msg,
                    "correct": correct,
                    "exercise": exercise,
                }
            except Exception as e:
                correct_msg = str(e)
                context = {
                    "form": form,
                    "error": str(e),
                    "correct_msg": correct_msg,
                    "correct": correct,
                    "exercise": exercise,
                }
    else:
        form = CppForm(initial={"cpp": exercise.prewritten_code})
        context = {
            "form": form,
            "exercise": exercise,
        }
    return render(request, "exercise_detail.html", context)


# def download_view(request):
#     code = request.GET.get("cpp", "")
#     response = HttpResponse(content_type="text/x-c++src")
#     response["Content-Disposition"] = 'attachment; filename="main.cpp"'
#     response.write(code)
#     return response
