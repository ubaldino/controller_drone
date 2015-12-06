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

PARAMETRO_ROJO      = 0
PARAMETRO_AZUL      = 1
PARAMETRO_VERDE     = 3
PARAMETRO_BLANCO    = 4

mog = cv2.BackgroundSubtractorMOG(history=3, nmixtures=5, backgroundRatio=0.9)

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


def encontrarBordesCanny(imagen):

        #src: matriz de entrada(1->CANAL de 8 bits) imagen de origen que debe ser una imagen de escala de grises
        #thresh: valor umbral se utiliza para clasificar los valores de pixel
        #maxval: valor maximo de umbral
        #type: tipo de umbral
        edges = cv2.Canny(imagen,127,255)

        #encuentra los contornos en una imagen binaria
        #imagen: imagen umbral
        #almacenamiento: cv2.RETR_TREE
        #metodo: CV_CHAIN_APPROX_SIMPLE
        #offsert = (0,0)-> contornos

        contornos, jerarquia = cv2.findContours(edges,cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE)

        #dibujas los contornos de la imagen
        cv2.drawContours(imagen,contornos,-1,(0,255,128),1)

        return imagen

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

    flag,b = cv2.threshold(gray,100,255,cv2.THRESH_BINARY)

    element = cv2.getStructuringElement(cv2.MORPH_ELLIPSE,(7,7))
    cv2.dilate(b,element)

    edges = cv2.Canny(b,100,255)

    lines90 = cv2.HoughLinesP(edges,1, np.pi/180, 100)
    lines180 = cv2.HoughLinesP(edges,1, np.pi, 100)

    if(lines90!=None):
        l = lines90.tolist()
        for x1,y1,x2,y2 in l[0]:
            cv2.line(img, (x1,y1), (x2,y2), (0,255,0), 5)

    if(lines180!=None):
        l = lines180.tolist()
        for x1,y1,x2,y2 in l[0]:
            cv2.line(img, (x1,y1), (x2,y2), (0,255,0), 3)

    return img


def resalteColor(img1,color):
    hsv = cv2.cvtColor(img1, cv2.COLOR_BGR2HSV)
    alto, ancho = hsv.shape[:2]
    img2=np.zeros([alto,ancho,3],dtype=np.uint8)

    # El programa detectara los colores dentro de estos rangos.
    if color == PARAMETRO_ROJO:
       # rojo
       bajos = np.array([0,50,50],dtype=np.uint8)
       altos = np.array([10,255,255],dtype=np.uint8)
       img2[:,:,:]=0,0,255 #rojo intenso en BGR

    elif color == PARAMETRO_AZUL:
        # azul - verde
        bajos = np.array([100,50,50], dtype=np.uint8)
        altos = np.array([130,255,255], dtype=np.uint8)
        img2[:,:,:]=0,0,255 #azul intenso en BGR

    elif color == PARAMETRO_VERDE:
        # azul
        bajos = np.array([45,  50, 50],dtype=np.uint8)
        altos = np.array([90, 255,255],dtype=np.uint8)
        img2[:,:,:]=255,0,255 # verde intenso en BGR

    else: # amarillo - blanco
        bajos = np.array([0,   0,200],dtype=np.uint8)
        altos = np.array([180,64,255],dtype=np.uint8)
        img2[:,:,:]=0,255,0 #amarillo intenso en BGR

    # Vamos a ver que pixeles estan en el rango. La (mascara sera blanco y negro)
    mask = cv2.inRange(hsv, bajos, altos)

    # Filtramos el ruido con un close seguido de un opening.Esto eliminara las zonas blancas de la mascara
    # mas pequenias y dejara las mas grandes, que se supone que seran objetos.
    #Filtrar el ruido con un CLOSE/OPEN
    #kernel = np.ones((6,6),np.uint8)
    #mask = cv2.morphologyEx(mask, cv2.MORPH_CLOSE, kernel)
    #mask = cv2.morphologyEx(mask, cv2.MORPH_OPEN, kernel)

    #Difuminar la mascara para suavizar los contornos y aplicar filtro canny
    #mask = cv2.GaussianBlur(mask, (5, 5), 0)
    #mask = cv2.Canny(mask,1,2)


    # Bitwise-AND mask and original image
    img2=cv2.cvtColor(img2,cv2.COLOR_BGR2HSV)
    img2_fg = cv2.bitwise_and(img2,img2,mask = mask)
    dst = cv2.add(hsv,img2_fg)
    dst = cv2.cvtColor(dst,cv2.COLOR_HSV2BGR)
    return dst



