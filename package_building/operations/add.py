import sys
sys.path.append('\\'.join(__file__.split())[:-2])
from config import config

def add(a, b):
    return config.OUTPUT_FORMAT + str(a + b)