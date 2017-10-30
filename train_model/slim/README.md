# PoliFace training/evaluation library
Training models are imported from tensorflow slim library.

In poliface, we usually use inception_v2 model for training and inspection.

# How to train

```shell
$ python train_image_classifier.py --train_dir=${TRAIN_DIR} --dataset_name=poliface --dataset_split_name=train --dataset_dir=${DATA_DIR} --model_name=inception_v2 --clone_on_cpu=True
```

Environment variables indicate directory storing data to train and trained model.

```shell
$ ls $TRAIN_DIR
checkpoint                            model.ckpt-9781.data-00000-of-00001  model.ckpt-9918.data-00000-of-00001
events.out.tfevents.1504017063.kwony  model.ckpt-9781.index ...

$ ls $DATA_DIR
polifaces_train_00003-of-00005.tfrecord  polifaces_validation_00002-of-00005.tfrecord
polifaces_train_00000-of-00005.tfrecord  polifaces_train_00004-of-00005.tfrecord ...
```

# How to retrain

```shell
$python train_image_classifier.py --train_dir=${TRAIN_DIR} --dataset_dir=${DATA_DIR} --dataset_name=poliface --dataset_split_name=train --model_name=inception_v2 --checkpoint_path=${CHECKPOINT_PATH} --clone_on_cpu=True
```

${CHECKPOINT_PATH} is a path the latest version of model training. It is recorded on checkpoint file in ${TRAIN_DIR}

```shell
$ cat checkpoint 
model_checkpoint_path: "/home/kwony/MachinLearning/TensorFlow/TrainSets/poliface/model_inception_v2/model.ckpt-10000"
```

# How to evaluate trained model.

```shell
$python eval_image_classifier.py --alsologtostderr --checkpoint_path=${CHECKPOINT_PATH} --dataset_dir=${DATA_DIR} --dataset_name=poliface --dataset_split_name=validation --model_name=inception_v2 --clone_on_cpu=True
```

Use this command to evaluate trained model. It uses validation data from ${DATA_SET} directory and show result.

# Predict politician with specific image.

```shell
$ python predict_image_inception_v2.py --image_file=${IMAGE_FILE_PATH} --check_point=${PRE-TRAINED MODEL} --label_file=${LABEL_FILE}
```

This command predict image with pre-trained inception_v2 model and show result by labels in label file.
