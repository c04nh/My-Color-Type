from django.shortcuts import render

from main.models import Question, Type, Color


def index(request):
    return render(request, 'index.html')

def form(request):
    questions = Question.objects.all()

    context = {
        'questions' : questions,
    }

    return render(request, 'form.html', context=context)

def result(request):
    N = Question.objects.count()
    K = Type.objects.count()
    T = Color.objects.count()

    counter = [0] * (K+1)
    counter2 = [0] * (T+1)

    for n in range(1, N+1):
        type_id = int(request.POST[f'question-{n}'][0])
        counter[type_id] += 1

    best_type_id1 = max(range(1, 2 + 1), key=lambda id : counter[id])
    best_type1 = str(Type.objects.get(pk=best_type_id1))

    best_type_id2 = max(range(3, 4 + 1), key=lambda id: counter[id])
    best_type2 = str(Type.objects.get(pk=best_type_id2))

    best_type_id3 = max(range(5, 6 + 1), key=lambda id: counter[id])
    best_type3 = str(Type.objects.get(pk=best_type_id3))

    best_type_id4 = max(range(7, 8 + 1), key=lambda id: counter[id])
    best_type4 = str(Type.objects.get(pk=best_type_id4))

    if best_type1 == 'E':
        counter2[1] += 1
        counter2[2] += 1
        counter2[3] += 1
        counter2[4] += 1
        counter2[5] += 1
        counter2[6] += 1
        counter2[7] += 1
        counter2[8] += 1
    elif best_type1 == 'I':
        counter2[9] += 1
        counter2[10] += 1
        counter2[11] += 1
        counter2[12] += 1
        counter2[13] += 1
        counter2[14] += 1
        counter2[15] += 1
        counter2[16] += 1

    if best_type2 == 'S':
        counter2[1] += 1
        counter2[2] += 1
        counter2[3] += 1
        counter2[4] += 1
        counter2[9] += 1
        counter2[10] += 1
        counter2[11] += 1
        counter2[12] += 1
    elif best_type2 == 'N':
        counter2[5] += 1
        counter2[6] += 1
        counter2[7] += 1
        counter2[8] += 1
        counter2[13] += 1
        counter2[14] += 1
        counter2[15] += 1
        counter2[16] += 1

    if best_type3 == 'T':
        counter2[1] += 1
        counter2[2] += 1
        counter2[5] += 1
        counter2[6] += 1
        counter2[9] += 1
        counter2[10] += 1
        counter2[13] += 1
        counter2[14] += 1
    elif best_type3 == 'F':
        counter2[3] += 1
        counter2[4] += 1
        counter2[7] += 1
        counter2[8] += 1
        counter2[11] += 1
        counter2[12] += 1
        counter2[15] += 1
        counter2[16] += 1

    if best_type4 == 'P':
        counter2[1] += 1
        counter2[3] += 1
        counter2[5] += 1
        counter2[7] += 1
        counter2[9] += 1
        counter2[11] += 1
        counter2[13] += 1
        counter2[15] += 1
    elif best_type4 == 'J':
        counter2[2] += 1
        counter2[4] += 1
        counter2[6] += 1
        counter2[8] += 1
        counter2[10] += 1
        counter2[12] += 1
        counter2[14] += 1
        counter2[16] += 1

    best_color_id = max(range(1, T+1), key=lambda id: counter2[id])
    best_color = Color.objects.get(pk=best_color_id)

    context = {
        'color': best_color
    }

    return render(request, 'result.html', context)