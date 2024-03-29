import cv2
#cascPath = ('haarcascade_frontalface_alt.xml')
imagePath = "./images-122.png"
#faceCascade = cv2.CascadeClassifier(cascPath)haarcascade_frontalface_alt.xml
faceCascade = cv2.CascadeClassifier("./haarcascade_frontalface_alt.xml")
# Read the image
image = cv2.imread(imagePath)
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

# Detect faces in the image
faces = faceCascade.detectMultiScale(
        gray,
        scaleFactor=1.05,
        minNeighbors=3,
    # flags = cv2.cv.CV_HAAR_SCALE_IMAGE
)

print ("Found {0} faces!".format(len(faces)))

# Draw a rectangle around the faces
for (x, y, w, h) in faces:
    cv2.rectangle(image, (x, y), (x+w, y+h), (0, 255, 0), 2)

# Display the resulting frame
cv2.imshow("Faces found",image)
cv2.waitKey(0)

