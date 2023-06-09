import meet as meet
import speech_recognition as sr
import pyttsx3

def get_speech_input():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        #print("Please speak your response:")
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


def conversation():
    speak_text("Welcome to the Vidyavardhaka College of Engineering. Let's begin.")
    print("Welcome to the Vidyavardhaka College of Engineering. Let's begin.\n")
    a = True
    b = True
    c = True
    d = True
    e = True
    f = True
    g = True
    h = True
    i = True
    j = True
    l = True
    while a == True:
        speak_text("Please state your name.")
        print("Please State Your Name !!!")
        name = get_speech_input()
        if name:
            speak_text(f"Nice to meet you, {name}.")
            print(name)
            a = False
        else:
            speak_text("Sorry, I didn't catch your name.")
            a == True

    Res=input(f"\nDo you want to rewrite the text? (y/n):")
    print(Res)
    if Res == "y":
        name=input("Enter Your Correct Name:")
    else:
        pass

    while b==True:
        speak_text("Please state your age.")
        print("Please State Your Age !!!")
        age = get_speech_input()
        if age:
            speak_text(f"Great, you are {age} years old.")
            print(age)
            b=False
        else:
            speak_text("Sorry, I didn't catch your age.")
            b==True

    Res1 = input(f"\nDo you want to rewrite the text? (y/n):")
    print(Res1)
    if Res1 == "y":
        age = input("Enter Your Correct Age:")
    else:
        pass

    while c == True:
        speak_text("Please state your gender.")
        print("Please State Your Gender !!!")
        gender = get_speech_input()
        if age:
            speak_text(f"Thank you for providing your gender as {gender}.")
            print(gender)
            c = False
        else:
            speak_text("Sorry, I didn't catch your gender.")
            c == True
    Res2 = input(f"\nDo you want to rewrite the text? (y/n):")
    print(Res2)
    if Res2 == "y":
        gender = input("Enter Your Correct Gender:")
    else:
        pass

    while d == True:
        speak_text("Please state your Date of birth.")
        print("Please State Your Date of birth !!!")
        Date_of_birth = get_speech_input()
        if Date_of_birth:
            speak_text(f"Thank you for providing your Date of birth as {Date_of_birth}.")
            print(Date_of_birth)
            d = False
        else:
            speak_text("Sorry, I didn't catch your Date_of_birth.")
            d ==True

    Res3=input(f"\nDo you want to rewrite the text? (y/n):")
    print(Res3)
    if Res3 == "y":
        Date_of_birth=input("Enter Your Correct Date_birth:")
    else:
        pass

    while e == True:
        speak_text("Please state your Address.")
        print("Please State Your Address!!!")
        Address = get_speech_input()
        if Address:
            speak_text(f"Thank you for providing your Address as {Address}.")
            print(Address)
            e = False
        else:
            speak_text("Sorry, I didn't catch your Address.")
            e == True

    Res4 = input(f"\nDo you want to rewrite the text? (y/n):")
    print(Res4)
    if Res4 == "y":
        Address = input("Enter Your Correct Address:")
    else:
        pass

    while f == True:
        speak_text("Please state your Phone number.")
        print("Please State Your Phone number !!!")
        Phone_number = get_speech_input()
        if Phone_number:
            speak_text(f"Thank you for providing your Phone number as {Phone_number}.")
            print(Phone_number)
            f = False
        else:
            speak_text("Sorry, I didn't catch your Phone_number.")
            f == True

    Res5 = input(f"\nDo you want to rewrite the text? (y/n):")
    print(Res5)
    if Res5 == "y":
        Phone_number = input("Enter Your Correct Phone number:")
    else:
        pass

    while g == True:
        speak_text("Please state your Gmail.")
        print("Please State Your Gmail !!!")
        Gmail = get_speech_input()
        if Gmail:
            speak_text(f"Thank you for providing your Gmail as {Gmail}.")
            Gmail = Gmail.replace("at", "@")
            print(Gmail)
            g = False
        else:
            speak_text("Sorry, I didn't catch your Gmail.")
            g == True

    Res6 = input(f"\nDo you want to rewrite the text? (y/n):")
    print(Res6)
    if Res6 == "y":
        Gmail = input("Enter Your Correct Gmail:")
    else:
        pass

    while h == True:
        speak_text("Please state your Blood group.")
        print("Please State Your Blood group !!!")
        Blood_group = get_speech_input()
        if Blood_group:
            speak_text(f"Thank you for providing your Blood_group as {Blood_group}.")
            Blood_group = Blood_group.replace("positive", "+")
            Blood_group = Blood_group.replace("negative", "-")
            print(Blood_group)
            h = False
        else:
            speak_text("Sorry, I didn't catch your Blood group.")
            h == True

    Res7 = input(f"\nDo you want to rewrite the text? (y/n):")
    print(Res7)
    if Res7 == "y":
        Blood_group = input("Enter Your Correct Blood group:")
    else:
        pass

    while i == True:
        speak_text("Please state your Parents name.")
        print("Please State Your Parents name !!!")
        Parents_name = get_speech_input()
        if Parents_name:
            speak_text(f"Thank you for providing your Parents name as {Parents_name}.")
            print(Parents_name)
            i = False
        else:
            speak_text("Sorry, I didn't catch your Parents_name.")
            i == True

    Res8 = input(f"\nDo you want to rewrite the text? (y/n):")
    print(Res8)
    if Res8 == "y":
        Parents_name = input("Enter Your Correct Parents_name:")
    else:
        pass

    while j == True:
        speak_text("Please state your Nationality.")
        print("Please State Your Nationality !!!")
        Nationality = get_speech_input()
        if Nationality:
            speak_text(f"Thank you for providing your Date of birth as {Nationality}.")
            print(Nationality)
            j = False
        else:
            speak_text("Sorry, I didn't catch your Nationality.")
            j == True

    Res9 = input(f"\nDo you want to rewrite the text? (y/n):")
    print(Res9)
    if Res9 == "y":
        Nationality = input("Enter Your Correct Nationalityy:")
    else:
        pass

    while l == True:
        speak_text("Please state your Previous education.")
        print("Please State Your Previous Education !!!")
        Previous_education = get_speech_input()
        if Previous_education:
            speak_text(f"Thank you for providing your Date of birth as {Previous_education}.")
            print(Previous_education)
            l = False
        else:
            speak_text("Sorry, I didn't catch your Previous_education.")
            l == True

    Res10 = input(f"\nDo you want to rewrite the text? (y/n):")
    print(Res10)
    if Res10 == "y":
        Previous_education = input("Enter Your Correct Previous_education:")
    else:
        pass

    speak_text("Thank you for providing your details. Have a nice day!")


    from fpdf import FPDF

    def create_pdf(text, filename):
        pdf = FPDF()
        pdf.add_page()
        pdf.set_font("Arial", size=12)
        for line in text:
            pdf.multi_cell(0, 10, txt=line)
        pdf.output(filename)

    text = [
        f"Welcome to our institution.",
        "We offer a wide range of courses.",
        f"Hello, {name}!",
        f"Your age is: {age}.",
        f"Your gender is: {gender}.",
        f"Your Date of Birth:{Date_of_birth}",
        f"Your Address id :{Address}",
        f"Your Phone number:{Phone_number}",
        f"Your MailID:{Gmail}",
        f"Your Blood Group:{Blood_group}",
        f"Your Parent Name:{Parents_name}",
        f"Your Nationality:{Nationality}",
        f"Your Nationality:{Previous_education}"
    ]

    create_pdf(text, "profile.pdf")

# Run the conversation
conversation()