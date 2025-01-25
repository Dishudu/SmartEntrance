import face_recognition
import numpy as np
import cv2
from pathlib import Path
from face_hash_manager import FaceHashManager
from gpio_controller import GPIOController


class VideoFaceRecognizer:
    def __init__(self, face_hash_manager: FaceHashManager, gpio_controller: GPIOController):
        self.face_hash_manager = face_hash_manager
        self.gpio_controller = gpio_controller
        self.known_face_encodings = []
        self.known_face_names = []

    def load_known_faces(self):
        known_faces = self.face_hash_manager.load_face_hashes()
        self.known_face_encodings = np.array([np.array(encoding) for encoding in known_faces.values()])
        self.known_face_names = list(known_faces.keys())

    def process_video(self):
        video_capture = cv2.VideoCapture(0)
        try:
            while True:
                ret, frame = video_capture.read()
                if not ret:
                    print("Не удалось получить кадр с веб-камеры")
                    break

                rgb_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
                face_locations = face_recognition.face_locations(rgb_frame, model="hog")
                face_encodings = face_recognition.face_encodings(rgb_frame, face_locations)

                found_known_face = False
                for (face_encoding, face_location) in zip(face_encodings, face_locations):
                    matches = face_recognition.compare_faces(self.known_face_encodings, face_encoding)
                    name = "Unknown"

                    if True in matches:
                        first_match_index = matches.index(True)
                        name = self.known_face_names[first_match_index]
                        found_known_face = True

                    top, right, bottom, left = face_location
                    color = (0, 255, 0) if name != "Unknown" else (0, 0, 255)
                    cv2.rectangle(frame, (left, top), (right, bottom), color, 2)
                    cv2.putText(frame, name, (left, top - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.5, color, 2)

                if found_known_face:
                    print("Знакомое лицо обнаружено")
                    self.gpio_controller.set_high()
                else:
                    print("Лица не распознаны")
                    self.gpio_controller.set_low()

                # Отображение кадра
                cv2.imshow('Video', frame)

                if cv2.waitKey(1) & 0xFF == ord('q'):
                    break
        finally:
            video_capture.release()
            cv2.destroyAllWindows()
            self.gpio_controller.cleanup()
