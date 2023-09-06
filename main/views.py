from django.shortcuts import render

def show_main(request):
    context = {
        'name': 'Jeslyn Theodora',
        'class': 'PBP E'
    }

    return render(request, "main.html", context)
