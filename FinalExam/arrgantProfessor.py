class Person(object):
    def __init__(self, name):
        self.name = name

    def say(self, stuff):
        return self.name + ' says: ' + stuff

    def __str__(self):
        return self.name


class Lecturer(Person):
    def lecture(self, stuff):
        return 'I believe that ' + Person.say(self, stuff)


class Professor(Lecturer):
    def say(self, stuff):
        return self.name + ' says: ' + self.lecture(stuff)


class ArrogantProfessor(Person):
    def say(self, stuff):
        return super(ArrogantProfessor, self).say(self.lecture(stuff))

    def lecture(self, stuff):
        return 'It is obvious that ' + super(ArrogantProfessor, self).say(stuff)
