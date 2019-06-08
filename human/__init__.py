import gender


class Human:
    HUMAN_MAX_AGE = 100

    def __init__(self, name, age):
        self.name = name
        self.age = age

    def lifetime_age(self):
        return self.__class__.HUMAN_MAX_AGE - self.age_decrement

    def is_man(self):
        return self.gender.is_male()

    def is_woman(self):
        return not self.is_man

    def __str__(self):
        return '<#{}: name={} age={} gender={}>'.format(str(self.__class__), self.name, self.age, self.gender)

    def __repr__(self):
        return self.__str__()


class Man(Human):
    def __init__(self, name, age):
        super().__init__(name, age)
        self.gender = gender.Male()
        self.age_decrement = 10


class Woman(Human):
    def __init__(self, name, age):
        super().__init__(name=name, age=age)
        self.gender = gender.Female()
        self.age_decrement = 20