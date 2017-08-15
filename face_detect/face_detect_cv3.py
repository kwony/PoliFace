#
# Author(s) Hyeonkwon Cho(chkwon91@gmail.com)
#
# Probe image(.jpg) files in directory and crop face area in image.
# 
# Simple usage.
#
# python face_detect_cv3.py \
#        [Image directory to probe] [Cropped image directory to store]

import cv2
import sys
import os
import glob

def faceCrop(imagePath):
    """ Crop face area in image
    Args:
        imagePath: Image path to detect face area
    Returns:
        List of face area.
    """
    # Get user supplied values
    cascPath = "haarcascade_frontalface_default.xml"
    cropImageList = []

    # Create the haar cascade
    faceCascade = cv2.CascadeClassifier(cascPath)

    # Read the image
    image = cv2.imread(imagePath)
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

    # Detect faces in the image
    faces = faceCascade.detectMultiScale(
        gray,
        scaleFactor=1.1,
        minNeighbors=5,
        minSize=(224, 224)
    )

    # if the number of faces exceeds 2, we ignore this image
    if len(faces) >= 2:
        return cropImageList

    # Draw a rectangle around the faces
    for (x, y, w, h) in faces:
        cropImg = image[y:y+h, x:x+w]
        cropImageList.append(cropImg) # Note: image format -> [y: y+h, x: x+w]
        #cv2.imshow("cropped", crop_img) # See face area with image viewer.

    return cropImageList

def imagesCrop(imageDir, cropDir):
    """Probes images and crop/save face area.
    Args:
        imageDir : Directory to probe images.
        cropDir : Directory to save cropped image.
    """
    imageList = glob.glob(imageDir + "*.jpg")

    if len(imageList) <= 0:
        print 'No Image Found'
        return

    print("Found {0} images!".format(len(imageList)))

    for image in imageList:
        cropImageList = faceCrop(image)
        index = 0
        for cropImage in cropImageList:
            # Cropped image name : cropped_{face index}_{original name}
            cv2.imwrite(cropDir + "cropped_" + str(index) + "_"
                    + os.path.basename(image), cropImage)
            index += 1

def main():
    imagePath = sys.argv[1]
    cropDir = sys.argv[2]
    imagesCrop(imagePath, cropDir)

main()
