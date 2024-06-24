from django.shortcuts import render,redirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .models import *
from .forms import *


def homePage(request):
    return render(request, 'index.html')


def projects(request):
    searchQuery = ''
    if request.GET.get('search_query'):
        searchQuery = request.GET.get('search_query')

    projectsQuery = Project.objects.filter(title__icontains = searchQuery)
    context = {'projects': projectsQuery, 'search_query' : searchQuery}
    return render(request, 'projects.html',context)


def singleProject(request,pk):
    projectObj = Project.objects.get(id=pk)
    form = ReviewForm()
    
    if request.method == 'POST':
        form = ReviewForm(request.POST)
        review = form.save(commit=False)
        review.project = projectObj
        review.owner = request.user.profile
        review.save()

        projectObj.getVoteCount

        messages.success(request, "Review has submited.")
        return redirect('single-project', pk = projectObj.id)

    context = {'project': projectObj, 'form' : form}
    return render(request, 'single-project.html', context)

@login_required(login_url='login')
def createProject(request):
    profile = request.user.profile
    form = ProjectForm()
    if request.method == 'POST':
        form = ProjectForm(request.POST, request.FILES)
        if form.is_valid:
            project = form.save(commit=False)
            project.owner = profile
            project.save()
            return redirect('myAccount')
    context = {'form': form, 'profile' : profile}
    return render(request, 'form-template.html', context)

@login_required(login_url='login')
def updateProject(request, pk):
    profile = request.user.profile
    project = profile.project_set.get(id=pk)
    form = ProjectForm(instance=project)

    if request.method == 'POST':
        newtags = request.POST.get('newtags').replace(',',  " ").split()

        form = ProjectForm(request.POST, request.FILES, instance=project)
        if form.is_valid():
            project = form.save()
            for tag in newtags:
                tag, created = Tag.objects.get_or_create(name=tag)
                project.tags.add(tag)

            return redirect('myAccount')

    context = {'form': form, 'project': project}
    return render(request, "update-project-form.html", context)

@login_required(login_url='login')
def deleteProject(request, pk):
    profile = request.user.profile
    project = profile.project_set.get(id=pk)
    if request.method == 'POST':
        project.delete()
        return redirect('myAccount')
    context = {'project': project}
    return render(request, 'delete-form.html', context)
