import requests
import os

class XKCD:
    def __init__(self):
        
        self.current_comic_url = ""
        self.message_author = ""
        self.current_comic_title = ""
        self.path = ""
        self.comic_img_url = ""
        self.channel = object()
        self.context = object()

        self.current_comic_num = 0
        self.message_id = 0
        self.day = 0
        self.month = 0
        self.year = 0
        self.latest_comic_number=0
        self.setLatestComicNumber()

    def setLatestComicNumber(self):
        """gets the latest comic's number"""

        #get the current url of the curr comic response
        self.current_comic_url = "https://xkcd.com/info.0.json"
        #requests the url 
        response = requests.get(self.current_comic_url).json()
        #parse the number
        self.latest_comic_number = response['num']
        

    def getLatestComicNumber(self):
        return self.latest_comic_number
     
    
    def pullComic(self,number = 1):
        """pulls the comic of the number passed
       
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
    
    def setContext(self, context):
        self.context = context
    def getContext(self):
        return self.context

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
    def getImageURL(self):
        return self.comic_img_url
    
    def setChannel(self,channel):
        self.channel = channel
    def getChannel(self):
        return self.channel
