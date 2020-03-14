from app import db
from models.alpha import Forex

def auto_save(to_from,high,low,close,date_):
    ''' call this fuction to save auto_save dta to Forex table'''
    data_from_api=Forex(to_from=to_from, high=high, low=low,close=close, datetime=date_)
    print("recieved")
    db.session.add(data_from_api)
    print("here")
    db.session.commit()
    print("sent")

auto_save(to_from="USD-KES", high=158.9500, low=158.9500,close=158.9500, date_="2020-03-13 16:00:00")
