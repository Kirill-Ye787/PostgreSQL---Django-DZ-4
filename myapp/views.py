from django.shortcuts import render
from .models import Company, Person

def company_list(request):
    companies = Company.objects.all()
    return render(request, "companies.html", {"companies": companies})

def person_list(request):
    people = Person.objects.all()
    return render(request, "people.html", {"people": people})
