from PyParser import JourneyParser
import gender
from human import Woman, Man, Human


class HumanFabric:
    def __init__(self, data):
        self.data = data

    @staticmethod
    def make_human(ary):
        name, age, gender = ary[0:3]
        return (Man if gender == 'Male' else Woman)(name=name, age=int(age))

    def make_humans(self):
        return list(map(self.make_human, self.data))


parser = JourneyParser(filepath='tmp/input_data.csv')
data = parser()

humans = HumanFabric(data=data).make_humans()
print(humans)

human = HumanFabric.make_human(ary=data[0])
print(human)
