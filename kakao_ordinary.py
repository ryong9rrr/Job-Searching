import requests
from bs4 import BeautifulSoup

URL = "https://careers.kakao.com/jobs?employeeType=Full%20Time&keyword=&"
extracted_links = []


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

#모든 페이지의 채용정보의 링크를 읽어내는 함수
def extract_jobs(last_page) :
    for page in range(last_page) :
        #print(f"KAKAO page {page+1}")
        result = requests.get(f"{URL}page={page+1}")
        soup = BeautifulSoup(result.text, 'html.parser')
        results = soup.find_all("a", {"class" : "link_jobs"})

        for result in results :
            link = result.get('href')
            extracted_links.append(link)
    

def detail_job() :
    extracted_jobs = []
    
    for link in extracted_links :
        extracted_job = []

        result = requests.get( f"https://careers.kakao.com{link}" )
        soup = BeautifulSoup(result.text, 'html.parser')

        title = soup.title.string
        extracted_job.append(title)

        contents = soup.find_all("p", {"class" : "txt_cont"})
        for content in contents[0:-1] :
            cont_desc = content.get_text().strip()
            extracted_job.append(cont_desc)

        extracted_jobs.append(extracted_job)

    return extracted_jobs


def get_job():
    last_page = get_last_page()
    extract_jobs(last_page)
    detail_job()
    
get_job()
