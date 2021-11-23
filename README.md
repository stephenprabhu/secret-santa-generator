A Django application that will store secret santa group members and randomly assign each member to any other member in the group.

<h5>Libraries Used:</h5>
<strong>python-decouple</strong> - For Using .env files

<h5>External Services Used:</h5>
<strong>SendGrid</strong> - for sending emails to group members

<h5>Goals:</h5>
* Make The Interface Easy To Use
* Overcome the issue of any member in the group getting assigned thier own name or getting left behind
* Make the process of creating a group and assigning secret santas a quick process

<h5>Installation Instructions: </h5>
1. Install pip
2. Clone The Project
3. Run <pre>pip install django</pre>
4. Run <pre>pip install python-decouple</pre>
5. Run <pre>python manage.py migrate</pre>
6. Run <pre>python manage.py runserver</pre>
