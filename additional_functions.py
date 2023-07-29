import requests
import os

def getLatestComicNumber():
    """gets the latest comic's number"""

    #get the current url of the curr comic response
    current_comic_url = "https://xkcd.com/info.0.json"
    #requests the url 
    response = requests.get(current_comic_url).json()
    #parse the number
    current_comic_num = response['num']
    
    return current_comic_num

def pullComic(number = 1):
    """pulls the comic of the number passed, saves it as the file.
       
       number defaults to 1

       returns the title of the comic back
    """
    url = 'https://xkcd.com/' + str(number) + '/info.0.json'

    #sends a req to get the data of the specific comic
    response =  requests.get(url).json()

    #parse the img link and title
    comic_img_url = response['img']
    comic_img_title = response['safe_title']

    #requests the url to get the contents of the comic .png file
    comic_file = requests.get(comic_img_url)
     #returns the comic content and its title

    
    if not os.path.exists("./XKCD"):
        os.makedirs("./XKCD")
    path = "./XKCD/XKCD.jpg"
        
    with open(path,'wb') as image:
        image.write(comic_file.content)

    return comic_img_title