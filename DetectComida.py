#importamos librerias
import torch
import cv2
import numpy as np
import torch.hub as hub

#leemos el modelo
model = hub.torch.load('ultralytics/yolov5', 'custom', path='C:/Users/admin/OneDrive/Escritorio/video/DetectorFrutas/model/DetectorFrutas.pt')


#realizamos videocaptura
cap = cv2.Videocapture(1)

#Empezamos
while true:
    #realizar lectura de la videocaptura
    ret, frame = cap.read()

    # realizamos deteccion
    detect = model(frame)

    # mostramos FPS
    cv2.imshow('Detector de frutas',np.squeeze(detect.render()))

    #Leer el teclado
    t = cv2.waitkey(5)
    if t == 27:
        break

cap.release()
cv2.destroyAllwindows()


