#Student Club Member Checker
from pyscript import display, document


def student_club(e):
    document.getElementById('result').innerHTML = ' '
    firstname = document.getElementById('first_name').value
    lastname = document.getElementById('last_name').value
    studentname = firstname + ' ' + lastname
    full_names = ['Elianna Co', 'Rhys Lozano', 'Savannah Sunga', 'Zoe Reyes', 'Bonnie Nubla', 'Alexa Agnote', 'Gisella Liwag']
    member_checker = studentname in full_names

    display_message = (f'Sorry, you did not pass', f'Congratulations {firstname} {lastname}, you are now part of the Netflix Lovers.')

    document.getElementById('results').innerHTML = (display_message[member_checker])