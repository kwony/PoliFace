""" Library to predict uploaded image file in politician list
"""
import os

# Crop face area in image file
def crop_face_area(filename):
	file_path = "./media/" + filename
	face_margin = "10"

	crop_option = ""
	crop_option += "crop_file" + " "
	crop_option += file_path + " "
	crop_option += file_path + " "
	crop_option += face_margin + " "

	os.system("python3 ../face_detect/face_detect_cv3.py " + crop_option)
	
# Predict politician face with image file
def predict(filename):
	# Assumes that python commands called at poli_web/
	file_path = "./media/" + filename

	crop_face_area(filename)

	check_point_path = "../train_model/trained_model/model.ckpt-10000"
	label_path = "../train_model/trained_model/labels.txt"

	predict_option = ""
	predict_option += "--image_file=" + file_path + " "
	predict_option += "--check_point=" + check_point_path + " "
	predict_option += "--label_file=" + label_path + " "
	os.system("python3 ../train_model/slim/predict_image_inception_v2.py " + predict_option)
