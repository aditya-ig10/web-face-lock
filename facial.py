import face_recognition
import cv2
import os
import time
import webbrowser
import sys
import pygetwindow as gw

known_people_dir = "known_people"
known_face_encodings = []
known_face_names = []

for file_name in os.listdir(known_people_dir):
    if file_name.endswith(".jpg") or file_name.endswith(".png"):
        name = os.path.splitext(file_name)[0]
        image_path = os.path.join(known_people_dir, file_name)
        image = face_recognition.load_image_file(image_path)
        encoding = face_recognition.face_encodings(image)[0]
        known_face_encodings.append(encoding)
        known_face_names.append(name)

video_capture = cv2.VideoCapture(0)
video_width = 640
video_height = 480
video_capture.set(cv2.CAP_PROP_FRAME_WIDTH, video_width)
video_capture.set(cv2.CAP_PROP_FRAME_HEIGHT, video_height)
video_capture.set(cv2.CAP_PROP_FPS, 1) 

start_time = time.time()
known_face_detected = False
frame_number = 0

while True:
    ret, frame = video_capture.read()
    frame_number += 1

    if frame_number % 2 != 0: 
        continue

    frame = cv2.flip(frame, 1)
    small_frame = cv2.resize(frame, (0, 0), fx=0.25, fy=0.25)

    face_locations = face_recognition.face_locations(small_frame)
    face_encodings = face_recognition.face_encodings(small_frame, face_locations)

    for (top, right, bottom, left), face_encoding in zip(face_locations, face_encodings):
        matches = face_recognition.compare_faces(known_face_encodings, face_encoding)
        name = "Unknown"

        if True in matches:
            first_match_index = matches.index(True)
            name = known_face_names[first_match_index]

            if not known_face_detected:
                start_time = time.time()
                known_face_detected = True

            if time.time() - start_time > 3:
                print("Signing You IN")
                webbrowser.open("D:/LoginIntegration/login.html")
                window = gw.getWindowsWithTitle('Video')[0]
                window.activate()

                sys.exit()

        else:
            known_face_detected = False
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

video_capture.release()
cv2.destroyAllWindows()
