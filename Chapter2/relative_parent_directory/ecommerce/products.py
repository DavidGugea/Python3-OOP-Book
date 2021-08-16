"""
import sys
import os

current_file = os.path.realpath(__file__)
current_dir_ecommerce = os.path.dirname(current_file)
parent_dir_parent_directory = os.path.dirname(current_dir_ecommerce)
sys.path.insert(0, parent_dir_parent_directory)
"""

from .database import Database
from ..main import *

class Product:
    pass