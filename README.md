# Automatic Facial Recognition Attendance System

This Python project uses **OpenCV** and **face_recognition** libraries to create a real-time **Facial Recognition Attendance System**. It captures faces from a webcam, recognizes them, and logs attendance by saving the names and timestamps of recognized individuals into a CSV file.

## Features
- Real-time face detection and recognition using the webcam.
- Attendance is marked automatically when a face is recognized.
- Saves attendance with the current time in a CSV file (`attendance.csv`).
- Can store and recognize multiple faces.

## Installation

To get started with the project, follow these steps:

### 1. Clone the Repository
```bash
git clone https://github.com/yourusername/Facial-Recognition-Attendance-System.git
cd Facial-Recognition-Attendance-System
```

### 2. Install Dependencies
Ensure you have Python installed (version 3.7 or higher). Install the required Python libraries using `pip`:

```bash
pip install opencv-python face-recognition numpy pandas
```

### 3. Add Known Faces
Place images of known individuals in the project folder. Rename the images (e.g., `person1.jpg`, `person2.jpg`, etc.). Modify the `load_known_faces` function in `attendance_system.py` to load these images.

## Usage

1. Run the script:
    ```bash
    python attendance_system.py
    ```
2. The webcam will open, and the system will start detecting and recognizing faces.
3. When a face is recognized, attendance is logged in the terminal and saved in the `attendance.csv` file.
4. Press **‘q’** to quit the webcam and stop the attendance logging.

## How It Works

- The system uses **OpenCV** to capture real-time video from the webcam.
- **face_recognition** library is used to encode the faces and match them against stored known faces.
- When a face is matched, the person’s name and the time of recognition are stored in a **pandas** DataFrame and exported to a CSV file.
  
## File Structure

```
.
|-- attendance_system.py   # Main script to run the attendance system
|-- person1.jpg            # Example image for known face 1
|-- person2.jpg            # Example image for known face 2
|-- attendance.csv         # Attendance output file
|-- README.md              # This README file
```

## Requirements

- Python 3.7 or higher
- OpenCV
- face_recognition
- numpy
- pandas

## Future Enhancements

- Add a GUI for easier management of known faces.
- Integrate with a database system for persistent attendance records.
- Implement multi-camera support for large-scale setups.
- Add email or SMS notifications when attendance is logged.

## Contributing

Contributions, issues, and feature requests are welcome! Feel free to check the [issues page](https://github.com/Proxlight/smart_attendance/issues) if you have any suggestions or bugs to report.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

---

## Author

- **Pratyush Mishra** – Founder of Proxlight
