
class WorkWithFiles(object):
    
    @staticmethod    
    def getDataFrom(source_data_file_name, str_parser):
        text_file = open(source_data_file_name, "r")
        source_data_arr = text_file.readlines()
        result_arr = []
        for source_data_arr_item in source_data_arr:
            p = str_parser(source_data_arr_item)
            result_arr.append(p)
        return result_arr

