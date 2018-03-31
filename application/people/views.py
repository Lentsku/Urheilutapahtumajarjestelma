from flask import redirect, render_template, request, url_for

from application import app, db
from application.people.models import Person
from application.people.forms import PersonForm, SearchForm

from flask_login import login_required

@app.route('/people', methods=['GET'])
def person_index():
    return render_template('people/list.html', form = SearchForm(), people = Person.query.all())

@app.route('/people/new/')
@login_required
def person_form():
    return render_template('people/new.html', form = PersonForm())

@app.route('/people/', methods=['POST'])
@login_required
def person_create():
    form = PersonForm(request.form)

    if not form.validate():
        return render_template('people/new.html', form = form)

    firstname = form.firstname.data
    lastname = form.lastname.data
    lastFirst = formatLastFirst(lastname[:3] + firstname[:2])
    birthdate = form.birthdate.data
    email = form.email.data
    phone = form.phone.data
    address = form.address.data
    postalCode = form.postalCode.data
    postOffice = form.postOffice.data
    country = form.country.data

    person = Person(firstname, lastname, lastFirst, birthdate, email, phone, address, postalCode, postOffice, country)

    db.session().add(person)
    db.session().commit()

    return redirect(url_for('person_index'))

@app.route('/people/search/', methods = ['GET', 'POST'])
def person_search():
    form = SearchForm(request.form)

    if not form.validate():
        return render_template('people/list.html', form = form)

    if form.validate_on_submit():
        lastFirst = formatLastFirst(form.lastFirst.data)
        people = Person.query.filter(Person.lastFirst == lastFirst)

    people = people.order_by(Person.lastname).all()

    return render_template('people/list.html', form = form, people = people)

def formatLastFirst(param):
    lastFirst = param
    firstUp = lastFirst[:1].upper()
    secondDown = lastFirst[1:3].lower()
    thirdUp = lastFirst[3:4].upper()
    fourthDown = lastFirst[4:5].lower()
    lastFirst = firstUp + secondDown + thirdUp + fourthDown

    return lastFirst
