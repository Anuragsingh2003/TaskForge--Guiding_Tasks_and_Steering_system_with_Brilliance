from django.contrib.auth.forms import AuthenticationForm
# Create your views here
from django. contrib import messages
from .forms import RegistrationForm
from django.http import HttpResponse
from django.contrib.auth import authenticate,login
from .models import *
from django.contrib.auth.models import User
from django.shortcuts import render, redirect,get_object_or_404
from .forms import *
from django.contrib.auth.decorators import login_required




def index(request):
    return render(request,'index.html')

#employee or users section start...........................................................................................

def register(request):
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password1')
            user=form.save()
            user = authenticate(request, username=username, password=password) # for login 
            #this line makes the error - bcz login authenticn not working nd also ther is no need to use..
            # login(request,user) 
            #messages.success(request, f'Account created for {username}!')
            return redirect('user_login')# redirecting to login func for users
    else:
        form = RegistrationForm()
    return render(request, 'user/register.html', {'form': form})

def user_login(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                if user.is_superuser:
                    messages.error(request, 'Superuser cannot log in to user dashboard.')
                else:
                    login(request, user)
                    request.session['username'] = username  # create session
                    return redirect('usr_dash')
            else:
                messages.error(request, 'Invalid username or password.')
    else:
        form = AuthenticationForm()
    return render(request, 'user/user_login.html', {'form': form})


#def usr_dash(request):
    #return render(request,'user/user_dash.html')
@login_required
def usr_dash(request):
    username = request.session.get('username', None)
    if username is None:
        return redirect('user_login')
    user = User.objects.get(username=username)
    tasks = Tasks.objects.filter(user=user)
    try:
        email = user.email
    except email.DoesNotExist:
        email = None

    return render(request, 'user/user_dash.html', {'user': user, 'email': email, 'tasks': tasks})# bcz we want to use sessions usr name or data
@login_required
def user_tasks(request):
    username = request.session.get('username', None)
    if username is None:
        return redirect('user_login')
    user = User.objects.get(username=username)#injecting session in users tasks .html
    tasks = Tasks.objects.filter(user=user)
    return render(request, 'user/user_tasks.html', {'tasks': tasks})

@login_required
def status_updates(request, task_id):
    task = get_object_or_404(Tasks, tid=task_id)#setting present task id to tid to do further logic
    if request.method == 'POST':
        form = UpdateForm(request.POST, instance=task) #2-this check is anyone click on any btn and form mthd=post
        if form.is_valid():
            form.save()
            return redirect('user_tasks')#3- when in edit.html when anyone click on save btn it , check if condt , then save.
    else:
        #note- 'instance' means we want to wirk with same id of data , we want here in this func 
        form = UpdateForm(instance=task) #note-form is maded acrd to our forms Tskform elmnt , and save all thing in obj form
    return render(request, 'user/status_updates.html', {'form': form, 'task': task}) #1- that we use in edit.html, i.e= form.as p

@login_required
def create_leave(request):
    if request.method == 'POST':
        leaveForm = ApplyLeaveForm(request.POST)
        if leaveForm.is_valid():  # Corrected is_valid() method call
            form = leaveForm.save(commit=False)  # Save the form instance without committing to the database
            form.user_id = request.user.id  # Assign the user_id
            form.save()  # Save the form instance to the database
            return HttpResponse('success')
    else:
        leaveForm = ApplyLeaveForm()
    context = {'leaveForm': leaveForm}
    return render(request, 'user/apply_leave.html', context)



def leave_status(request):
    # Retrieve the leaves applied by the logged-in user
    leaves = Leave_apply.objects.filter(user=request.user)
    # Pass the leaves to the template
    return render(request, 'user/leave_status.html', {'leaves': leaves})

@login_required
def task_more(request, task_id):
    task = get_object_or_404(Tasks, tid=task_id)
    return render(request, 'user/task_more.html', {'task': task})
    
    
    
        #note- 'instance' means we want to wirk with same id of data , we want here in this func 
         #note-form is maded acrd to our forms Tskform elmnt , and save all thing in obj form
    
# admin section start............................................................................................

def admin_login(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None and user.is_superuser:
                login(request, user)
                return redirect('admin_d')
    else:
        form = AuthenticationForm()
    return render(request, 'admin/login.html', {'form': form})

@login_required
def admin_d(request):
    return render(request,'admin/admin_dash.html')



@login_required
def create_task(request):
    if request.method == 'POST':
        form = TaskForm(request.POST,request.FILES)
        if form.is_valid():
            Form = form.save(commit=True)
            Form.author = request.user
            Form.save()
            return HttpResponse('sucess')
    else:
        form = TaskForm()
    return render(request, 'admin/create_task.html', {'form': form})

@login_required
def manage_task(request):
    tasks = Tasks.objects.all()
    context = {'tasks': tasks}
    return render(request,'admin/manage_task.html',context)


# it is compolsry to use task_id in func edit_tsk and not any oter wrds , i.e=not tid or id
@login_required
def edit_task(request, task_id):
    task = get_object_or_404(Tasks, tid=task_id)
    if request.method == 'POST':
        form = TaskForm(request.POST, instance=task) #2-this check is anyone click on any btn and form mthd=post
        if form.is_valid():
            form.save()
            return redirect('manage_task')#3- when in edit.html when anyone click on save btn it , check if condt , then save.
    else:
        #note- 'instance' means we want to wirk with same id of data , we want here in this func 
        form = TaskForm(instance=task) #note-form is maded acrd to our forms Tskform elmnt , and save all thing in obj form
    return render(request, 'admin/edit.html', {'form': form, 'task': task}) #1- that we use in edit.html, i.e= form.as p

@login_required
def del_task(request, task_id):
    task = get_object_or_404(Tasks, tid=task_id)
    if request.method == 'POST':
        task.delete()
        return redirect('manage_task')
    return render(request, 'admin/del_task.html', {'task': task})

@login_required
def leaves_list(request):
    leaves=Leave_apply.objects.all()
    data={'leaves':leaves}
    return render(request,'admin/leave_list.html',data)

@login_required
def accept_leave(request, leave_id): #1 firstly getting id of leave through url.py
    leave = get_object_or_404(Leave_apply, lid=leave_id) #2 then saving or changing leave id to actual lid to get or work with correct leave applic
    leave.status = 'Approved' #3 then u know if anyone cll this view func it will changed leave status to approve
    leave.save() #4 then save
    return redirect('leaves_list')

@login_required
def reject_leave(request, leave_id):
    leave = get_object_or_404(Leave_apply, lid=leave_id)
    leave.status = 'Rejected'
    leave.save()
    return redirect('leaves_list')

@login_required
def full_message_view(request, leave_id):
    leave = Leave_apply.objects.get(lid=leave_id)
    return render(request, 'admin/full_message.html', {'leave': leave})

@login_required
def task_desc(request, task_id):
    task = get_object_or_404(Tasks, tid=task_id)
    return render(request, 'admin/task_desc.html', {'task': task})