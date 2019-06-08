class JourneyParser:
    def __init__(self, filepath):
        self.filepath = filepath

    def __call__(self):
        file = open(self.filepath)
        lines = list(map(lambda string: string.strip().split(','), file.readlines()))[1:]
        file.close()
        return lines

