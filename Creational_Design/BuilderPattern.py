class Person:
    def __init__(self):
        self.name = None
        self.age = None
        self.phone = None
        self.address = None

        # there could be 100s of paramters in a complex object

    def __str__(self):
        return f'Name : {self.name}, age: {self.age} phone: {self.phone} address: {self.address}'


class PersonBuilder:
    def __init__(self, person = Person()):
        self.person = person

    def setname(self, name):
        self.person.name=name
        return self

    def setage(self, age):
        self.person.age=age
        return self

    def setplace(self, add):
        self.person.address=add
        return self

    def build(self):
        return self.person


if __name__ == '__main__':

    pb = PersonBuilder()
    person = pb.build()

    print(person)

    #now here we are only setting age and name as required and we are able to get the Person object
    person =pb.setage(20).setname('Bob').build()
    print(person)
    person = pb.setplace('India').build()
    print(person)
