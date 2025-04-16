
# 🧠 Face Recognition Attendance System

A Python-based real-time face recognition system for automating attendance using webcam input. This project utilizes `OpenCV`, `dlib`, and the `face_recognition` library to detect, recognize, and mark attendance for known individuals. Created for learning and academic purposes.

![Python](https://img.shields.io/badge/Python-3.8-blue)
![OpenCV](https://img.shields.io/badge/OpenCV-4.x-success)
![License](https://img.shields.io/badge/License-MIT-lightgrey)

---

## 🎯 Aim

To develop a smart and efficient attendance system using facial recognition technology that automatically detects and marks the presence of registered individuals via live webcam feed.

---

## 🛠️ Features

- ✅ Real-time face detection using OpenCV and dlib  
- ✅ Face recognition using pre-trained deep learning models  
- ✅ Automatic attendance logging into a `.csv` file with timestamps  
- ✅ Easy-to-update dataset of registered users  
- ✅ Error-handling for unrecognized faces or no detection  

---

## 📁 Project Structure

```
Face-Recognition-Attendance-System/
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
- Add images of known individuals into the `images/` folder.  
- Use the format: `Name.jpg`, `Name1.png`, etc.

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

- Python scripting & OpenCV
- Real-time face detection & recognition
- CSV data handling
- Debugging & problem-solving
- Deep learning model integration

---

## 📈 Future Scope

- 📌 Integration with database systems (e.g., Firebase, MySQL)  
- 📌 Web/mobile app interface for remote attendance  
- 📌 Improved accuracy with deep learning enhancements  
- 📌 Support for mask detection or emotion recognition  

---

## 📸 Sample Output

![Sample Output](https://github.com/vinaymore69/Face-Recognition-Atendence-System/blob/main/Screenshot%202025-04-15%20105037.png)

---

## 📌 Conclusion

This project showcases the power of computer vision and machine learning in automating everyday tasks like attendance tracking. It minimizes manual effort, boosts accuracy, and acts as a foundational step into AI-based systems.

---

## 🧾 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

---

## 👨‍💻 Authors

**Vinay More**  
GitHub: [@vinaymore69](https://github.com/vinaymore69)  
Email: [vinaymore0110@gmail.com](mailto:vinaymore0110@gmail.com)

**Shreya Panhale**  
GitHub: [@shreya0512panhale](https://github.com/shreya0512panhale)  
Email: [shreyashreddhapanhale@gmail.com](mailto:shreyashreddhapanhale@gmail.com)

---
