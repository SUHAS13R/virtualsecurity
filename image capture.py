import cv2
import os
from datetime import datetime
from reportlab.lib.pagesizes import letter
from reportlab.lib.units import inch
from reportlab.pdfgen import canvas
import speech_recognition as sr
import pyttsx3



def print_image_in_pdf(image_path):
    # Create a new PDF
    count = 1
    pdf_path = f"output{count}.pdf"
    c = canvas.Canvas(pdf_path, pagesize=letter)

    # Load the image
    c.drawImage(image_path, 1 * inch, 1 * inch, width=1.5 * inch, height=2 * inch)

    # Add the real date and time to the PDF
    current_datetime = datetime.now().strftime("Date:%Y-%m-%d Time:%H:%M:%S")
    c.setFont("Helvetica", 12)
    c.drawString(1 * inch, 0.5 * inch, current_datetime)

    # Save and close the PDF
    c.showPage()
    c.save()

    print(f"PDF saved at: {pdf_path}")





# Specify the image path

def capture_live_face_photos_video(output_folder):
    # Load the pre-trained face cascade classifier
    face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')

    # Open the default camera (index 0)
    cap = cv2.VideoCapture(0)

    # Check if the camera was successfully opened
    if not cap.isOpened():
        print("Unable to open the camera.")
        return

    # Create the output folder if it doesn't exist
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)

    # Define the video writer to save the recording
    frame_width = int(cap.get(3))
    frame_height = int(cap.get(4))
    out = cv2.VideoWriter(os.path.join(output_folder, 'output.avi'), cv2.VideoWriter_fourcc('M', 'J', 'P', 'G'), 10,
                          (frame_width, frame_height))

    # Capture live face photos and record video indefinitely
    photo_count = 0
    while True:
        # Read a frame from the camera
        ret, frame = cap.read()

        if ret:
            # Convert the frame to grayscale for face detection
            gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

            # Detect faces in the grayscale frame
            faces = face_cascade.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=5, minSize=(30, 30))

            # Draw rectangles around the detected faces and capture photos
            for (x, y, w, h) in faces:
                # Draw a rectangle around the face
                cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 2), 2)

                # Save the face image as a file
                face_img = frame[y:y + h, x:x + w]
                photo_filename = os.path.join(output_folder, f'face_photo_{photo_count}.jpg')
                cv2.imwrite(photo_filename, face_img)
                photo_count = 0





            # Write the frame to the video
            out.write(frame)

            # Display the frame with face detection
            cv2.imshow("Live Face Photo and Video", frame)
        image_path = os.path.join(output_folder, f'face_photo_{photo_count}.jpg')
        print_image_in_pdf(image_path)
        # Break the loop if 'q' is pressed
        if cv2.waitKey(1) & 0xFF == ord('q'):
            pass

    # Release the video writer, camera, and close all windows
    out.release()
    cap.release()
    cv2.destroyAllWindows()
    image_path = os.path.join(output_folder, f'face_photo_{photo_count}.jpg')
    print_image_in_pdf(image_path)



# Specify the output folder to store the files
output_folder = 'output_folder'

# Call the function to capture live face photos and record video indefinitely, storing the files in the output folder

capture_live_face_photos_video(output_folder)