from django.shortcuts import render

# to send response bank to the template
from django.http import HttpResponse

# for template operations
from django.template import loader

# to import the database model and opertate with data
from .models import Member

def members(request):
    
    # to return and load the template
    #template = loader.get_template('myfirst.html') 
    #return HttpResponse(template.render())

    mymembers = Member.objects.all().values()
    template = loader.get_template('all_members.html')
    context = {
        'mymembers' : mymembers,
    }
    return HttpResponse(template.render(context, request))

# to print detail on each member by matching their id
def details(request, id):
    mymember = Member.objects.get(id=id)
    template = loader.get_template('details.html')
    context = {
        'mymember' : mymember,
    }
    return HttpResponse(template.render(context, request))


def main(request):
    template = loader.get_template('main.html')
    return HttpResponse(template.render())


def testing(request):
    template = loader.get_template('template.html')
    context = {
        'tests' : ['test1', 'test2', 'test3']
    }
    return HttpResponse(template.render(context, request)) 