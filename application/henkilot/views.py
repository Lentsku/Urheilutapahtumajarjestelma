from flask import redirect, render_template, request, url_for

from application import app, db
from application.henkilot.models import Henkilo
from application.henkilot.forms import EtunimiForm

@app.route('/henkilot', methods=['GET'])
def henkilot_index():
    return render_template('henkilot/list.html', henkilot = Henkilo.query.all())

@app.route('/henkilot/new/')
def henkilot_form():
    return render_template('henkilot/new.html', form = EtunimiForm())

@app.route('/henkilot/', methods=['POST'])
def henkilot_create():
    etunimi = request.form.get('etunimi')
    sukunimi = request.form.get('sukunimi')
    sukuEtu = request.form.get('sukuEtu')
    osoite = request.form.get('osoite')
    postinumero = request.form.get('postinumero')
    postitoimipaikka = request.form.get('postitoimipaikka')
    maa = request.form.get('maa')
    sahkoposti = request.form.get('sahkoposti')
    puhelin = request.form.get('puhelin')

    henkilo = Henkilo(etunimi, sukunimi, sukuEtu, osoite, postinumero, postitoimipaikka, maa, sahkoposti, puhelin)

    db.session().add(henkilo)
    db.session().commit()

    return redirect(url_for('henkilot_index'))
