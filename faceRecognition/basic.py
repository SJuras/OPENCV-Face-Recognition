import cv2
import numpy as np
import face_recognition

# step 1 - load image and convert to to RGB
imgElon = face_recognition.load_image_file('Assets/elonMusk.jpg')
imgElon = cv2.cvtColor(imgElon, cv2.COLOR_BGR2RGB)

# load the Test Image
imgTest = face_recognition.load_image_file('Assets/elonmuskTest.jpg')
imgTest = cv2.cvtColor(imgTest, cv2.COLOR_BGR2RGB)


# step 2



cv2.imshow("Main", imgElon)
cv2.imshow("Testing", imgTest)
cv2.waitKey(0)


print("Code Executed")
