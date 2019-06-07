class Base:
    MALE_STR = 'male'
    FEMALE_STR = 'female'

    def is_male(self):
        return self.value == self.__class__.MALE_STR

    def is_female(self):
        return not self.is_male


class Male:
    def __init__(self):
        self.value = Base.MALE_STR


class Female:
    def __init__(self):
        self.value = Base.FEMALE_STR
