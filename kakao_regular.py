import requests
from bs4 import BeautifulSoup

#카카오 신입개발자 공채
def get_kakao_regular() :

    URL = "https://careers.kakao.com/2021-developer"

    result = requests.get(URL)
    soup = BeautifulSoup(result.text, 'html.parser')

    title = soup.title.string
    schedule = soup.find("div", {"class" : "group_blind"}).find("span").string
    certificates_data = soup.find_all("div", {"class" : "group_blind"})[2].find("ul", {"class" : "list_info"}).find_all("li")

    certificates = []

    for certificate in certificates_data :
        certificates.append(certificate.string)

    return {
        "title" : title, #신입 개발자 공채
        "schedule" : schedule, #2020.08.24 (월) ~ 09.07 (월) 19:00
        "certificates" : certificates
    }