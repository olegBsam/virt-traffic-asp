import re

class Configuration(object):
    source_data_directory = "./source_data/"
    
    #Чтение из BC-Oct89Ext.TL
    bc_oct89ext_filename = "./source_data/BC-Oct89Ext.TL"

    @staticmethod
    def bc_oct89ext_Str_parser(one_str):
        return re.findall('\d*\.?\d+', one_str)

