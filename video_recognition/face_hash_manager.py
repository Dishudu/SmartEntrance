import face_recognition
import json
import os
from pathlib import Path


class FaceHashManager:
    def __init__(self, image_folder: Path, encodings_file: Path):
        self.image_folder = image_folder
        self.encodings_file = encodings_file
        self.known_faces = {}

        if not self.image_folder.exists():
            self.image_folder.mkdir(parents=True)

    def save_face_hashes(self):
        for image_file in os.listdir(self.image_folder):
            if image_file.endswith(('.jpg', '.png')):
                image_path = self.image_folder / image_file
                image = face_recognition.load_image_file(image_path)
                face_encoding = face_recognition.face_encodings(image)

                if face_encoding:
                    self.known_faces[image_file.split('.')[0]] = face_encoding[0].tolist()
                else:
                    print(f"Лицо не найдено на изображении: {image_file}")

        with open(self.encodings_file, 'w') as f:
            json.dump(self.known_faces, f)

    def load_face_hashes(self):
        if not self.encodings_file.exists():
            raise FileNotFoundError("Файл с кодировками лиц не найден. Сохраните известные лица сначала.")
        with open(self.encodings_file, 'r') as f:
            self.known_faces = json.load(f)

        return self.known_faces
