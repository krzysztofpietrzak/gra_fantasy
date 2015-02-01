from django.shortcuts import render, render_to_response

# Create your views here.
def index(request):
    # user = request.user
    # if user.is_active and user.username!='pmanager':
    #     gracz = Gracz.objects.get(nazwa=user.username)

    # return render(request, 'index.html')
    return render_to_response('index.html', locals())