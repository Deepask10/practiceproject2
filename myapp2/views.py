from django.http import HttpResponse


def home(request):
    return HttpResponse("Welcome to for loop assignment")


def evenlist(request):
    numbers = [10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]
    even_numbers = []

    for num in numbers:
        if num % 2 == 0:
            even_numbers.append(num)

    return HttpResponse(f"Even numbers list = {even_numbers}")


def oddlist(request):
    numbers = [10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]
    odd_numbers = []

    for num in numbers:
        if num % 2 != 0:
            odd_numbers.append(num)

    return HttpResponse(f"Odd numbers list = {odd_numbers}")


def oddindexlist(request):
    numbers = [10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]
    odd_index_values = []

    for i in range(len(numbers)):
        if i % 2 != 0:
            odd_index_values.append(numbers[i])

    return HttpResponse(f"Odd index values = {odd_index_values}")
