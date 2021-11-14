from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.models import Group
from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views.generic import DeleteView, UpdateView
from django.views import View
from main.models import Person
from django.conf import settings
from main.forms import PersonForm
import random

# Manage Members In A Group
class PersonListView(View):
    template_name = 'main/people_list.html'
    def get(self,request):
         if request.user.is_authenticated:
             members = Person.objects.filter(group=request.user)
             personForm =  PersonForm()
             ctx = {'person_list':members, 'person_form': personForm}
             return render(request,self.template_name,ctx)
         else:
            return redirect('%s?next=%s' % (settings.LOGIN_URL,request.path))

# POST for adding members
class PersonCreateView(View, LoginRequiredMixin):
    def post(self, request):
       form = PersonForm(request.POST)
       if form.is_valid():
           person = form.save(commit=False)
           person.group = request.user
           person.save()
           return redirect(reverse_lazy('main:list'))
       ctx = {'form':form}
       return render(request,'main/register.html',ctx)

# Update Member
class PersonUpdateView(UpdateView, LoginRequiredMixin):
    model = Person
    template_name = 'main/person_update.html'
    fields= ['name']
    success_url = reverse_lazy('main:list')

# Delete Member
class PersonDeleteView(DeleteView, LoginRequiredMixin):
    model = Person
    template_name = 'main/person_delete.html'
    success_url = reverse_lazy('main:list')

    def get_queryset(self):
        print('delete get_queryset called')
        qs = super(PersonDeleteView, self).get_queryset()
        return qs.filter(group=self.request.user)


class PersonChooseView(View):
    def get(self, request):
        if request.user.is_authenticated:
            people = Person.objects.filter(group=request.user, hasBeenAssigned=False )
            return render(request, 'main/person_choose.html', {'people':people})
        else:
            return redirect('%s?next=%s' % (settings.LOGIN_URL,request.path))

    def post(self, request):
        currentPerson = Person.objects.filter(id=request.POST['person'])
        #add error safety for the line if chosenPerson deosnt exist
        secretSanta = generateSecretSanta(currentPerson, request.user)
       


def generateSecretSanta(currentPerson,group):
     if(currentPerson.has_voted):
        message="You Have Already Been Assigned A Secret Santa"
     else:
        people =  Person.objects.filter(group=group, hasBeenAssigned=False)
     if len(people)>2 :
         num = random.randrange(0, len(people)-1)
         person = people[num]

