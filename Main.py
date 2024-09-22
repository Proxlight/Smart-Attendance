import cv2
import face_recognition
import numpy as np
import pandas as pd
from datetime import datetime

# Create lists to store known face encodings and names
known_face_encodings = []
known_face_names = []

# Load known faces from images
def load_known_faces():
    # Load and encode person 1's face
    person1_image = face_recognition.load_image_file("person1.jpg")
    person1_encoding = face_recognition.face_encodings(person1_image)[0]
    known_face_encodings.append(person1_encoding)
    known_face_names.append("Person 1")
    
    # Load and encode person 2's face
    person2_image = face_recognition.load_image_file("person2.jpg")
    person2_encoding = face_recognition.face_encodings(person2_image)[0]
    known_face_encodings.append(person2_encoding)
    known_face_names.append("Person 2")

# Initialize an empty DataFrame for attendance
attendance_df = pd.DataFrame(columns=["Name", "Time"])

# Mark attendance in the DataFrame
def mark_attendance(name):
    now = datetime.now()
    current_time = now.strftime("%H:%M:%S")
    
    # Log attendance if the person has not been recorded already
    if name not in attendance_df["Name"].values:
        attendance_df.loc[len(attendance_df)] = [name, current_time]
        print(f"Marked attendance for {name} at {current_time}")

# Real-time face recognition and attendance marking
def run_attendance_system():
    # Open webcam video stream
    video_capture = cv2.VideoCapture(0)

    while True:
        # Capture frame from webcam
        ret, frame = video_capture.read()
        
        # Resize frame to 1/4 size for faster face recognition
        small_frame = cv2.resize(frame, (0, 0), fx=0.25, fy=0.25)
        rgb_small_frame = small_frame[:, :, ::-1]  # Convert BGR to RGB

        # Find all face locations and face encodings in the current frame
        face_locations = face_recognition.face_locations(rgb_small_frame)
        face_encodings = face_recognition.face_encodings(rgb_small_frame, face_locations)

        for face_encoding, face_location in zip(face_encodings, face_locations):
            # Compare faces with known face encodings
            matches = face_recognition.compare_faces(known_face_encodings, face_encoding)
            face_distances = face_recognition.face_distance(known_face_encodings, face_encoding)
            
            # Find the best match for the detected face
            best_match_index = np.argmin(face_distances)
            if matches[best_match_index]:
                name = known_face_names[best_match_index]
                mark_attendance(name)

                # Draw a rectangle around the face
                top, right, bottom, left = face_location
                top, right, bottom, left = top * 4, right * 4, bottom * 4, left * 4  # Scale back to original size
                cv2.rectangle(frame, (left, top), (right, bottom), (0, 255, 0), 2)
                cv2.putText(frame, name, (left + 6, bottom - 6), cv2.FONT_HERSHEY_SIMPLEX, 0.75, (255, 255, 255), 2)

        # Display the video frame with recognized faces
        cv2.imshow('Attendance System', frame)

        # Press 'q' to quit the video capture
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    # Release the webcam and close video window
    video_capture.release()
    cv2.destroyAllWindows()

