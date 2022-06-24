class Product:  # клас виріб
    def values(self):
        return (self.name, self.code)

    def __init__(self, name, code):
        self.name = name
        self.code = int(code)