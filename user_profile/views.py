from django.shortcuts import render
from django.contrib.auth.models import User
from .models import *
from django.db import connection
from django.http import Http404, HttpResponseRedirect

# Create your views here.
def profile_user(request):
    sales = Sales.objects.filter(User_id=request.user.id)
    if request.method == 'POST':
        login = request.POST.get('login')
        mail = request.POST.get('mail')
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')

        try:
            User.objects.get(username=login)
            message = 1
            return render(request, 'UserProf/profile_user.html', {'sales': sales, 'message': message})
        except User.DoesNotExist:
            with connection.cursor() as cursor:
                cursor.execute(
                    f'''UPDATE auth_user set username ='{login}',
                                    last_name = '{last_name}',
                                    first_name ='{first_name}', 
                                    email ='{mail}' 
                                    where id ={request.user.id};''')
                return HttpResponseRedirect('/profile/')

    return render(request, 'UserProf/profile_user.html', {'sales': sales})
