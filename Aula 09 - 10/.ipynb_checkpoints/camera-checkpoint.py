import cv2
captura_imagem = cv2.VideoCapture(0)

largura = int(captura_imagem.get(cv2.CAP_PROP_FRAME_WIDTH))
altura = int(captura_imagem.get(cv2.CAP_PROP_FRAME_HEIGHT))

while True:
    ret, frame = captura_imagem.read()
    magma = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    cv2.imshow('frame', magma)

    if cv2.waitKey(10) & 0xFF == ord('s'):
        break
captura_imagem.release()
cv2.destroyAllWindows()