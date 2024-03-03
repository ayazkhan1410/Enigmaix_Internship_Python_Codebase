import cv2  # Import the OpenCV library.

# Load the pre-trained face detection model from a file.
face_cascade = cv2.CascadeClassifier('C:/Users/ayazb/AppData/Local/Programs/Python/Python311/Lib/site-packages/cv2/data/haarcascade_frontalface_default.xml')

# Open the default camera (0) for video capture.
cap = cv2.VideoCapture(0)

# Start an infinite loop for real-time video processing.
while True:
    _, image = cap.read()  # Read a frame from the camera.

    # Convert the frame to grayscale for face detection.
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

    # Detect faces in the grayscale frame using the face detection model.
    faces = face_cascade.detectMultiScale(gray, 1.1, 4)

    # Loop through the detected faces and draw rectangles around them.
    for (x, y, w, h) in faces:
        cv2.rectangle(image, (x, y), (x + w, y + h), (0, 300, 0), 4)

    # Display the frame with detected faces in a window named 'REAL-TIME FACE DETECTION'.
    cv2.imshow('REAL-TIME FACE DETECTION', image)

    # Check if the user pressed the 'a' key, and if so, exit the loop.
    if cv2.waitKey(10) == ord("a"):
        break

# Release the camera when the loop ends.
cap.release()
