from bs4 import BeautifulSoup
from urllib.parse import urlparse
import requests


class ScrapImageURL:
    def __init__(self, url, search_tags):
        self.__url = url
        self.__search_tags = search_tags
        self.__base = urlparse(url).hostname
        self.__scheme = urlparse(url).scheme + "://"

    def retrieve_webpage(self):
        html_text = requests.get(self.__url)
        if html_text.status_code == 404:
            print("Page Not Found!!")
            return False
        return self.get_image_url(html_text)

    def get_image_url(self, html_text):
        soup = BeautifulSoup(html_text.text, 'html.parser')
        all_image = soup.find_all('img')
        image_urls = []
        for image in all_image:
            img_url = image.attrs.get('src', False)
            image_tag = image.attrs.get('alt', False)
            if img_url and (image_tag in self.__search_tags):
                image_urls.append(self.__scheme + self.__base + img_url)

        return image_urls
