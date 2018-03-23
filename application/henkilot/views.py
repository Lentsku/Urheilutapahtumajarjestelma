from application import app, db
from flask import redirect, render_template, request, url_for
from application.henkilot.models import Henkilo

@app.route('/henkilot', methods=['GET'])
def tasks_index():
    return render_template('henkilo/list.html', henkilot = Task.query.all())

@app.route('/henkilot/new/')
def tasks_form():
    return render_template('henkilot/new.html')

@app.route('/tasks/', methods=['POST'])
def tasks_create():
    h = Henkilo(request.form.get('etunimi', 'sukunimi', 'sukuEtu', 'osoite', postinumero, 'postitoimipaikka', 'maa', 'sahkoposti', 'puhelin'))

    db.session().add(h)
    db.session().commit()

    return redirect(url_for('henkilot_index'))
