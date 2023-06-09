from PIL import Image
import os
import speech_recognition as sr
import pyttsx3
from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas
import cv2

def get_speech_input():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        audio = r.listen(source)
    try:
        text = r.recognize_google(audio)
        return text.lower()
    except sr.UnknownValueError:
        print("Sorry, I could not understand your speech.")
        return ""
    except sr.RequestError:
        print("Sorry, there was an issue with the speech recognition service.")
        return ""

def speak_text(text):
    engine = pyttsx3.init()
    engine.say(text)
    engine.runAndWait()

def image_to_pdf(path, voice):
    image_name = f"{voice}_floor.jpg"
    image_path = os.path.join(path, image_name)

    if os.path.exists(image_path):
        # Convert image to PDF
        pdf_path = f"{voice}_floor.pdf"
        c = canvas.Canvas(pdf_path, pagesize=letter)
        c.drawImage(image_path, 0, 0, width=letter[0], height=letter[1])
        c.save()
        print(f"Image '{image_name}' converted to PDF '{pdf_path}' and saved.")
        exit()
    else:
        print(f"Image '{image_name}' not found in folder '{path}'.")


def conversation():
    z = True
    while z:
        print("Where do you want to go?")
        speak_text("Where do you want to go?")
        voice = get_speech_input()
        if voice:
            print(f"your way to, {voice}.")
            speak_text(f"Your way to, {voice}.")
            z = False
        else:
            print("Sorry, I didn't catch that.")
            speak_text("Sorry, I didn't catch that.")
            z = Truen
    res = input("\nDo you want to rewrite the text? (y/n):")
    print(res)
    if res.lower() == "y":
        voice = input("Enter your correct voice:")
    else:
        pass
    path = "paths"
    image_to_pdf(path, voice)


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
            conversation()

            # Break the loop if 'q' is pressed
            if cv2.waitKey(1) & 0xFF == ord('q'):
                break

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

# Call the conversation function to interact with the user through speech recognition and text-to-speech
