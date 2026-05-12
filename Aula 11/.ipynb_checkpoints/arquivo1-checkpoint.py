import cv2

#Criar a nossa função apresentará o circulo
def desenha_circulo(event, x, y, flags, param):

    #Criar variaveis do tipo global 
    global centro, clique 

    #Condicionais que iram verificar o clique do mouse 
    if event == cv2.EVENT_LBUTTONDOWN:
        centro = (x,y)
        clique = False

    if event == cv2.EVENT_LBUTTONUP:
        clique = True

#Atribuição de Valores
centro = (0,0)
clique = False 

#Captura do Vídeo
cap = cv2.VideoCapture(0)

#Criar uma janela para o vídeo
cv2.namedWindow('Janela')

#Juntar a janela a função desenha_circulo
cv2.setMouseCallback('Janela', desenha_circulo)

while True:

    #Captura frame a frame
    ret, frame = cap.read()

    #Verificar se algo já foi clicado
    if clique:
        #desenhar o circulo
        cv2.circle(frame, center = centro, radius = 80, color = (0,255,0), thickness = 10)

    #Apresentar o frame resultante
    cv2.imshow('Janela', frame)

        #comando de saída 
    if cv2.waitKey(10) & 0xFF == ord('s'):
        break

#Quando finalizar, destruir os elementos 
cap.release()
cv2.destroyAllWindows()