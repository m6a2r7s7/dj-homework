from django.shortcuts import render
from django.http import HttpResponse

DATA = {
    'omlet': {
        'яйца, шт': 2,
        'молоко, л': 0.1,
        'соль, ч.л.': 0.5,
    },
    'pasta': {
        'макароны, г': 0.3,
        'сыр, г': 0.05,
    },
    'buter': {
        'хлеб, ломтик': 1,
        'колбаса, ломтик': 1,
        'сыр, ломтик': 1,
        'помидор, ломтик': 1,
    },
    'soup' : {
        'шампиньоны, гр' : 400,
        'лук' : 2,
        'сливки, мл': 400,
        'вода, мл': 100
    }
    # можете добавить свои рецепты ;)
}

# Напишите ваш обработчик. Используйте DATA как источник данных
# Результат - render(request, 'calculator/index.html', context)
# В качестве контекста должен быть передан словарь с рецептом:
# context = {
#   'recipe': {
#     'ингредиент1': количество1,
#     'ингредиент2': количество2,
#   }
# }

def view(request, dish):
    servings = int(request.GET.get("servings", 1))
    for d in DATA:
        if d == dish:
            for i in DATA[d]:
                DATA[d][i] *= servings
                context = {'recipe': DATA[d]}
                return HttpResponse(render(request, 'calculator/index.html', context))