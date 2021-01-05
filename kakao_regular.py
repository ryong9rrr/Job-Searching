import requests
from bs4 import BeautifulSoup

#카카오 신입개발자 공채
URL = "https://careers.kakao.com/2021-developer"

result = requests.get(URL)
soup = BeautifulSoup(result.text, 'html.parser')

title = soup.title.string
schedule = soup.find("div", {"class" : "group_blind"}).find("span").string
certificates = soup.find_all("div", {"class" : "group_blind"})[2].find("ul", {"class" : "list_info"}).find_all("li")


print(title) #신입 개발자 공채
print(schedule) #2020.08.24 (월) ~ 09.07 (월) 19:00
for certificate in certificates :
    print(certificate.string)