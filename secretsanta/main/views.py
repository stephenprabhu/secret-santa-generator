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
from django.core.mail import send_mail


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
    fields= ['name','email']
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
            people = Person.objects.filter(group=request.user )
            return render(request, 'main/person_choose.html', {'people':people})
        else:
            return redirect('%s?next=%s' % (settings.LOGIN_URL,request.path))

    def post(self, request):
        currentPerson = Person.objects.filter(id=request.POST['person'])
        #add error safety for the line if chosenPerson deosnt exist
        secretSanta = generateSecretSanta(currentPerson[0], request.user)
        ctx = {'person':secretSanta}
        return render(request, 'main/person_reveal.html', ctx)
       

       


def generateSecretSanta(currentPerson,group):
     if(currentPerson.hasVoted):
        return 0
     else:
        people =  Person.objects.filter(group=group, hasBeenAssigned=False).exclude(id=currentPerson.id)
     if len(people)>2 :
         num = random.randrange(0, len(people)-1)
         chosenPerson = people[num]
     elif len(people)==2 :
         chosenPerson = people.filter(hasVoted=False)[0]
     elif len(people)==1:
         chosenPerson = people[0]
     else:
         return None
     currentPerson.hasVoted = True
     currentPerson.save()
     chosenPerson.hasBeenAssigned=True
     chosenPerson.save()
     sendMail(chosenPerson,currentPerson)
     return chosenPerson


def sendMail(chosenPerson,currentPerson):
    if(chosenPerson==0 or chosenPerson==None):
        return
    else:
        message = "Your secret santa is " + chosenPerson.name    
        send_mail('About Your Secret Santa', message, 'contact@stephenprabhu.com', [currentPerson.email], fail_silently=False)

     

