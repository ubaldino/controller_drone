import cv2
import numpy as np

NADA                    = 0
RESALTAR_CUERPOS        = 1
RESALTAR_HUMO           = 2
RESALTAR_FUEGO          = 3
RESALTAR_BORDES         = 4
RESALTAR_LINEAS_RECTAS  = 5
RESALTAR_AZUL           = 6
RESALTAR_ROJO           = 7
RESALTAR_VERDE          = 8
RESALTAR_BLANCO         = 9
DETECTAR_MOVIMIENTO     = 10
RESALTAR_COLORES_FUEGO  = 11

mog = cv2.BackgroundSubtractorMOG(history=3, nmixtures=5, backgroundRatio=0.0001)


#funcion que intensifica los colores en un rango(min y max)
#rango minino de los tres canales HSV: hMin,sMin,vMin
#rango maximo de los tres canales HSV: hMax,sMax,vMax
def aumentarIntensidadPorRangoDeColor(frame,hMin,hMax,sMin,sMax,vMin,vMax):

  #convierte el frame al espacio de color hsv
  hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

  #Se crea un array con las posiciones minimas y maximas
  lower=np.array([hMin,sMin,vMin])
  upper=np.array([hMax,sMax,vMax])

  #Crea una mascara en el rango de colores
  mask = cv2.inRange(hsv, lower, upper)

  #prueba de mascara resultante quitando bit a bit los pixeles
  res = cv2.bitwise_and(frame, frame, mask= mask)

  #fusiona dos imagenes con su grado de opacidad
  #addWeighted(img1,opacidad1,img2,opacidad2)
  salida=cv2.addWeighted(frame,0.7,res,0.3,0)
  return salida

#Funcion que encuentra los contornos de una imagen
#imagen:jpg|png
def encontrarBordes(imagen):
        #recibe una imagen y lo transforma en escala de grises
        imagen_gris = cv2.cvtColor(imagen,cv2.COLOR_BGR2GRAY)

        #src: matriz de entrada(1->CANAL de 8 bits) imagen de origen que debe ser una imagen de escala de grises
        #thresh: valor umbral se utiliza para clasificar los valores de pixel
        #maxval: valor maximo de umbral
        #type: tipo de umbral
        ret,umbral = cv2.threshold(imagen_gris,150,255,0)

        #encuentra los contornos en una imagen binaria
        #imagen: imagen umbral
        #almacenamiento: cv2.RETR_TREE
        #metodo: CV_CHAIN_APPROX_SIMPLE
        #offsert = (0,0)-> contornos

        contornos, jerarquia = cv2.findContours(umbral,cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE)

        #dibujas los contornos de la imagen
        cv2.drawContours(imagen,contornos,-1,(0,255,128),2)

        return imagen

def detectorHaar(img,haar):
    #Convertimos la imagen a escala de grises
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    #Activamos el detector
    #image, cascade, storage, scale_factor=1.1, min_neighbors=3, flags=0, min_size=(0, 0)
    objetosDetectados = haar.detectMultiScale(gray, 1.5, 1)

    #Iniciamos un bucle for para que de cada objeto que cumple con el patron
    #nos proporcione coordenadas y dibujemos rectangulos
    orig = img.copy()
    for (x,y,w,h) in objetosDetectados:
        #dibujamos un rectangulo sobre el objeto deectado
        cv2.rectangle(img,(x,y),(x+w,y+h),(128,0,255),4)
        #aplicamos un filtro para diferenciarlo del resto de la imagen
        #img[y: y + h, x: x + w] =cv2.applyColorMap(orig[y: y + h, x: x + w],4)
    return img


def detectarMovimiento(img) :

    fgmask = mog.apply(img)
    mask_rbg = cv2.cvtColor(fgmask,cv2.COLOR_GRAY2BGR)
    image = img & mask_rbg

    return image

def marcarRectas(img) :

    gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)

    flag,b = cv2.threshold(gray,127,255,cv2.THRESH_BINARY)

    element = cv2.getStructuringElement(cv2.MORPH_CROSS,(1,1))
    #cv2.erode(b,element)

    edges = cv2.Canny(b,127,255)

    lines = cv2.HoughLinesP(edges,1, np.pi/180, 100)

    if(lines!=None):
        l = lines.tolist()
        for x1,y1,x2,y2 in l[0]:
            cv2.line(img, (x1,y1), (x2,y2), (0,255,0), 3)
        img = cv2.cvtColor(edges,cv2.COLOR_GRAY2BGR)
    return img


def resaltarColor(img, color):


    return img


