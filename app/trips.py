from datetime import date
from app import db


def delete_old(trips):
    today = str(date.today())

    for trip in trips:
        this_date = trip.date
        if this_date < today:
            db.session.delete(trip)
            db.session.commit()
            trips.remove(trip)
