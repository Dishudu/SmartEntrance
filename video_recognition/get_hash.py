import face_recognition
import json
import os

def save_face_hash(IMAGE_FOLDER,
                   ENCODINGS_FILE):
    known_faces = {} # Создание словаря для хранения кодировок лиц и имен

    if not os.path.exists(IMAGE_FOLDER):
            os.makedirs(IMAGE_FOLDER)

    # Проходим по всем изображениям в папке
    for image_file in os.listdir(IMAGE_FOLDER):
        if image_file.endswith(('.jpg', '.png')):
            # Загружаем изображение и получаем кодировку
            image_path = os.path.join(IMAGE_FOLDER, image_file)
            image = face_recognition.load_image_file(image_path)
            face_encoding = face_recognition.face_encodings(image)
            
            if face_encoding:
                known_faces[image_file.split('.')[0]] = face_encoding[0].tolist()
            else:
                print(f"Лицо не найдено на изображении: {image_file}")


    # Сохраняем кодировки в файл JSON
    with open(ENCODINGS_FILE, 'w') as f:
        json.dump(known_faces, f)
