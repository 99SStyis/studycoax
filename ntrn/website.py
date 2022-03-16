class Person:
    type = "human"

    def __parameter__(self, name="Amazon", lastname="Inc" ,objects=10):
        self.name = name
        self.objects = objects
        self.lastname = lastname

    def open(self):
        print(f'{self.name} {self.lastname} bought {self.objects} bananas')

a = Person()
b = Person()
c = Person('Sam', 'Winchester')
d = Person('Ivar', 'Ungelist', 18)

print(a.name, a.lastname, a.ojects('banana'))