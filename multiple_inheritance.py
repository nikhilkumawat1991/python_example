
class father:
    def display(self):
        print("display called from father")

class mother:
    def display(self):
        print("display called from mother")


class child(father,mother):
    pass