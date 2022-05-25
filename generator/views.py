from django.shortcuts import render
import random


def home(request):
    return render(request, 'generator/home.html')


def password(request):

    length = int(request.GET.get('length'))
    base = list()
    characters = list('abcdefghijklmnopqrstuvwxyz')
    uppercase = list('ABCDEFGHIJKLMNOPQRSTUVWXYZ')
    numbers = list('0123456789')
    specials = list('~`@#$%^&*()_-=+')

    base.extend(characters)

    if request.GET.get('uppercase') == 'on':
        base.extend(uppercase)

    if request.GET.get('numbers') == 'on':
        base.extend(numbers)

    if request.GET.get('specials') == 'on':
        base.extend(specials)

    def generate():
        numbers_passed, uppercase_passed, specials_passed = True, True, True
        characters_passed = False

        password = ''
        for i in range(length):
            password += random.choice(base)

        if request.GET.get('uppercase') == 'on':
            uppercase_passed = False
            for i in password:
                if i in uppercase:
                    uppercase_passed = True
                    break

        if request.GET.get('numbers') == 'on':
            numbers_passed = False
            for i in password:
                if i in numbers:
                    numbers_passed = True
                    break

        if request.GET.get('specials') == 'on':
            specials_passed = False
            for i in password:
                if i in specials:
                    specials_passed = True
                    break

        for i in password:
            if i in characters:
                characters_passed = True
                break

        if numbers_passed and uppercase_passed and specials_passed and characters_passed:
            return password
        else:
            return generate()

    password = generate()

    return render(request, 'generator/password.html', {'password': password})
