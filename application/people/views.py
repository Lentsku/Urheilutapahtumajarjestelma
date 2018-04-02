from flask import redirect, render_template, request, url_for

from application import app, db
from application.people.models import Person
from application.personSeries.models import PersonSeries
from application.series.models import Series

from application.people.forms import PersonForm, SearchForm, SelectOptionsForm
from application.series.forms import SelectSeriesForm
from application.domain.textRenderer import formatName

from flask_login import login_required

seriesIdGlobal = -1
selectedOptionGlobal = 'add'

@app.route('/people', methods=['GET'])
def person_index():
    selectSeriesForm = SelectSeriesForm(request.form, seriesSelector=seriesIdGlobal)
    selectOptionsForm = SelectOptionsForm(request.form, optionsSelector=selectedOptionGlobal)
    return render_template('people/list.html', selectSeriesForm = selectSeriesForm,
                            selectOptionsForm = selectOptionsForm,
                            searchForm = SearchForm(request.form),
                            people = Person.query.all())

@app.route('/people/new/')
def person_form():
    return render_template('people/new.html', form = PersonForm())

@app.route('/people/update/', methods=['POST'])
def person_update():
    personId = request.form['person_id']
    person = Person.query.filter_by(id = personId).first()
    personSeriesList = PersonSeries.query.filter_by(person_id = personId).all()
    seriesList = []

    for personSeries in personSeriesList:
        seriesId = personSeries.series_id
        series = Series.query.filter_by(id = seriesId).first()
        seriesList.append(series)

    personForm = PersonForm(firstname=person.firstname)

    return render_template('people/update.html', person = person, personSeries = personSeries,
                            series = seriesList, form = personForm)

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
    searchForm = SearchForm(request.form)

    if not searchForm.validate():
        return render_template('people/list.html', form = searchForm)

    formParam = searchForm.lastFirstSearch.data
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

    return render_template('people/list.html', selectSeriesForm = SelectSeriesForm(request.form, seriesSelector=seriesIdGlobal),
                            selectOptionsForm = SelectOptionsForm(request.form, optionsSelector=selectedOptionGlobal),
                            searchForm = searchForm, people = people)

@app.route('/people/add/person/', methods = ['POST'])
def add_person():
    seriesId = seriesIdGlobal
    personId = request.form['person_id']

    if not seriesId == -1:
        personSeries = PersonSeries(1)
        personSeries.series_id = seriesId
        personSeries.person_id = personId
        db.session().add(personSeries)
        db.session().commit()

    return redirect(url_for('person_index'))

@app.route('/people/select/option/', methods = ['POST'])
def select_option():
    # TODO make the SelectField store the selected value upon selection without clicking a submit-button
    selectOptionsForm = SelectOptionsForm(request.form)

    global selectedOptionGlobal
    selectedOptionGlobal = selectOptionsForm.optionsSelector.data

    return redirect(url_for('person_index'))

@app.route('/people/add/series/', methods = ['POST'])
def add_series():
    # TODO make the SelectField store the selected value upon selection without clicking a submit-button
    selectSeriesForm = SelectSeriesForm(request.form)

    global seriesIdGlobal
    seriesIdGlobal = selectSeriesForm.seriesSelector.data

    return redirect(url_for('person_index'))
