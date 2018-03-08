import numpy
import pandas
import math
from keras.models import Sequential
from keras.layers import Dense
from keras.layers import LSTM
from sklearn.preprocessing import MinMaxScaler
from sklearn.metrics import mean_squared_error
from lib.format_utils import *

notes = processed_to_2d_array("./data/processed/beethoven_opus10_1.mid.csv.processed")

