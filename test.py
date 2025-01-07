import cv2
import face_recognition

# Load known face encoding and names
known_face_encodings = []
known_face_names = []

# Load known faces and their names here (use raw string literals or escape backslashes)
known_person_1_image = face_recognition.load_image_file(r"C:\Users\habey\OneDrive\Desktop\hostel_ids\habada.png")
known_person_2_image = face_recognition.load_image_file(r"C:\Users\habey\OneDrive\Desktop\hostel_ids\dominic.png")
known_person_3_image = face_recognition.load_image_file("person_3.jpg")

# Encode faces
known_person_1_face_encoding = face_recognition.face_encodings(known_person_1_image)[0]
known_person_2_face_encoding = face_recognition.face_encodings(known_person_2_image)[0]
known_person_3_face_encoding = face_recognition.face_encodings(known_person_3_image)[0]

known_face_encodings.append(known_person_1_face_encoding)
known_face_encodings.append(known_person_2_face_encoding)
known_face_encodings.append(known_person_3_face_encoding)

known_face_names.append("Habada")
known_face_names.append("Dominic")
known_face_names.append("Person 3")

# Initialize webcam
video_capture = cv2.VideoCapture(0)

# Check if the webcam is accessible
if not video_capture.isOpened():
    print("Error: Could not access the webcam.")
    exit()

while True:
    # Capture frame by frame
    ret, frame = video_capture.read()

    if not ret:
        print("Error: Failed to capture image.")
        break

    # Find all the faces and face encodings in the frame of video
    face_locations = face_recognition.face_locations(frame)
    face_encodings = face_recognition.face_encodings(frame, face_locations)

    # Loop through each face in this frame of video
    for (top, right, bottom, left), face_encoding in zip(face_locations, face_encodings):
        # Check if the face is a match for the known face(s)
        matches = face_recognition.compare_faces(known_face_encodings, face_encoding)
        name = "Unknown"

        if True in matches:
            first_match_index = matches.index(True)
            name = known_face_names[first_match_index]

        # Draw box around the face
        cv2.rectangle(frame, (left, top), (right, bottom), (0, 0, 255), 2)
        cv2.putText(frame, name, (left, top-10), cv2.FONT_HERSHEY_SIMPLEX, 0.75, (0, 0, 255), 2)

    # Display the resulting image
    cv2.imshow('Video', frame)

    # Break the loop when 'q' is pressed
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Release the video capture object and close all OpenCV windows
video_capture.release()
cv2.destroyAllWindows()
