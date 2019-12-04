import requests 
import datetime as dt
from bs4 import BeautifulSoup
from time import sleep



URL = "https://traffic.api.here.com/traffic/6.2/flow.xml?app_id=bvspMBY693uKD4E5Iesm&app_code=QYe9Ffu-JEeIEpZNRqgtJw&bbox=42.357609,%20-71.079125;42.351007,%20-71.064951&responseattributes=sh,fc"
new_hour = 20;
i = 15

while True:
    if (dt.datetime.now().hour == new_hour):
        response = requests.get(url = URL)
        name = str(dt.datetime.now().hour) + "-" + str(i) +  ".xml"
        file = open(name, "w")
        bs = BeautifulSoup(response.content, 'xml')
        file.write(bs.prettify())
        file.close
        i += 1
        new_hour += 1
    else:
        sleep(60*30)


