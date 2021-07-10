from tensorflow.keras.preprocessing import image
from tensorflow.keras.models import load_model as load
import numpy as np
import cv2
import os

# hyperparameter
IMAGE_SIZE = (150, 150)

def load_model():
  checkpoint = 'model/model_none.h5'
  model = load(checkpoint)
  # (loss, accuracy) = model.evaluate( 
  #     train_generator, verbose=1)
  # print("[INFO] Accuracy: {:.2f}%".format(accuracy * 100)) 
  # print("[INFO] Loss: {:.4f}".format(loss))

  return model

def preprocess(img, mode):
  img = cv2.resize(img, IMAGE_SIZE)
  img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
  if mode == 'clahe':
    clahe = cv2.createCLAHE(clipLimit=2.0, tileGridSize=(8,8))
    img = cv2.cvtColor(img, cv2.COLOR_RGB2GRAY)
    img = clahe.apply(img)
    img = cv2.cvtColor(img, cv2.COLOR_GRAY2RGB)
  
  return img

def predict(path, mode):
  print(mode)
  img = cv2.imread(path)
  img = preprocess(img, mode)
  img_tensor = image.img_to_array(img)
  img_tensor = np.expand_dims(img_tensor, axis=0)
  img_tensor /= 255.
  img_tensor = np.vstack([img_tensor])
  model = load_model()
  classes = model.predict(img_tensor)
  pred = np.argmax(classes, axis=1)
  if pred == 0:
    pred = 'Normal'
  else:
    pred = 'COVID-19'
  prob = np.max(classes)

  return pred, prob, img