from flask import render_template, request, redirect, url_for

from application import app, db
from application.series.models import Series
from application.series.forms import SeriesForm
from application.domain.textRenderer import formatName

@app.route('/series', methods=['GET'])
def series_index():
    return render_template('series/list.html', series = Series.query.all())

@app.route('/series/new/')
def series_form():
    return render_template('series/new.html', form = SeriesForm())

@app.route('/series/', methods=['POST'])
def series_create():
    form = SeriesForm(request.form)

    if not form.validate():
        return render_template('series/new.html', form = form)

    seriesName = form.seriesName.data
    eventName = form.eventName.data
    startTime = form.startTime.data
    totalDistance = form.totalDistance.data

    series = Series(seriesName, eventName, startTime, totalDistance)

    db.session().add(series)
    db.session().commit()

    return redirect(url_for('series_index'))
