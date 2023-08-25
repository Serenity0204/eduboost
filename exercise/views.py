from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .models import Exercise
from .forms import CppForm
from .utils import run_cpp
from django.core.paginator import Paginator
from django.http import HttpResponse


def exercise_view(request):
    request.session.set_expiry(900)
    exercises_list = Exercise.objects.all().order_by("id")

    paginator = Paginator(exercises_list, 5)  # Show 5 exercise per page.
    page_number = request.GET.get("page")
    exercises = paginator.get_page(page_number)

    context = {"exercises": exercises}
    return render(request, "exercise.html", context)


def exercise_search_view(request):
    request.session.set_expiry(900)  # Reset session expiry to 15 minutes (900 seconds)
    query = request.GET.get("query")
    if not query:
        return redirect("coding_exercise")

    exercises_list = Exercise.objects.filter(title__startswith=query).order_by("id")
    paginator = Paginator(exercises_list, 5)  # Show 5 exercise per page.
    page_number = request.GET.get("page")
    exercises = paginator.get_page(page_number)

    context = {"exercises": exercises}
    return render(request, "exercise.html", context)


@login_required(login_url="login")
def exercise_detail_view(request, exercise_id):
    request.session.set_expiry(900)
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
                    correct_msg = f"The Answer Is Correct, Congrats!"
                    correct = True
                else:
                    if error:
                        correct_msg = "Compilation Error"
                    else:
                        correct_msg = f"The Answer Is Not Correct.\nExpected:\n{answer}\nBut Found:\n{output}"
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
