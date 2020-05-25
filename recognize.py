import face_recognition
import face_recognition_models
import pickle
import cv2
import imutils
from imutils import paths
from imutils.video import VideoStream
import numpy as np
import os
import threading
import time
import datetime

def train():
    inp_path = input("Enter Data Set Path:\n")
    img_path = list(paths.list_images(inp_path))
    knownEncodings = []
    knownNames = []

    for (i, img) in enumerate(img_path):
        print("[INFO] Processing Image {}/{}".format(i + 1,len(img_path)))

        name = img.split(os.path.sep)[-2]

        image = cv2.imread(img)
        rgb = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
        frame = face_recognition.face_locations(rgb, model='hog')
        encodings = face_recognition.face_encodings(rgb, frame)

        for encoding in encodings:
            knownEncodings.append(encoding)
            knownNames.append(name)
    
    print("[INFO] Serializing encodings... ")
    data = {"encodings": knownEncodings, "names": knownNames}
    file = open('./encodings.pickle', "wb")
    file.write(pickle.dumps(data))
    file.close()

def std_lst(name):
    names = []
    names.append(name)
    print(names)


def recognize():
    #display = int(input("Press 1 to Get Diaplay Output or Else 0:"))
    print("[INFO] loading encodings...")
    data = pickle.loads(open("./encodings.pickle", "rb").read())
    print("[INFO] Starting Video Stream...")
    vs = VideoStream(src=0).start()
    #cap = cv2.VideoCapture(0)
    
    while True:
        frame = vs.read()
        rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        rgb = imutils.resize(frame, width=750)
        r = frame.shape[1]/float(rgb.shape[1])
        box = face_recognition.face_locations(rgb, model='hog')
        encodings = face_recognition.face_encodings(rgb, box)

        for encoding in encodings:
            matches = face_recognition.compare_faces(data["encodings"],encoding)
            name = "Unknown"
            
            if True in matches:
                matched_id = [i for (i,b) in enumerate(matches) if b]
                counts = {}

                for i in matched_id:
                    name = data["names"][i]
                    counts[name] = counts.get(name, 0)
                    name = max(counts, key = counts.get)
       
        std_lst(name)
               
        for((top,right,bottom,left), name) in zip(box, name):
            top = int(top*r)
            right = int(right *r)
            bottom = int(bottom *r)
            left = int(left *r)
            cv2.rectangle(frame, (left,top), (right, bottom),(0, 255, 0), 2)
		    #y = (top-15) if (top-15>15) else (top+15)
            if top-15>15:
                y = top-15
            else:
                y = top+15
            cv2.putText(frame, name, (left, y), cv2.FONT_HERSHEY_SIMPLEX,0.75, (0, 255, 0), 2)
        
                      
        cv2.imshow("Frame", frame)
        key = cv2.waitKey(1) & 0xFF    
        if key == ord("q"):
            break
    print(names)
    #time.sleep(5)
    #vs.sleep(10)       
    
    cv2.destroyAllWindows()
    


def main():
    print("*****Menu*****\n")
    inp = int(input("1. Train Faces\n2. Start Recognizer: "))
    if inp == 1: 
        train()
    elif inp == 2:
        #recognize()
        while True:
            recognize()
        #time.sleep(15)
    else:
        print("Invalid Input\n")
if __name__ == "__main__":
   # stuff only to run when not called via 'import' here
   main()




