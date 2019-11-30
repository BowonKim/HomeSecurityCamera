import picamera
import time
import datetime
import smtplib
from email.mime.text import MIMEText

path = '/media/pi/Segate Backup Plus Drive1/CCTV/video'    #path of a flash drive to store the video files.

def record():
    with picamera.PiCamera() as camera:
        camera.resolution = (640,480)   #set the quality of video files.
        now = datetime.datetime.now()
        filename = now.strftime('%m%d%H') # used time when the video was taken as the name of the file.
        camera.start_recording(output = path + '/' + filename +'.h624')
        camera.wait_recording(10)  #set the time for recording
        textFile = open('storedVideo.txt','a')  #open text file. it will store the name of the video.
        textFile.write(filename + '\n')    #write the name of the video file to text file
        textFile.close()
        time.sleep(10)  # set the time to sleep

        me = 'kbowon98@gmail.com'   #email of sender
        password = 'write the password of email.'   #password of sender's email
        you = 'kbowon98@gmail.com'  #email of recipient
        subject = 'Notification'    #subject of email
        contents = 'Stored video in the flash drive'    #contents of email

        msg = MIMEText(contents, _charset = 'euc-kr')

        msg['subject'] = subject
        msg['from'] = me
        msg['to'] = you

        server = smtplib.SMTP('SMTP.gmail.com',587)
        server.ehlo()
        server.starttls()
        server.ehlo()
        server.login(me,password)

        try:
            server.sendmail(me,you,msg.as_string())
            print("Success")
        except:
            print("Error")
        server.quit()
while True:     #loop to record the video constantly
    record()