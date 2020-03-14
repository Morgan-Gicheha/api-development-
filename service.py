from app import db
import requests
from models.alpha import Forex

def alpha_vantage_request():
    r = requests.get()



def alpha_vantage_save(to,from_,high,low,close,date_):
    ''' call this fuction to save auto_save dta to Forex table'''
    data_from_api=Forex(to=to,from_=from_ high=high, low=low,close=close, datetime=date_)
    print("recieved")
    db.session.add(data_from_api)
    print("here")
    db.session.commit()
    print("sent")

alpha_vantage_save(to="KES",from_="USD", high=158.9500, low=158.9500,close=158.9500, date_="2020-03-13 16:00:00")


