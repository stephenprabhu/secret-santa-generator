A Django application that will store secret santa group members and randomly assign each member to any other member in the group.

<h3><a href="http://steverogers133.pythonanywhere.com/">Final Result</a></h3>

<h5>Libraries Used:</h5>
<strong>python-decouple</strong> - For Using .env files

<h5>External Services Used:</h5>
<strong>SendGrid</strong> - for sending emails to group members

<h5>Goals:</h5>
<ul>
  <li>Make The Interface Easy To Use</li>
  <li>Overcome the issue of any member in the group getting assigned thier own name or getting left behind</li>
  <li>Make the process of creating a group and assigning secret santas quick</li>
  <li>Send emails to Each member in the group quickly and prevent the email from getting into the spam folder</li>
</ul>

<h5>Installation Instructions: </h5>
1. Install pip<br>
2. Clone The Project<br>
3. Run <pre>pip install django</pre>
4. Run <pre>pip install python-decouple</pre>
5. Run <pre>python manage.py migrate</pre>
6. Run <pre>python manage.py runserver</pre>
