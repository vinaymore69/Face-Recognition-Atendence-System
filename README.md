
# 🧠 Face Recognition Attendance System

A Python-based real-time face recognition system for automating attendance using webcam input. This project uses `OpenCV`, `dlib`, and the `face_recognition` library to detect, recognize, and mark attendance for known individuals. The project was created for learning and academic purposes.

![Python](https://img.shields.io/badge/Python-3.8-blue)
![OpenCV](https://img.shields.io/badge/OpenCV-4.x-success)
![License](https://img.shields.io/badge/License-MIT-lightgrey)

---

## 🎯 Aim

To develop a smart and efficient attendance system that uses facial recognition technology to automatically detect and mark the presence of registered individuals through live webcam feed.

---

## 🛠️ Features

- Real-time face detection using OpenCV and dlib.
- Face recognition using pre-trained deep learning models.
- Automatic attendance logging into a `.csv` file with timestamps.
- Easy-to-update dataset of registered users.
- Error-handling for unrecognized faces or no detection.

---

## 📁 Project Structure

```
Face-Recognition-Attendence-System/
│
├── images/                    # Folder to store known images
├── attendance.csv             # CSV file where attendance is marked
├── recognize_attendance.py    # Main script to start the system
├── encode_faces.py            # Script to encode images and save encodings
├── requirements.txt           # Required Python libraries
└── README.md                  # Project documentation
```

---

## 🚀 How to Run

### 1. Clone the Repository
```bash
git clone https://github.com/vinaymore69/Face-Recognition-Atendence-System.git
cd Face-Recognition-Atendence-System
```

### 2. Install Dependencies
```bash
pip install -r requirements.txt
```

### 3. Prepare Dataset
- Add images of known individuals in the `images/` folder.  
- Name each image using the format: `Name.jpg` or `Name1.png`.

### 4. Encode Known Faces
```bash
python encode_faces.py
```

### 5. Start the Recognition System
```bash
python recognize_attendance.py
```

---

## ✅ Skills Developed

- Python scripting and OpenCV
- Real-time face detection and recognition
- Data handling with CSV
- Debugging and problem-solving
- Understanding of deep learning model usage

---

## 📈 Future Scope

- Integration with database systems (e.g., Firebase, MySQL).
- Web or mobile app interface for remote access.
- Improve accuracy with deep learning enhancements.
- Add support for mask detection or emotion recognition.

---

## 📌 Conclusion

This project demonstrates the power of computer vision and machine learning in automating daily tasks like attendance. It reduces manual work, enhances accuracy, and serves as a stepping stone into the world of AI-powered systems.

---

## 📸 Sample Output

![Sample]([https://user-images.githubusercontent.com/your_placeholder_here.png](https://github.com/vinaymore69/Face-Recognition-Atendence-System/blob/main/Screenshot%202025-04-15%20105037.png))  
*(You can replace this with your own image)*

---

## 🧾 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

---

## 🙋‍♂️ Author

**Vinay More & Shreya Panhale**  
GitHub: [@vinaymore69](https://github.com/vinaymore69) 
GitHub: [@vinaymore69](https://github.com/shreya0512panhale) 
📧 [vinaymore0110@gmail.com](mailto:vinaymore0110@gmail.com) 
📧 [shreayashreddhapanhale@gmail.com](mailto:shreyashreddhapanhale@gmail.com)  
  

---

```

Let me know if you'd like to add a demo video, screenshot, or deploy it on Streamlit or a web interface!
