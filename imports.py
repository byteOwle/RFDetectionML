# Import all the things we need ---
#   by setting env variables before Keras import you can set up which backend and which GPU it uses
# %matplotlib inline
import os,random
os.environ["KERAS_BACKEND"] = "theano"
os.environ["THEANO_FLAGS"] = "device=cuda,floatX=float32"
import numpy as np
from flask import Flask, request, jsonify
import theano as th
import theano.tensor as T
import tensorflow as tf
from keras.utils import np_utils
import tensorflow.keras.models as models
from keras.layers.core import Reshape,Dense,Dropout,Activation,Flatten
from keras.layers.noise import GaussianNoise
from keras.layers.convolutional import Conv2D, MaxPooling2D, ZeroPadding2D
from tensorflow.keras.regularizers import *
from tensorflow.keras.optimizers import Adam
import matplotlib.pyplot as plt
import seaborn as sns
import pickle, random, sys, keras