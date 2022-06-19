import cv2
import numpy as np
import imutils
import os #Para guardar o almacenar datos

Datos =  'p'  # P es el nombre de la carpeta que vamos a crear 
if not os.path.exists(Datos): # Si la carpeta existe no se va a crear 
    print('Carpeta creada: ', Datos)
    os.makedirs(Datos) # Para crear la carpeta 

cap = cv2.VideoCapture(0) #iniciar la camara 

# Especificamos x1,y1 y x2,y2
x1, y1 = 190, 80 #Distancias para nuestro rectangulo
x2, y2 = 450, 398 #Distancias para nuestro rectangulo 
count = 0 #Decalaramos una variable (count) y la igualamos a 0

while True:
    ret, frame = cap.read()
    if ret == False: break #Esta condicion es para que no genere ningun conflicto cuando guardemos la imagen en nuestra computadora

    imAux = frame.copy()
    cv2.rectangle(frame,(x1,y1),(x2,y2),(255,0,0),2) # Aqui dibujamos el rectangulo
    objeto = imAux[y1:y2,x1:x2] #Es para separar el rectangulo en otra zona

   

    k = cv2.waitKey(1)
    if k == ord('s'): #cuando precionemos la tecla S tomara foto de la imagen 
        cv2.imwrite(Datos + '/objeto_{}.jpg'.format(count), objeto) #Guarda la imagen tomada
        print('Imagen almacenada: '+ 'objeto_{}.jpg'.format(count))
        count = count +   1 

    if k == 27: # Esc de nuestra computadora
        break

    cv2.imshow('frame',frame)
    #cv2.imshow('objeto',objeto)
    # objeto = imutils.resize(objeto, width = 38) 
  
cap.release()
cv2.destroyAllWindows()

    
  
