import pickle
from pprint import pprint

# open the pickle file for reading
obj = pickle.load(open("RML2016.10a_dict.pkl",'rb'), encoding="latin1")

# print the contents of the object
pprint(obj)