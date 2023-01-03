import pandas
import requests
from datetime import datetime
import time
import smtplib

MY_LAT = 33.162689
MY_LONG = -96.937622
MY_EMAIL = "Ishmaelsesay2@gmail.com"
MY_PASSWORD = ""


def is_above():

    response = requests.get("http://api.open-notify.org/iss-now.json")
    response.raise_for_status()
    data = response.json()

    iss_latitude = float(data["iss_position"]["latitude"])
    iss_longitude = float(data ["iss_position"]["longitude"])

    if MY_LAT-5 <= iss_latitude <= MY_LAT+5 and MY_LONG-5 <= iss_longitude <= MY_LONG:
        return True


def is_night():

    time_now = datetime.now().hour

    parameters = {
        "lat" : MY_LAT,
        "lng" : MY_LONG,
        "formatted" : 0
    }

    response = requests.get("https://api.sunrise-sunset.org/json", params = parameters)
    response.raise_for_status()
    data = response.json()

    sunrise = int(data["results"]["sunrise"].split("T")[1].split(":")[0])
    sunset = int(data["results"]["sunset"].split("T")[1].split(":")[0])

    if sunset <= time_now <= sunrise:
        return True


while True:
    time.sleep(60)
    if is_night() and is_above():
        connection = smtplib.SMTP("smtp.gmail.com")
        connection.starttls()
        connection.login(MY_EMAIL,MY_PASSWORD)
        connection.send_mail(

            from_addr = MY_EMAIL,
            to_addr = MY_EMAIL,
            msg = "Subject: ISS location notification\n\nLook Up Homie!"

        )










# https://api.sunrise-sunset.org/json
# http://api.open-notify.org/iss-now.json



#response code
#api endpoint url is location
#1 hold on
#2 sduccess here you go
#3 no permission go away
#4 u screwed up
#5 i screwed up (server screwed up)