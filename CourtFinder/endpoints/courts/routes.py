from flask import Blueprint, render_template
from CourtFinder.models.courts import Court

courts = Blueprint('courts', __name__)


@courts.route('/courts')
def list_courts():
    court = Court.query.all()
    return render_template('courts/courts.html', Courts=court)


@courts.route('/map')
def map():
    return render_template('courts/map.html')


@courts.route('/courts/create')
def create_court():
    return render_template('/')


@courts.route('/courts/auth/login')
def create_court():
    return render_template('/')
