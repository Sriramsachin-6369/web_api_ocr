<<<<<<< HEAD
from flask import Flask as fl , render_template,Response,request
import cv2
import os
import datetime
import api_ocr 



try:
    os.mkdir('./photos')
except OSError as error:
    pass

switch =0
cam=0

no__cam=0
#sucess=1
#frame=0

   
    
app = fl(__name__ )
  

    
@app.route('/')  #create the web url
def index():
      return render_template('index.html') #comunicate with html file

##############################################################################################################################################

@app.route('/request',methods =['POST','GET'])
def task():
        obj=camera()
        
        if request.method == 'POST':
            if request.form.get('no__cam') == 'switch_cam':
                obj.switchingcamera()
            if request.form.get('stop') == 'Stop/Start':
               obj. start_stop("switch")
            if request.form.get('click_photo') == 'capture_photo':
                obj.capture()
            if request.form.get('ocr_txt') == 'text_extraction':
                ret,img = cam.read()
                return api_ocr.ocr.text(img)
        elif request.method == 'GET':
         return render_template('index.html')
        return render_template('index.html')

#########################################################################################################################################################






@app.route('/video')
def fun():
        obj =camera
        return Response(obj.get_video(),mimetype='multipart/x-mixed-replace; boundary=frame')# transmit the video to the web


######################################################################################################################################################################


class camera:
    frame=0
    sucess=0
    def __init__(self):
         #self.cam=0
        #pass
        self.sucess=1
        self.frame 
  

    def get_video():
        global sucess,frame
        #camera.video_capture()

        while(1):
            sucess,frame =cam.read()
            if  sucess:
                ret,buffer= cv2.imencode('.jpg',frame)
                frame = buffer.tobytes()
                yield (b'--frame\r\n'
                        b'Content-Type: image/jpeg\r\n\r\n' +frame + b'\r\n')
    def capture(self):
                global frame,sucess

                sucess,frame=cam.read()
                now = datetime.datetime.now()
                pa = os.path.sep.join(['photos', "pic_{}.png".format(str(now).replace(":",''))])
                cv2.imwrite(pa,frame)


    def start_stop(self,button):
            global switch
            #switch = button
            
            if (switch ==1):
                switch =0
                cam.release()
                #cv2.destroyAllWindows()
            else:
                switch =1
                camera.video_capture()
                #switch =1
    def switchingcamera(self):
            global no__cam
            if(no__cam == 0):
                cam.release()
                #cv2.destroyAllWindows()
                no__cam =1
                camera.video_capture()
            elif(no__cam==1):
                cam.release()
                #cv2.destroyAllWindows()
                no__cam =0
                camera.video_capture()


    def video_capture():
            #self. cam
            global cam
            cam = cv2.VideoCapture(no__cam)



        
       
      
         
          


 
if __name__=='__main__':
    app.run(debug=True)
cam.release()
=======
from flask import Flask as fl , render_template,Response,request
import cv2
import os
import datetime
import api_ocr 



try:
    os.mkdir('./photos')
except OSError as error:
    pass

switch =0
cam=0

no__cam=0
#sucess=1
#frame=0

   
    
app = fl(__name__ )
  

    
@app.route('/')  #create the web url
def index():
      return render_template('index.html') #comunicate with html file

##############################################################################################################################################

@app.route('/request',methods =['POST','GET'])
def task():
        obj=camera()
        
        if request.method == 'POST':
            if request.form.get('no__cam') == 'switch_cam':
                obj.switchingcamera()
            if request.form.get('stop') == 'Stop/Start':
               obj. start_stop("switch")
            if request.form.get('click_photo') == 'capture_photo':
                obj.capture()
            if request.form.get('ocr_txt') == 'text_extraction':
                ret,img = cam.read()
                return api_ocr.ocr.text(img)
        elif request.method == 'GET':
         return render_template('index.html')
        return render_template('index.html')

#########################################################################################################################################################






@app.route('/video')
def fun():
        obj =camera
        return Response(obj.get_video(),mimetype='multipart/x-mixed-replace; boundary=frame')# transmit the video to the web


######################################################################################################################################################################


class camera:
    frame=0
    sucess=0
    def __init__(self):
         #self.cam=0
        #pass
        self.sucess=1
        self.frame 
  

    def get_video():
        global sucess,frame
        #camera.video_capture()

        while(1):
            sucess,frame =cam.read()
            if  sucess:
                ret,buffer= cv2.imencode('.jpg',frame)
                frame = buffer.tobytes()
                yield (b'--frame\r\n'
                        b'Content-Type: image/jpeg\r\n\r\n' +frame + b'\r\n')
    def capture(self):
                global frame,sucess

                sucess,frame=cam.read()
                now = datetime.datetime.now()
                pa = os.path.sep.join(['photos', "pic_{}.png".format(str(now).replace(":",''))])
                cv2.imwrite(pa,frame)


    def start_stop(self,button):
            global switch
            #switch = button
            
            if (switch ==1):
                switch =0
                cam.release()
                #cv2.destroyAllWindows()
            else:
                switch =1
                camera.video_capture()
                #switch =1
    def switchingcamera(self):
            global no__cam
            if(no__cam == 0):
                cam.release()
                #cv2.destroyAllWindows()
                no__cam =1
                camera.video_capture()
            elif(no__cam==1):
                cam.release()
                #cv2.destroyAllWindows()
                no__cam =0
                camera.video_capture()


    def video_capture():
            #self. cam
            global cam
            cam = cv2.VideoCapture(no__cam)



        
       
      
         
          


 
if __name__=='__main__':
    app.run(debug=True)
cam.release()
>>>>>>> 59cbde7 (updated)
cv2.destroyAllWindows()