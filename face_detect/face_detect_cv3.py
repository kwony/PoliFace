#
# Author(s) Hyeonkwon Cho(chkwon91@gmail.com)
#
# Probe image(.jpg) files in directory and crop face area in image.
# 
# Simple usage.
#
# python face_detect_cv3.py \
#        [Image root directory to probe] [Cropped image root directory to store]
#        [Face marginal space]

import cv2
import sys
import os
import glob

def faceCrop(imagePath, faceMargin):
    """ Crop face area in image
    Args:
        imagePath: Image path to detect face area
        faceMargin: Marginal space on face area
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
        minSize=(224-faceMargin*2, 224-faceMargin*2)
    )

    # if the number of faces exceeds 2, we ignore this image
    if len(faces) >= 2:
        print("Face num >= 2")
        return cropImageList

    for (x, y, w, h) in faces:
        # if it cannot be cropped including marginal space, ignore it.
        if y-faceMargin <= 0 or x-faceMargin <= 0:
            print("Unable to crop marginal space")
            return cropImageList
        cropImg = image[y-faceMargin : y+h+faceMargin, x-faceMargin : x+w+faceMargin]
        cropImageList.append(cropImg) # Note: image format -> [y: y+h, x: x+w]
        #cv2.imshow("cropped", crop_img) # See face area with image viewer.

    return cropImageList

def imagesCrop(imageDir, cropDir, faceMargin):
    """Probes images and crop/save face area.
    Args:
        imageDir : Directory to probe images.
        cropDir : Directory to save cropped image.
        faceMargin : Marginal space on face area
    """
    imageList = glob.glob(imageDir + "*.jpg")

    if len(imageList) <= 0:
        print 'No Image Found'
        return

    print("Found {0} images!".format(len(imageList)))

    for image in imageList:
        cropImageList = faceCrop(image, faceMargin)
        index = 0
        for cropImage in cropImageList:
            # Cropped image name : cropped_{face index}_{original name}
            cv2.imwrite(cropDir + "cropped_" + str(index) + "_"
                    + os.path.basename(image), cropImage)
            index += 1

def traverse_folder(imageDir, cropDir, faceMargin):
    """Probe folders in image Dir and call imagesCrop
       Image data format is on below.
            -> [root directory]/[image classification]/*.jpg
       Cropped image will be stored on this directory
            -> [crop dir]/[image classification]/
       Arg:
           imageDir : Root directory to probe
           cropDir : Root directory to store cropped images
           faceMargin : Marginal space on face area
    """

    for root, dirs, files in os.walk(imageDir):
        print(root)
        for subdir in dirs:
            if not os.path.exists(os.path.join(cropDir, subdir)):
                os.mkdir(os.path.join(cropDir, subdir))
            imagesCrop(os.path.join(root, subdir + "/"),
                    os.path.join(cropDir, subdir + "/"), faceMargin)

def main():
    imageRoot = sys.argv[1]
    cropRoot = sys.argv[2]

    # Set faceMargin variable if third argument is set.
    if len(sys.argv) > 3 :
        print("sys.argv : " + sys.argv[3])
        faceMargin = int(sys.argv[3])
    else:
        faceMargin = 0

    traverse_folder(imageRoot, cropRoot, faceMargin)

main()
