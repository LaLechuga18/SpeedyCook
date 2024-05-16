import cv2

# Inicializar la captura de video desde la camara
cap = cv2.VideoCapture(0, cv2.CAP_DSHOW)

# Cargar los clasificadores en cascada para la deteccion de objetos
clasificador_manzana = cv2.CascadeClassifier('manzana_verde.xml') #manzana verde
clasificador_platano = cv2.CascadeClassifier('platano.xml') #platano
clasificador_huevo = cv2.CascadeClassifier('huevo.xml') #huevo
clasificador_jitomate = cv2.CascadeClassifier('jitomate.xml') #jitomate
clasificador_papa = cv2.CascadeClassifier('papa.xml') #papa
clasificador_pan = cv2.CascadeClassifier('pan.xml') #pan
clasificador_lechuga = cv2.CascadeClassifier('lechuga.xml')#lechuga
clasificador_carne = cv2.CascadeClassifier('carne.xml') #carne

while True:
    # Capturar un fotograma de la cámara
    ret, frame = cap.read()
    
    # Convertir el fotograma a escala de grises
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    # Detectar objetos utilizando los clasificadores en cascada
    objetos_Manzana = clasificador_manzana.detectMultiScale(gray, scaleFactor=5, minNeighbors=800, minSize=(70, 78))
    objetos_Platano = clasificador_platano.detectMultiScale(gray, scaleFactor=5, minNeighbors=800, minSize=(70, 78))
    objetos_huevo = clasificador_huevo.detectMultiScale(gray, scaleFactor=5, minNeighbors=800, minSize=(70, 78))
    objetos_jitomate = clasificador_jitomate.detectMultiScale(gray, scaleFactor=5, minNeighbors=800, minSize=(70, 78))
    objetos_papa = clasificador_papa.detectMultiScale(gray, scaleFactor=5, minNeighbors=800, minSize=(70, 78))
    objetos_pan = clasificador_pan.detectMultiScale(gray, scaleFactor=5, minNeighbors=800, minSize=(70, 78))
    objetos_lechuga = clasificador_lechuga.detectMultiScale(gray, scaleFactor=8, minNeighbors=800, minSize=(70, 78))
    objetos_carne = clasificador_carne.detectMultiScale(gray, scaleFactor=8, minNeighbors=800, minSize=(70, 78))

    # Dibujar rectangulos alrededor de los objetos detectados y etiquetarlos
    for (x, y, w, h) in objetos_Manzana:
        cv2.rectangle(frame, (x, y), (x+w, y+h), (0, 255, 0), 2)
        cv2.putText(frame, 'Manzana verde', (x, y-10), cv2.FONT_HERSHEY_SIMPLEX, 0.7, (0, 255, 0), 2)

    for (x, y, w, h) in objetos_Platano:
        cv2.rectangle(frame, (x, y), (x+w, y+h), (0, 0, 255), 2)
        cv2.putText(frame, 'Platano', (x, y-10), cv2.FONT_HERSHEY_SIMPLEX, 0.7, (0, 0, 255), 2)

    for (x, y, w, h) in objetos_huevo:
        cv2.rectangle(frame, (x, y), (x+w, y+h), (255, 0, 0), 2)
        cv2.putText(frame, 'Huevo', (x, y-10), cv2.FONT_HERSHEY_SIMPLEX, 0.7, (255, 0, 0), 2)

    for (x, y, w, h) in objetos_jitomate:
        cv2.rectangle(frame, (x, y), (x+w, y+h), (0, 255, 255), 2)
        cv2.putText(frame, 'jitomate', (x, y-10), cv2.FONT_HERSHEY_SIMPLEX, 0.7, (0, 255, 255), 2)

    for (x, y, w, h) in objetos_papa:
        cv2.rectangle(frame, (x, y), (x+w, y+h), (255, 255, 0), 2)
        cv2.putText(frame, 'Papa', (x, y-10), cv2.FONT_HERSHEY_SIMPLEX, 0.7, (255, 255, 0), 2)

    for (x, y, w, h) in objetos_pan:
        cv2.rectangle(frame, (x, y), (x+w, y+h), (255, 0, 255), 2)
        cv2.putText(frame, 'Pan', (x, y-10), cv2.FONT_HERSHEY_SIMPLEX, 0.7, (255, 0, 255), 2)

    for (x, y, w, h) in objetos_lechuga:
        cv2.rectangle(frame, (x, y), (x+w, y+h), (128, 0, 128), 2)
        cv2.putText(frame, 'Lechuga', (x, y-10), cv2.FONT_HERSHEY_SIMPLEX, 0.7, (128, 0, 128), 2)

    for (x, y, w, h) in objetos_carne:
        cv2.rectangle(frame, (x, y), (x+w, y+h), (0, 128, 128), 2)
        cv2.putText(frame, 'carne', (x, y-10), cv2.FONT_HERSHEY_SIMPLEX, 0.7, (0, 128, 128), 2)

    # Mostrar el fotograma resultante
    cv2.imshow('frame', frame)
    
    # Salir del bucle si se presiona la tecla 'Esc'
    if cv2.waitKey(1) == 27:
        break

# Liberar la captura de video y cerrar todas las ventanas
cap.release()
cv2.destroyAllWindows()
