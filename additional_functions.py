import requests


def getLatestComicNumber():
    current_comic_url = "https://xkcd.com/info.0.json"
    response = requests.get(current_comic_url).json()
    current_comic_num = response['num']
    return current_comic_num

def pullComic(url):
    response =  requests.get(url).json()
    comic_img_url = response['img']
    comic_img_title = response['safe_title']

    comic_file = requests.get(comic_img_url)

    return comic_file,comic_img_title