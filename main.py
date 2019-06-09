from PyParser import JourneyParser


import gender


class Human:
    HUMAN_MAX_AGE = 100

    def __init__(self, name, age):
        self.name = name
        self.age = age

    def lifetime_age(self):
        return self.__class__.HUMAN_MAX_AGE - self.age_decrement

    def is_man(self):
        return True if self.gender == 'male' else False

    def is_woman(self):
        return not self.is_man

    def __str__(self):
        return '<#{}: name={} age={} gender={}>'.format(str(self.__class__), self.name, self.age, self.gender)


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


man = Man(name='John', age=21)
women = Woman(name='John', age=21)

pars_var = JourneyParser(filepath='./tmp/test1.csv')
print(pars_var.check_filepath())

print(pars_var.get_info_from_file())