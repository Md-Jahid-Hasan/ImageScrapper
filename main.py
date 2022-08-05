from ImageScrap import ScrapImageURL
from urllib.parse import urlparse


def print_hi(name):
    url = input("Please enter a valid url : ")
    tags = [tag for tag in input("please enter space separated tags: ").split()]
    web_page = ScrapImageURL(url, tags)
    urls = web_page.retrieve_webpage()
    print(urls)

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print_hi('PyCharm')

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
