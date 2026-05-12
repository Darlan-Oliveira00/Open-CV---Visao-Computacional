import cv2
import time 

video = cv2.VideoCapture('videogravado.avi')

if video.isOpened == False:
    print('Erro ao abrir o vídeo')

while video.isOpened():
    ret, frame = video.read()

    if ret == True:
        #FPS - Frame Por Segundo
        time.sleep(1/15)
        cv2.imshow('frame', frame)

        if cv2.waitKey(5) & 0xFF == ord('s'):
            break
    else:
        break
video.release()
cv2.destroyAllWindows()