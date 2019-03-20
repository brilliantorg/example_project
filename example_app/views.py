from django.shortcuts import render

def hello_world(request):
    context = {
        'msg': 'hello world!',
    }
    return render(request, 'hello_world.html', context)
