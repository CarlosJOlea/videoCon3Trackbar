import cv2
import numpy as np

cap = cv2.VideoCapture(1)
cv2.namedWindow("Imagen")


def nada(x):
    pass


#creando barra de desplazamiento

cv2.createTrackbar("LowerH", "Imagen", 0, 255,nada)
cv2.createTrackbar("LowerV", "Imagen", 0, 255,nada)
cv2.createTrackbar("LowerS", "Imagen", 0, 255,nada)


cv2.createTrackbar("UpperH", "Imagen", 0, 255, nada)
cv2.createTrackbar("UpperV", "Imagen", 0, 255, nada)
cv2.createTrackbar("UpperS", "Imagen", 0, 255, nada)


while(1):

    #Leer cada cuadro
    ret, frame = cap.read()
    

    lowerH = cv2.getTrackbarPos("LowerH", "Imagen")
    lowerS = cv2.getTrackbarPos("LowerV", "Imagen")
    lowerV = cv2.getTrackbarPos("LowerS", "Imagen")

    upperH = cv2.getTrackbarPos("UpperH", "Imagen")
    upperS = cv2.getTrackbarPos("UpperV", "Imagen")
    upperV = cv2.getTrackbarPos("UpperS", "Imagen")

    #Definir el rango del color azul en HSV
    lower_blue = np.array([lowerH,lowerS,lowerV])
    upper_blue = np.array([upperH,upperS,upperV])

    #convertir BGR a HSV
    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

    #Umbralizar la imagen para nada mas leer los azules
    mask = cv2.inRange(hsv, lower_blue, upper_blue)

    #Conjuncion bit pot bit
    res = cv2.bitwise_and(frame, frame, mask= mask)
    cv2.imshow('frame', frame)
    cv2.imshow('mask', mask)
    cv2.imshow('res', res)

    if cv2.waitKey(1) == ord("q"):
        break

cv2.destroyAllWindows()