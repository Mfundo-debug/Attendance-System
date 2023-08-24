import cv2
import face_recognition
import sqlite3

# Load pre-trained face recognition model
model = face_recognition.load_model('model')

# Connect to attendance database
conn = sqlite3.connect('attendance.db')
c = conn.cursor()

# Capture image from camera
cap = cv2.VideoCapture(0)
ret, frame = cap.read()

# Identify face in image
face_locations = face_recognition.face_locations(frame)
face_encodings = face_recognition.face_encodings(frame, face_locations)

# Check if face is recognized
if len(face_encodings) > 0:
    # Mark attendance in database
    c.execute("INSERT INTO attendance (name, date) VALUES (?, ?)", ('John Doe', '2021-10-01'))
    conn.commit()
else:
    # Prompt user to register face
    print('Face not recognized. Would you like to register your face?')
    response = input()
    if response.lower() == 'yes':
        # Capture image of user's face
        ret, frame = cap.read()
        cv2.imwrite('new_face.jpg', frame)
        
        # Add new face to face recognition model
        new_face = face_recognition.load_image_file('new_face.jpg')
        new_encoding = face_recognition.face_encodings(new_face)[0]
        model.append(new_encoding)
        
        # Mark attendance in database
        c.execute("INSERT INTO attendance (name, date) VALUES (?, ?)", ('John Doe', '2021-10-01'))
        conn.commit()

# Release camera and close database connection
cap.release()
conn.close()