import requests
from bs4 import BeautifulSoup

def get_kakao_intern() :
    URL = "https://careers.kakao.com/jobs?employeeType=Intern&keyword=&page=1"

    result = requests.get(URL)
    soup = BeautifulSoup(result.text, 'html.parser')

    is_not = soup.find("div", {"class" : "wrap_nodata job_nodata"})

    print(is_not.text)

    if is_not is None :
        return {
            "공고확인" : URL
        } 
    else :
        return {
            is_not.text #진행중인 공고가 없습니다.
        } 