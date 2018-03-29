from flask import redirect, render_template, request, url_for

from application import app, db
from application.henkilot.models import Henkilo
from application.henkilot.forms import HenkiloForm

@app.route('/henkilot', methods=['GET'])
def henkilot_index():
    return render_template('henkilot/list.html', henkilot = Henkilo.query.all())

@app.route('/henkilot/new/')
def henkilot_form():
    return render_template('henkilot/new.html', form = HenkiloForm())

@app.route('/henkilot/', methods=['POST'])
def henkilot_create():
    form = HenkiloForm(request.form)

    etunimi = form.etunimi.data
    sukunimi = form.sukunimi.data
    sukuEtu = form.sukuEtu.data
    sahkoposti = form.sahkoposti.data
    puhelin = form.puhelin.data
    osoite = form.osoite.data
    postinumero = form.postinumero.data
    postitoimipaikka = form.postitoimipaikka.data
    maa = form.maa.data

    henkilo = Henkilo(etunimi, sukunimi, sukuEtu, sahkoposti, puhelin, osoite, postinumero, postitoimipaikka, maa)

    db.session().add(henkilo)
    db.session().commit()

    return redirect(url_for('henkilot_index'))
