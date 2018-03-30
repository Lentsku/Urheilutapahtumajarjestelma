from flask import redirect, render_template, request, url_for

from application import app, db
from application.people.models import Person
from application.people.forms import PersonForm

from flask_login import login_required

@app.route('/people', methods=['GET'])
def person_index():
    return render_template('people/list.html', people = Person.query.all())

@app.route('/people/new/')
def person_form():
    return render_template('people/new.html', form = PersonForm())

@app.route('/people/', methods=['POST'])
def person_create():
    form = PersonForm(request.form)

    if not form.validate():
        return render_template('people/new.html', form = form)

    firstname = form.firstname.data
    lastname = form.lastname.data
    lastFirst = lastname[:3] + firstname[:2]
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
