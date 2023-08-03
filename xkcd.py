import requests
import os

class XKCD:
    def __init__(self):
        
        self.current_comic_url = ""
        self.message_author = ""
        self.current_comic_title = ""
        self.path = ""
        self.comic_img_url = ""

        self.current_comic_num = 0
        self.message_id = 0
        self.day = 0
        self.month = 0
        self.year = 0


    def getLatestComicNumber(self):
        """gets the latest comic's number"""

        #get the current url of the curr comic response
        self.current_comic_url = "https://xkcd.com/info.0.json"
        #requests the url 
        response = requests.get(self.current_comic_url).json()
        #parse the number
        self.setComicNumber(response)
        return self.current_comic_num
     
    
    def pullComic(self,number = 1):
        """pulls the comic of the number passed, saves it as the file.
       
       number defaults to 1
        """
        url = 'https://xkcd.com/' + str(number) + '/info.0.json'

        #sends a req to get the data of the specific comic
        response =  requests.get(url).json()

        #parse the img link and title
        self.setImageURL(response)
        self.setComicTitle(response)
        self.setComicNumber(response)
        self.setComicDate(response)

        #requests the url to get the contents of the comic .png file
        comic_file = requests.get(self.comic_img_url)
        
        if not os.path.exists("./XKCD"):
            os.makedirs("./XKCD")
        self.path = "./XKCD/XKCD.jpg"
            
        with open(self.path,'wb') as image:
            image.write(comic_file.content)

    

    def setMessageAuthor(self, author):
        self.message_author = author
    def getMessageAuthor(self):
        return self.message_author
    
    

    def setMessageID(self, message_id):
        self.message_id = message_id
    def getMessageID(self):
        return self.message_id
    


    def setComicTitle(self,resp):
        self.current_comic_title = resp['safe_title']
    def getComicTitle(self):
        return self.current_comic_title

    def setComicNumber(self,resp):
        self.current_comic_num = resp['num']
    def getComicNumber(self):
        return self.current_comic_num

    def setComicDate(self,resp):
        self.day = resp['day']
        self.month = resp['month']
        self.year = resp['year']
    def getComicDate(self):
        return str(self.day) + '-'+ str(self.month) +'-' + str(self.year)
    def getPath(self):
        return self.path
    
    def setImageURL(self,resp):
        self.comic_img_url = resp['img']

