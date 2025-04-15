import cv2
import pickle
import face_recognition
import pandas as pd
from datetime import datetime

# Load known encodings
with open("encodings.pickle", "rb") as f:
    data = pickle.load(f)

# Initialize attendance log
attendance_file = "attendance.csv"
try:
    df = pd.read_csv(attendance_file)
except FileNotFoundError:
    df = pd.DataFrame(columns=["Name", "Time"])

seen_names = set(df["Name"].tolist())

# Initialize camera
cap = cv2.VideoCapture(1, cv2.CAP_DSHOW)
if not cap.isOpened():
    print("[ERROR] Cannot open camera index 1.")
    exit()

print("[INFO] Using camera index 1")
cv2.namedWindow("Attendance", cv2.WINDOW_NORMAL)
print("[INFO] Starting video stream…")

try:
    while True:
        ret, frame = cap.read()
        if not ret:
            print("[WARNING] Failed to grab frame")
            break

        # Face detection and recognition
        small_frame = cv2.resize(frame, (0, 0), fx=0.25, fy=0.25)
        rgb_small = cv2.cvtColor(small_frame, cv2.COLOR_BGR2RGB)

        # Detect faces
        face_locations = face_recognition.face_locations(rgb_small)
        face_encodings = face_recognition.face_encodings(rgb_small, face_locations)

        # Process each face
        for (top, right, bottom, left), face_encoding in zip(face_locations, face_encodings):
            # Scale coordinates back to original size
            top *= 4
            right *= 4
            bottom *= 4
            left *= 4

            # Compare with known faces
            matches = face_recognition.compare_faces(data["encodings"], face_encoding)
            name = "Unknown"

            if True in matches:
                face_distances = face_recognition.face_distance(data["encodings"], face_encoding)
                best_match_index = face_distances.argmin()
                name = data["names"][best_match_index]

            # Draw green rectangle
            cv2.rectangle(frame, (left, top), (right, bottom), (0, 255, 0), 2)
            cv2.putText(frame, name, (left + 6, bottom - 6),
                        cv2.FONT_HERSHEY_SIMPLEX, 0.5, (255, 255, 255), 1)

            # Record attendance
            if name != "Unknown" and name not in seen_names:
                seen_names.add(name)
                time_str = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
                df = pd.concat([df, pd.DataFrame([{"Name": name, "Time": time_str}])], ignore_index=True)
                df.to_csv(attendance_file, index=False)
                print(f"[LOGGED] {name} at {time_str}")

        # Add UI overlays
        cv2.putText(frame, datetime.now().strftime('%Y-%m-%d %H:%M:%S'),
                    (10, 30), cv2.FONT_HERSHEY_SIMPLEX, 0.7, (255, 255, 255), 2)
        cv2.putText(frame, "Press Q to quit", (10, frame.shape[0] - 10),
                    cv2.FONT_HERSHEY_SIMPLEX, 0.7, (255, 0, 0), 2)

        cv2.imshow("Attendance", frame)
        if cv2.waitKey(1) & 0xFF == ord('q'):
            print("\n[INFO] User requested exit")
            break

except Exception as e:
    print(f"[ERROR] {str(e)}")

finally:
    cap.release()
    cv2.destroyAllWindows()
    print("[INFO] Camera released and windows closed")