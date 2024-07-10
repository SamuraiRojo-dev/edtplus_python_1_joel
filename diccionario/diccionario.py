import cv2
import os
import numpy as np
from PIL import Image

# Ruta de la carpeta donde se encuentran las imágenes de entrenamiento
train_dir = 'path/to/train/images'

# Inicializar el reconocedor de rostros
recognizer = cv2.face.LBPHFaceRecognizer_create()

# Función para obtener las etiquetas y los datos de entrenamiento
def get_images_and_labels(path):
    image_paths = [os.path.join(path, f) for f in os.listdir(path)]
    face_samples = []
    ids = []

    for image_path in image_paths:
        PIL_img = Image.open(image_path).convert('L')
        img_numpy = np.array(PIL_img, 'uint8')
        id = int(os.path.split(image_path)[-1].split(".")[0])
        faces = face_cascade.detectMultiScale(img_numpy)

        for (x, y, w, h) in faces:
            face_samples.append(img_numpy[y:y+h, x:x+w])
            ids.append(id)

    return face_samples, ids

# Cargar el clasificador de rostros pre-entrenado
face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')

# Obtener las imágenes y etiquetas de entrenamiento
faces, ids = get_images_and_labels(train_dir)

# Entrenar el reconocedor de rostros
recognizer.train(faces, np.array(ids))

# Inicializar la cámara
cap = cv2.VideoCapture(0)

while True:
    # Capturar un frame de la cámara
    ret, img = cap.read()

    # Convertir la imagen a escala de grises
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    # Detectar los rostros en la imagen
    faces = face_cascade.detectMultiScale(gray, scaleFactor=1.2, minNeighbors=5)

    for (x, y, w, h) in faces:
        # Obtener la predicción del reconocedor de rostros
        id, confidence = recognizer.predict(gray[y:y+h, x:x+w])

        # Dibujar rectángulos alrededor de los rostros detectados
        cv2.rectangle(img, (x, y), (x+w, y+h), (255, 0, 0), 2)

        # Mostrar el nombre del usuario reconocido
        print(f'Usuario reconocido: {id} (Confianza: {confidence}%)')

    # Mostrar la imagen con los rostros detectados
    cv2.imshow('img', img)

    # Salir del bucle si se presiona la tecla 'q'
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Liberar la cámara y cerrar todas las ventanas
cap.release()
cv2.destroyAllWindows()