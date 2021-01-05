import requests
from bs4 import BeautifulSoup

URL = "https://careers.kakao.com/jobs?employeeType=Full%20Time&keyword=&page=1"


#마지막 페이지를 알아내는 함수
def get_last_page() :
    result = requests.get(URL)
    soup = BeautifulSoup(result.text, 'html.parser')
    links = soup.find_all("a", {"class" : {"change_page link_page"}}) 
    pages = []

    for link in links :
        pages.append(int(link.string))

    max_page = pages[-1]
    return max_page

#현재 페이지의 채용정보의 링크와 제목을 읽어내는 함수
def get_job() :
    result = requests.get(URL)
    soup = BeautifulSoup(result.text, 'html.parser')
    jobs = soup.find("ul", {"class" : "list_jobs"}).find_all("li")

    for job in jobs :
        link_title = job.find("a", {"class" : "link_jobs"})
        print( link_title )

get_job()