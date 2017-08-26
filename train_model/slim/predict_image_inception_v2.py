#
# Author(s) Hyeonkwon Cho(chkwon91@gmail.com)
#
"""Predict image file with pre-trained inceptionV2 model.

Usage:
```shell

$ python predict_image_inception_v2.py \
        --image_file = {image file path} \
        --check_point = {pre-trained model path} \
        --label_file = {File including classes list} \
"""

import numpy as np
import os
import base64
import tensorflow as tf

try:
    import urllib2 as urllib
except ImportError:
    import urllib.request as urllib

from nets import inception
from preprocessing import inception_preprocessing

from tensorflow.contrib import slim

image_size = inception.inception_v2.default_image_size

###################
# Dataset path #
###################

tf.app.flags.DEFINE_string(
        'check_point', None, 'Pretrained model path.')

tf.app.flags.DEFINE_string(
        'image_file', None, 'Image file to predict')

tf.app.flags.DEFINE_string(
        'label_file', None, 'Label file created by TF converting')

FLAGS = tf.app.flags.FLAGS

def predict(image_file, check_point, label_file):
    """ Predict image file with pre-trained model and print top-3 predictions.
    Arg:
        image_file: Image file to predict.
        check_point: Pretrained model path.
        label_file: Classes list file with txt format
    Returns:
        Nothing.
    """

    with open(label_file) as f:
        classes = f.readlines()

    with tf.Graph().as_default():
        with open(image_file, "rb") as image_file:
            image_string = image_file.read()
        image = tf.image.decode_jpeg(image_string, channels=3)
        processed_image = inception_preprocessing.preprocess_image(image, image_size,
                image_size, is_training=False)
        processed_images  = tf.expand_dims(processed_image, 0)
        # Create the model, use the default arg scope to configure the batch norm parameters.
        with slim.arg_scope(inception.inception_v2_arg_scope()):
            logits, _ = inception.inception_v2(processed_images,
                    num_classes=len(classes), is_training=False)
        probabilities = tf.nn.softmax(logits)

        init_fn = slim.assign_from_checkpoint_fn(check_point, slim.get_model_variables('InceptionV2'))

        with tf.Session() as sess:
            init_fn(sess)
            np_image, probabilities = sess.run([image, probabilities])
            probabilities = probabilities[0, 0:]
            sorted_inds = [i[0] for i in sorted(enumerate(-probabilities), key=lambda x:x[1])]

        # Show top 3 predictions
        for i in range(5):
            index = sorted_inds[i]
            print('Probability %0.2f%% => [%s]' % (probabilities[index] * 100, classes[index]))

def main(_):
    if not FLAGS.image_file:
        raise ValueError('You must supply image file with --image_file')

    if not FLAGS.check_point:
        raise ValueError('You must supply pretrained model path with --check_point')

    if not FLAGS.label_file:
        raise ValueError('You must set label file with --label_file')

    predict(FLAGS.image_file, FLAGS.check_point, FLAGS.label_file)

if __name__ == '__main__':
    tf.app.run()
