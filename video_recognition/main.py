from face_hash_manager import FaceHashManager
from gpio_controller import GPIOController
from video_face_recognizer import VideoFaceRecognizer
from pathlib import Path

if __name__ == "__main__":
    BASE_DIR = Path(__file__).resolve().parent.parent
    IMAGE_FOLDER = BASE_DIR / "shared" / "faces"
    ENCODINGS_FILE = BASE_DIR / "shared" / "face_encodings.json"

    face_hash_manager = FaceHashManager(IMAGE_FOLDER, ENCODINGS_FILE)
    gpio_controller = GPIOController(pin=17)
    video_recognizer = VideoFaceRecognizer(face_hash_manager, gpio_controller)

    face_hash_manager.save_face_hashes()
    video_recognizer.load_known_faces()
    video_recognizer.process_video()
