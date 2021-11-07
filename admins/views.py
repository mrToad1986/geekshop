from django.shortcuts import render, HttpResponseRedirect
from django.contrib.auth.decorators import user_passes_test
from django.urls import reverse

from users.models import User
from admins.forms import UserAdminRegistrationForm, UserAdminProfileForm

def index(request):
    return render(request, 'admins/index.html')

#CRUD (Create, Read, Update, Delete):

@user_passes_test(lambda u: u.is_staff)
def admin_users(request):
    context = {'title': 'Админ-панель - Пользовтаели', 'users': User.objects.all()}
    return render(request, 'admins/admin-users-read.html', context)

@user_passes_test(lambda u: u.is_staff)
def admin_users_create(request):
    if request.method == 'POST':
        form = UserAdminRegistrationForm(data=request.POST, files=request.FILES)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('admins:admin_users'))
    else:
        form = UserAdminRegistrationForm()
    context = {'title': 'Админ-панель - Создание пользователя', 'form': form}
    return render(request, 'admins/admin-users-create.html', context)

@user_passes_test(lambda u: u.is_staff)
def admin_users_update(request, id):
    selected_user = User.objects.get(id=id)
    if request.method == 'POST':
        form = UserAdminProfileForm(instance=selected_user, files=request.FILES, data=request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('admins:admin_users'))
    else:
        form = UserAdminProfileForm(instance=selected_user)
    context = {
        'title': 'Админ-панель - Редактирование пользовтаеля',
        'form': form,
        'selected_user': selected_user,
    }
    return render(request, 'admins/admin-users-update-delete.html', context)

@user_passes_test(lambda u: u.is_staff)
def admin_users_remove(request, id):
    user = User.objects.get(id=id)
    user.safe_delete()
    return HttpResponseRedirect(reverse('admins:admin_users'))
