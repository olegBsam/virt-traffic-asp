from os import startfile
from com.configuration.config import Configuration
#import tensorflow as tf
#from tensorflow import keras
from com.work_with_files.work_with_files import WorkWithFiles

source_data = WorkWithFiles.getDataFrom(Configuration.bc_oct89ext_filename, Configuration.bc_oct89ext_Str_parser)


t = 12

