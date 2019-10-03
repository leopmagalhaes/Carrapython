
#para fechar o programa, pressione a tecla q.

#esse efeito balada é uma forma didática de aprender a separar às cores (RGB) de uma imagem colorida.
import numpy as np
import cv2

cap= cv2.VideoCapture(0)
"""o 0(zero) faz o programa abrir a webcan... se no lugar de 0 fosse colocado o endereço de um arquivo de vídeo, esse arquivo seria aberto"""
contadorBalada=0
"""esse contador será responsável por atribuir os valores das cores (0,1,2) à imagemBalada"""
while(True):
     existeFrame, frame = cap.read()
     """Frane é o nome da variavel que vai receber o frame capturado na função cap.read()"""
     """a variável existeFrame receberá apenas a informação de existência de um frama válido (verdadeiro ou falso), se a variável frame recebe um frame válido, existeFrama será True, caso contrário será false"""
     altura, largura, _ = frame.shape
     """atribui as medidas do frame à altura, largura e canais de cores. Não é necessário informar o canal de cor por isso usa '_'."""
     imagemVazia=np.zeros((altura, largura), dtype='uint8') 
     """criar uma imagem vazia, composta apenas por zeros, ou seja, totalmente preta, ou seja, ausencia de qualquer cor"""
     """esta imagem terá a altura e largura do frame de vídeo. É necessário informar o tipo de dados que estão sendo utilizados"""
     """uint8, como uma imagem possui 3 canais de cor que variam de 0 a 255 para cada bit. 255 em algarismos binários é representado por 11111111, ou seja, oito números "1" (8 bits), por isso uint8"""
     (B, G, R)  = cv2.split(frame)
     """função split quebra a imagem em três, uma para cada cor. è uma variavel tuple, que apresenta três saidas, R, G e B, sendo R (vermelho), G(verde) e B (azul)"""
     R= cv2.merge([imagemVazia, imagemVazia, R])
     """a funlçao cv2.merge, faz uma fuzão entre 3 canais. Neste caso, estamos fundindo imagemVazia + imagemVazia + R, que resulta em uma imagem toda vermelha, pois o único canal que de fato apresenta cor é o vermelho. Da mesma forma, foi feito para os canais G e B abaixo"""
     G= cv2.merge([imagemVazia, G, imagemVazia])
     """imagem toda verde"""
     B= cv2.merge([B, imagemVazia, imagemVazia])
     """imagem toda azul"""
     """estamos pegando cada uma das imagens geradas no split e atribuindo à elas apenas uma cor"""
     imagemBalada = np.zeros((altura, largura, 3), dtype='uint8') #cria uma imagem preenchidas com zeros do tamanho do frame sendo capturado. Esa imagem é salva na variável tipo uint8 chamada de iamgemBalada.
     contadorBalada = contadorBalada % 4 #atribui à variável contadoBalada, quatro números (0,1,2,3).
     """sempre valores 0,1,2,3"""
     #a seguir são feitos alguns condicionais para mostrar imagems diferentes. Essas imagens serão a imagem original, a imagem e as imagens R, G e B.
     if(contadorBalada == 0): #se a variável contadorBalada for igual a zero, etnão irá mostrar a imagem chamada de frame, que é nossa imagem original
        imagemBalada = frame
     elif(contadorBalada == 1): #se o contador tiver valor 1, mostra a imagem R
        imagemBalada = R
     elif(contadorBalada == 2): #se o valor for 2, imagem G
        imagemBalada = G
     elif(contadorBalada == 3): # e se for 3, imagem B
        imagemBalada = B
     contadorBalada +=1 # como temos um contato que pode receber quatro valores (0,1,2,3), o valor inicial é sempre 0. Após a primeira iteração, o valor será somado um (+=1),e então contadorBalada passar a ter valor 1. Na próxima iteração terá valor 2, e depois 3. Como estamos dentro de um loop, essa sequencia de iterações será repetido até que o programa seja encerrado.
     cv2.imshow("webcam", imagemBalada) #mostra a imagem sendo capturada e processada.

#como estramos trabalhando com vídeo, e o vídeo é uma sequencia de frames, o que acontece é que a cada iteração, a cor da imagem será alterada dando uma efeito "balada" na imagem.
     if(cv2.waitKey(50) & 0xFF==ord('q')): #encerra o programa ao pressionar a tecla q. O valro '50' foi utlizado para que fosse possível visualizar a mudança das cores, caso contrário seria tão rápido que ficaria quase que imperceptível.
        break
     """o valor dentro da função waitKey() indica o tempo (em milisegundos) que irá demorar para mudar para o próximo frame"""
     """a função 0xff verifica se a tecla que se aperta no teclado é a mesma que a declarada, se sim, ela fecha o programa"""
cap.release() #libera a camera.
cv2.destroyAllWindows() #fecha qualquer janela aberta pelo programa,
