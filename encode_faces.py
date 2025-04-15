import os
import pickle
import face_recognition

known_encodings = []
known_names = []

dataset_dir = "dataset"
for person_name in os.listdir(dataset_dir):
    person_dir = os.path.join(dataset_dir, person_name)
    if not os.path.isdir(person_dir):
        continue

    for img_name in os.listdir(person_dir):
        img_path = os.path.join(person_dir, img_name)
        image = face_recognition.load_image_file(img_path)
        boxes = face_recognition.face_locations(image, model="hog")
        encodings = face_recognition.face_encodings(image, boxes)

        for encoding in encodings:
            known_encodings.append(encoding)
            known_names.append(person_name)

data = {"encodings": known_encodings, "names": known_names}
with open("encodings.pickle", "wb") as f:
    pickle.dump(data, f)

print("[INFO] Encodings serialized to 'encodings.pickle'")
