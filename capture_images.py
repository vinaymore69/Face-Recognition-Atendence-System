import cv2
import os

name = input("Enter name: ")
save_dir = os.path.join("dataset", name)
os.makedirs(save_dir, exist_ok=True)

cap = cv2.VideoCapture(1)
count = 0

while True:
    ret, frame = cap.read()
    if not ret:
        break

    cv2.imshow("Capture – Press 's' to save, 'q' to quit", frame)
    key = cv2.waitKey(1) & 0xFF

    if key == ord('s'):
        filename = f"{name}_{count}.jpg"
        cv2.imwrite(os.path.join(save_dir, filename), frame)
        print(f"Saved {filename}")
        count += 1
    elif key == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
