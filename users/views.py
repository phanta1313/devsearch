from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from django.contrib.auth.models import User
from .models import *
from .forms import *


def profiles(request):
    search_query = ''
    if request.GET.get('search_query'):
        search_query = request.GET.get('search_query')

    profiles = Profile.objects.filter(name__icontains = search_query)

    
    context = {'profiles' : profiles, 'search_query' : search_query}
    return render(request, 'profiles.html', context)

def profile(request, pk):
    profile = Profile.objects.get(id=pk)
    topSkills = profile.skill_set.exclude(description__exact="")
    otherSkills = profile.skill_set.filter(description="")
    context = {'profile' : profile, 'topSkills' : topSkills, 'otherSkills': otherSkills}
    return render(request, 'profile.html', context)

def loginUser(request):
    page = 'login'
   
    if request.user.is_authenticated:
        return redirect('index')

    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        try:
            user = User.objects.get(username=username)
        except:
            messages.error(request, 'Username does not exist')
        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect('myAccount')
        else:
            messages.error(request, 'Username or password is incorrect')

    context = {'page': page}
    return render(request, 'login-register.html', context)

@login_required(login_url='login')
def logoutUser(request):
    logout(request)
    messages.info(request, 'User has logged out')
    return redirect('login')

def registerUser(request):
    page = 'register'
    form = CustomUserCreationForm()

    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.username = user.username.lower()
            user.save()

            messages.success(request, 'User was created')
            login(request, user)
            return redirect('editAccount')
       
        
    print(form)
    context = {'page' : page, 'form' : form}
    return render(request, 'login-register.html', context)

@login_required(login_url='login')
def myAccount(request):
    profile = request.user.profile
    topSkills = profile.skill_set.all()
    projects = profile.project_set.all()
    context = {'profile': profile, 'topSkills': topSkills, 'projects' : projects}
    return render(request, 'account.html', context)

@login_required(login_url='login')
def editAccount(request):
    profile = request.user.profile
    form = ProfileForm(instance=profile)

    if request.method == 'POST':
       
        form = ProfileForm(request.POST, request.FILES, instance=profile)
        if form.is_valid():
            form.save()
        
            return redirect('myAccount')
    else:
        print(form.errors)
        
    context = {'form' : form}
    return render(request, 'profile_form.html', context)

@login_required(login_url='login')
def addSkill(request):
    profile = request.user.profile
    form = SkillForm()
    if request.method == 'POST':
        form = SkillForm(request.POST, request.FILES)
        if form.is_valid:
            skill = form.save(commit=False)
            skill.owner = profile
            skill.save()

            return redirect('myAccount')
    context = {'form': form, 'profile' : profile}
    return render(request, 'skill-form.html', context)

@login_required(login_url='login')
def updateSkill(request, pk):
    profile = request.user.profile
    skill = profile.skill_set.get(id=pk)
    form = SkillForm(instance=skill)

    if request.method == 'POST':
       
        form = SkillForm(request.POST, request.FILES, instance=skill)
        if form.is_valid():
            form.save()
        
            return redirect('myAccount')
    else:
        print(form.errors)
        
    context = {'form' : form}
    return render(request, 'skill-form.html', context)


@login_required(login_url='login')
def deleteSkill(request, pk):
    profile = request.user.profile
    skill = profile.skill_set.get(id=pk)
    if request.method == 'POST':
        skill.delete()
        return redirect('myAccount')
    
    context = {'skill': skill}
    return render(request, 'delete-form.html', context)

@login_required(login_url='login')
def inbox(request):
    profile = request.user.profile
    messageQuery = profile.messages.all()
    unreadCount = messageQuery.filter(is_read = False).count()
    context = {'messageQuery' : messageQuery, 'unreadCount' : unreadCount}   
    return render(request, 'inbox.html', context)

@login_required(login_url='login')
def sendMessage(request, pk):
    form = MessageForm()
    sender = request.user.profile
    reciever = Profile.objects.get(id=pk)
    if request.method == 'POST':
        form = MessageForm(request.POST, request.FILES)
        if form.is_valid:
            message = form.save(commit=False)
            message.sender = sender
            message.reciever = reciever
            message.save()

    context = {'form' : form}
    return render(request, 'form-template.html', context)

