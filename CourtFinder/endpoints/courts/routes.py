from flask import Blueprint, render_template
from CourtFinder.models.courts import Court

courts = Blueprint('courts', __name__)


@courts.route('/courts')
def list_courts():
    court = Court.query.all()
    return render_template('courts/courts.html', Courts=court)

@courts.route('/courts/<int:court_id>/delete', methods=['GET', 'DELETE'])
def remove_court(court_id):
  court = Court.query.get_or_404(court_id)
  Court.query.delete(court)
  court = Court.query.all
  return render_template('courts/courts.html', Courts=court)

@courts.route('/map')
def map():
    return render_template('courts/map.html')

