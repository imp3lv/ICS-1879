class Telephone:
    def __init__(self, number, model):
        self.number = number
        self.model = model
        self.calls = []

    def Call(self, name, number):
        self.calls.append(number)
        print('Дзвінок від', name, number, '- номер додано у список')

    def DeleteCall(self):
        self.calls.pop()
