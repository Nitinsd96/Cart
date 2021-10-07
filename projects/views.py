from django.shortcuts import render

# Create your views here.
from django.shortcuts import render
import projects
from projects.models import Project

cart_list = []

def project_index(request):
    projects = Project.objects.all()
    context = {
        'projects': projects
    }
    return render(request, 'project_index.html', context)

def project_detail(request, title):

    project = Project.objects.all()
    global cart_list
    print(cart_list)
    cart_list.append(title)
    
    return render(request, 'project_detail.html')


def show_cart(request):
    projects=Project.objects.all()
    projects_dict={}

    global cart_list
    for project in projects:
        
        projects_dict[project.title]=project
    
    cart_projects=[]
    for i, title in enumerate(cart_list):
        cart_projects.append(projects_dict[title])
        

    return render(request, 'show_cart.html', {'cart':cart_projects})

def delete(request, title):
    new_list = []
    global cart_list
    for projects in cart_list:
        if projects!=title:
            new_list.append(projects)
    
    cart_list=new_list

    return render(request, 'show_cart.html')