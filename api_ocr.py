import cv2
from flask import render_template
import pytesseract as pt
import spacy
import re

text =0

class ocr():
    def text(img):
        
       
        d_img =cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
        thresh2 = cv2.adaptiveThreshold(d_img, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C,cv2.THRESH_BINARY, 119, 18)
        #cv2.imshow("frame",thresh2)

        ret, thresh4 = cv2.threshold(thresh2, 25 ,220, cv2.THRESH_TOZERO)

        #cv2.waitKey(0)
        text = pt.image_to_string(thresh4)
        print(text)
        obj = card_details(text) 

        obj.company()
        obj.name()
        obj.phone_number()
        obj.address()
        obj.emails()
        obj.websities()


       
        

        return render_template('index.html',tet=obj.ph,email=obj.dh,name=obj.names[0],com=obj.org_names[0],web=obj.web)
class card_details():

    
    
 
    def __init__(self, text):
        self.text = text
        


    def company(self):
        nlp = spacy.load('en_core_web_sm')
        doc = nlp(self.text)
        self.org_names = [ent.text for ent in doc.ents if ent.label_ == 'ORG']
        print( self.org_names)
      
    


    def name(self):
       designation={'Partner','Head','assit'}
       pattern =r"\b([A-Z][a-z]+(?: [A-Z][a-z]+)*)\b(?:.*\b{}\b|)\b".format(designation)

       self.names= re.findall(pattern,self.text,re.DOTALL)

       print(self.names[0])
        
    

    def phone_number(self):

        self.ph=re.findall(r'[\+\(]?[1-9][0-9 .\-\(\)]{8,}[0-9]', self.text)
        print (self.ph)
        
    

    def emails(self):
        self.dh = re.findall(r"[a-z0-9\.\-+_]+@[a-z0-9\.\-+_]+\.[a-z]+", self.text)
        print (self.dh)
        
    
    def address(self):
        pattern =r'\d{1,3}/.*\s-\s\d{3}\s\d{3}'
        self.match = re.findall(pattern, self.text,re.DOTALL)
        print (self.match)


    def websities(self):
        self.web= re.findall(r"(?i)\b((?:[\w-]+:(?:/{1,3}|[a-z0-9%])|www\d{0,3}[.]|[a-z0-9.\-]+[a-z]{2,4}/)(?:[^\s()<>]+))", self.text)
        print (self.web)
        





