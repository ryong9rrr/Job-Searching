import requests
from bs4 import BeautifulSoup

URL = "https://careers.kakao.com/jobs?employeeType=Intern&keyword=&page=1"

result = requests.get(URL)
soup = BeautifulSoup(result.text, 'html.parser')

is_not = soup.find("div", {"class" : "wrap_nodata job_nodata"})

if is_not is None :
    print(f"공고확인 : {URL}")
else :
    print(is_not.text)