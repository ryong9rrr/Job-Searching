import requests
from bs4 import BeautifulSoup

URL = "https://careers.kakao.com/jobs?employeeType=Full%20Time&keyword=&"


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
def extract_jobs(last_page) :
  jobs = []
  for page in range(last_page) :
    print(f"KAKAO page {page+1}")
    result = requests.get(f"{URL}page={page+1}")
    soup = BeautifulSoup(result.text, 'html.parser')
    print(soup.title)


def get_job():
    last_page = get_last_page()
    extract_jobs(last_page)

get_job()
