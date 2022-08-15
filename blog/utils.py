import requests
from bs4 import BeautifulSoup


def scrap_elementor_site(url):
    headers = {"user_agent":"Mozilla/5.0 (platform; rv:geckoversion) Gecko/geckotrail Firefox/firefoxversion"}

    response = requests.get(url,headers=headers)
    soup = BeautifulSoup(response.content)
    blogs = list()
    articles = soup.find_all('section',class_='elementor-section')
    for article in articles:
        blog = {}

        title = article.find('h3',class_='elementor-heading-title elementor-size-default')
        if title:
            try:
                num,set_title = title.text.split('.')
                image = article.find('div',class_='elementor-image')
                if image:
                    set_image = image.find('img')['src']
                description = article.find('div',class_='elementor-text-editor elementor-clearfix').find(
                    'p'
                )
                if description:
                    set_description = description.text
                    blog['title'] = set_title
                    blog['description'] = set_description
                    blog['image'] = set_image
                    blogs.append(blog)
            except:
                pass

    return blogs
            

def scrapping_wpbeginner(url):

    headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/50.0.2661.102 Safari/537.36'}
    response = requests.get(url,headers=headers)
    print(response.status_code)
    soup = BeautifulSoup(response.content,features="html.parser")
    blogs = list()
    articles = soup.find_all('h4')
    for article in articles:
        blog = {}
        title = article.find('a')
        if title :
            try:
                num,set_title = title.text.split('.')
                image  = title.findNext('p')
                if image:
                    if image.findNext('a'):
                        image  = image.findNext('a').find('img')
                        if image:
                            set_image  =image['data-lazy-srcset']
                            description = image.findNext('p').text
                            blog['title'] = set_title
                            blog['description'] = description
                            blog['image'] = set_image
                            blogs.append(blog)

            except:
                pass

    return blogs



def scrapping_makeuseof(url):
    headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/50.0.2661.102 Safari/537.36'}
    response = requests.get(url,headers=headers)
    print("status code ",response.status_code)
    blogs = list()
    soup = BeautifulSoup(response.content,features="html.parser")
    articles_even  = soup.find_all('div',class_='ad-even')
    articles_odd  = soup.find_all('div',class_='ad-odd')
    articles_even.extend(articles_odd)
    for article in articles_even[:-1]:
        blog = {}
        title = article.findNext('h2').text
        nums,last_title = title.split('.')
        count_details = article.findNext('p')
        if count_details:
            first_descp = count_details.findNext('p')
            secound_descp = first_descp.findNext('p')
            description = first_descp.text + secound_descp.text
            blog['title'] = last_title
            blog['description'] = description
            blogs.append(blog)


    return blogs



