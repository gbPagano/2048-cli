


class Person:
    def __init__(self, nome, age) -> None:
        self.nome = nome
        self.age = age


    def capitalizar(self):
        self.nome = self.nome.capitalize()


rafael = Person("rafael", 20).capitalizar()

print(rafael)