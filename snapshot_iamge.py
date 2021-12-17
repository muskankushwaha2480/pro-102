import cv2
import dropbox
import time
import random

start_time = time.time()

def take_snapshot():
    number = random.randint(0,10)

    videoCaptureObject = cv2.VideoCapture(0)

    result = True

    while (result):
        ret,frame = videoCaptureObject.read()
        img_name = "img" + str(number) + ".png"
        cv2.imwrite(img_name,frame)
        start_time = time.time
        result = False
    
    return img_name
    print("Snapshot taken")

    videoCaptureObject.release()
    cv2.destroyAllWindows()

def upload_file(img_name):
    access_token = "tFRTRYMm-CIAAAAAAAAAAePTjG_Jm1rTKv4DMOrLQdFzUhRC0Z37LDakr2C7TuZP"
    file = img_name
    file_from = file
    file_to = "/newFolder1/" + (img_name)
    dbx = dropbox.Dropbox(access_token)

    with open(file_from,'rb') as f:
        dbx.files_upload(f.read(),file_to,mode=dropbox.files.WriteMode.overwrite)

def main():
    while(True):
        if((time.time()- start_time) >= 5):
            name = take_snapshot()
            upload_file(name)

main()
