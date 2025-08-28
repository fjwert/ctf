import requests, json, datetime, re
from bs4 import BeautifulSoup

def get_url (applicationURL):
    URL = applicationURL
    response = requests.get(URL)
    html_data = response.text
    soup = BeautifulSoup(html_data, "html.parser")
    res = soup.find_all(class_=["ramp ref"])
    finalURL = ''
    for element in res:
        finalURL += element['value']
    print(finalURL)


testURL = "https://tns4lpgmziiypnxxzel5ss5nyu0nftol.lambda-url.us-east-1.on.aws/challenge"
get_url(testURL)