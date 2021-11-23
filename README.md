A Django application that will store secret santa group members and randomly assign each member to any other member in the group.

<h6>Libraries Used:</h6>
* <strong>python-decouple</strong> - For Using .env files

<h6>External Services Used:</h6>
<strong>SendGrid</strong> - for sending emails to group members

<h6>Goals:</h6>
* Make The Interface Easy To Use
* Overcome the issue of any member in the group getting assigned thier own name or getting left behind
* Make the process of creating a group and assigning secret santas a quick process

<h6>Installation Instructions: </h6>
1. Install pip
2. Clone The Project
3. Run <pre>pip install django</pre>
4. Run <pre>pip install python-decouple</pre>
5. Run <pre>python manage.py migrate</pre>
6. Run <pre>python manage.py runserver</pre>
