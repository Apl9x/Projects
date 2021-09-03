import cv2
import os

import math

def face_distance_to_conf(face_distance, face_match_threshold=0.67):
    if face_distance > face_match_threshold:
        range = (1.0 - face_match_threshold)
        linear_val = (1.0 - face_distance) / (range * 2.0)
        return linear_val
    else:
        range = face_match_threshold
        linear_val = 1.0 - (face_distance / (range * 2.0))
        return linear_val + ((1.0 - linear_val) * math.pow((linear_val - 0.5) * 2, 0.2))

            


dataPath = 'C:/Users/Lenny/Desktop/yoyoni/6to/Lunita/Proyecto final AI/data'
imagePaths = os.listdir(dataPath)
print('imagePaths=', imagePaths)

#face_recognizer = cv2.face.EigenFaceRecognizer_create()
#face_recognizer = cv2.face.FisherFaceRecognizer_create()
face_recognizer = cv2.face.LBPHFaceRecognizer_create()



#Leemos el modelo
#face_recognizer.read('modeloEigenface.xml')
#face_recognizer.read('modeloFisherface.xml')
face_recognizer.read('modeloLBPHface.xml')


#cap = cv2.VideoCapture('Videos/Pelon2.mp4')
#cap = cv2.VideoCapture('Pelon.mp4')
#cap = cv2.VideoCapture('Videos/paublo2.mp4')
cap = cv2.VideoCapture('Videos/Pelon4.mp4')
#cap = cv2.VideoCapture('Videos/Jordan.mp4')
#cap = cv2.VideoCapture(0,cv2.CAP_DSHOW)



faceClassif = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')

while True:
    ret,frame = cap.read()
    if ret == False: break
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    auxFrame = gray.copy()

    faces = faceClassif.detectMultiScale(gray,1.3,5)

    for (x,y,w,h) in faces:
        rostro = auxFrame[y:y+h,x:x+w]
        rostro = cv2.resize(rostro,(150,150),interpolation= cv2.INTER_CUBIC)
        result = face_recognizer.predict(rostro)

        cv2.putText(frame,'{}'.format(result),(x,y-5),1,1.3,(255,255,0),1,cv2.LINE_AA)
        '''
        #EigenFaces
        if result[1] < 5500:
            acc = round(face_distance_to_conf(result[1])*-1,2)
            if acc >= 100:
                acc = 100            
            cv2.putText(frame,'{}'.format(imagePaths[result[0]]),(x,y-25),2,1.1,(0,255,0),1,cv2.LINE_AA)
            cv2.putText(frame,'{}%'.format(acc),(x,y+230),1,1.3,(0,255,0),1,cv2.LINE_AA)            
            cv2.rectangle(frame, (x,y),(x+w,y+h),(0,255,0),2)
        else:
            cv2.putText(frame,'Desconocido',(x,y-25),2,1.1,(0,255,0),1,cv2.LINE_AA)
            cv2.rectangle(frame, (x,y),(x+w,y+h),(0,255,0),2)
        
        #FisherFace
        if result[1] < 800:
            acc = round(face_distance_to_conf(result[1])*-1,2)
            if acc >= 100:
                acc = 100            
            cv2.putText(frame,'{}'.format(imagePaths[result[0]]),(x,y-25),2,1.1,(0,255,0),1,cv2.LINE_AA)
            cv2.putText(frame,'{}%'.format(acc),(x,y+230),1,1.3,(0,255,0),1,cv2.LINE_AA)            
            cv2.rectangle(frame, (x,y),(x+w,y+h),(0,255,0),2)
        else:
            cv2.putText(frame,'Desconocido',(x,y-25),2,1.1,(0,255,0),1,cv2.LINE_AA)
            cv2.rectangle(frame, (x,y),(x+w,y+h),(0,255,0),2)        
        '''
        #LBPHFace
        if result[1] < 70:
            acc = round(face_distance_to_conf(result[1])*-1,2)
            if acc >= 100:
                acc = 100
            cv2.putText(frame,'{}'.format((imagePaths[result[0]])),(x,y-25),2,1.1,(0,255,0),1,cv2.LINE_AA)
            cv2.putText(frame,'{}%'.format(acc),(x,y+230),1,1.3,(0,255,0),1,cv2.LINE_AA)
            cv2.rectangle(frame, (x,y),(x+w,y+h),(0,255,0),2)
        else:
            cv2.putText(frame,'Desconocido',(x,y-25),2,1.1,(0,0,255),1,cv2.LINE_AA)
            cv2.rectangle(frame, (x,y),(x+w,y+h),(0,0,255),2)                
        

    cv2.imshow('frame',frame)
    k = cv2.waitKey(1)
    if k == 27:
        break


cap.release()
cv2.destroyAllWindows()