import pdb


class JourneyParser:
    def __init__(self, filepath):
        self.filepath = filepath
        print('init success')

    def check_filepath(self):
        return self.filepath

    def get_info_from_file(self):
        data_list = []
        file = open(self.filepath, 'r')
        fileline = file.readline()
        data_line = fileline.split(',')
        for i in range(0, len(data_line)):
            data_list.append([data_line[i]])
        while True:
            fileline = file.readline()
            if len(fileline) == 0:
                break
            data_line = fileline.split(',')
            for i in range(0, len(data_line)):
                data_list[i].append(data_line[i])
        file.close()
        return data_list
