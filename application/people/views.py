from flask import redirect, render_template, request, url_for

from application import app, db
from application.people.models import Person
from application.people.forms import PersonForm, SearchForm
from application.domain.textRenderer import formatName

from flask_login import login_required

@app.route('/people', methods=['GET'])
def person_index():
    return render_template('people/list.html', form = SearchForm(), people = Person.query.all())

@app.route('/people/new/')
def person_form():
    return render_template('people/new.html', form = PersonForm())

@app.route('/people/', methods=['POST'])
def person_create():
    form = PersonForm(request.form)

    if not form.validate():
        return render_template('people/new.html', form = form)

    firstname = formatName(form.firstname.data)
    lastname = formatName(form.lastname.data)
    birthdate = form.birthdate.data
    email = form.email.data
    phone = form.phone.data
    address = formatName(form.address.data)
    postalCode = form.postalCode.data
    postOffice = formatName(form.postOffice.data)
    country = formatName(form.country.data)

    person = Person(firstname, lastname, birthdate, email, phone, address, postalCode, postOffice, country)

    db.session().add(person)
    db.session().commit()

    return redirect(url_for('person_index'))

@app.route('/people/search/', methods = ['POST'])
def person_search():

    form = SearchForm(request.form)

    if not form.validate():
        return render_template('people/list.html', form = form)

    formParam = form.lastFirstSearch.data
    lastFirstSplit = ''
    if '.' in formParam:
        lastFirstSplit = formParam.split('.')
    else:
        lastFirstSplit = formParam.split(' ') # Critical to specify .split(' ')

    lastname = formatName(lastFirstSplit[0])
    people = ''
    if len(lastFirstSplit) == 1:
        people = Person.query.filter(Person.lastname.like(lastname + '%'))
    elif lastname == '':
        firstname = formatName(lastFirstSplit[1])
        people = Person.query.filter(Person.firstname.like(firstname + '%'))
    else:
        firstname = formatName(lastFirstSplit[1])
        people = Person.query.filter(Person.lastname.like(lastname + '%')) \
                             .filter(Person.firstname.like(firstname + '%'))

    people = people.order_by(Person.lastname).all()

    return render_template('people/list.html', form = form, people = people)
