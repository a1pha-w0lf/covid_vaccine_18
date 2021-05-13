
import requests
from datetime import date 
import json
import time
from mail import *
today = date.today()


def jprint(obj):
    # create a formatted string of the Python JSON object
    text = json.dumps(obj, sort_keys=True, indent=4)
    print(text)

def check_availalibity_18(district_id):

    parameters = {"district_id" : district_id,
                    "date" : today.strftime("%d-%m-%y")
    }
    headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/56.0.2924.76 Safari/537.36'}
    response = requests.get("https://cdn-api.co-vin.in/api/v2/appointment/sessions/public/calendarByDistrict", headers = headers, params = parameters)

    content = response.json()

    #jprint(content)
    for i in range (len(content["centers"])):
        for j in range(len(content["centers"][i]["sessions"])):
            if content["centers"][i]["sessions"][j]["min_age_limit"] == 45 and content["centers"][i]["sessions"][j]["available_capacity"] != 0:
                return {"Name":content["centers"][i]["name"], "Address": content["centers"][i]["address"], "Available Capacity": content["centers"][i]["sessions"][j]["available_capacity"] }



while True:
    if check_availalibity_18(571) != None:
        send_mail()
    time.sleep(300)
