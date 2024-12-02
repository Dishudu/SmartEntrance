import face_recognition
import numpy as np
import json
import cv2
from get_hash import save_face_hash
from pathlib import Path

# Создание путей с использованием pathlib
BASE_DIR = Path(__file__).resolve().parent.parent
IMAGE_FOLDER = BASE_DIR / "shared" / "faces"
ENCODINGS_FILE = BASE_DIR / "shared" / "face_encodings.json"

if __name__ == "__main__":
    save_face_hash(IMAGE_FOLDER=IMAGE_FOLDER,
                   ENCODINGS_FILE=ENCODINGS_FILE)
    
    # Загружаем известные кодировки из JSON
    with open(ENCODINGS_FILE, 'r') as f:
        known_faces = json.load(f)

    # Преобразуем кодировки в numpy массивы
    known_face_encodings = np.array([np.array(face_encoding) for face_encoding in known_faces.values()])
    known_face_names = list(known_faces.keys())

    # Захват видео с веб-камеры
    video_capture = cv2.VideoCapture(0)

    while True:
        # Захват кадра с веб-камеры
        ret, frame = video_capture.read()
        if not ret:
            print("Не удалось получить кадр с веб-камеры")
            break
        
        # Преобразование изображения из BGR в RGB
        rgb_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        
        # # Уменьшение размера кадров, чтобы снизить нагрузку
        # frame = cv2.resize(rgb_frame, (0, 0), fx=0.5, fy=0.5)


        # Поиск всех лиц на текущем кадре
        face_locations = face_recognition.face_locations(rgb_frame,
                                                        model="hog") # Используйте model="hog" для детекции лиц,
                                                                    # если производительность критична

        # Проверка, найдены ли лица
        if face_locations:
            # Получение кодировок лиц   
            face_encodings = face_recognition.face_encodings(rgb_frame, face_locations)
            # Сравнение каждого найденного лица с известными кодировками
            for (face_encoding, face_location) in zip(face_encodings, face_locations):
                matches = face_recognition.compare_faces(known_face_encodings, face_encoding)
                name = "Unknown"

                # Если найдено совпадение, используем первое найденное имя
                if True in matches:
                    first_match_index = matches.index(True)
                    name = known_face_names[first_match_index]

                # Рисуем рамку вокруг лица
                # Выводим имя, если опознано, иначе выводим "Unknown"
                top, right, bottom, left = face_location
                if name != "Unknown":
                    cv2.rectangle(frame, (left, top), (right, bottom), (0, 255, 0), 2)
                    cv2.putText(frame, name, (left, top - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 255, 0), 2)
                else:
                    cv2.rectangle(frame, (left, top), (right, bottom), (0, 0, 255), 2)
                    cv2.putText(frame, name, (left, top - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 0, 255), 2)
            
        # Отображение видео
        cv2.imshow('Video', frame)
        
        cv2.waitKey(1) # задержка для более стабильного отображения
        
        # Остановка по нажатию клавиши 'q'
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    # Освобождение ресурсов
    video_capture.release()
    cv2.destroyAllWindows()



