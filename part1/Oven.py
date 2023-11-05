class Oven:
    def __init__(self):
        self.ingredientes =[]
        self.output = None

    def add(self, item):
        self.ingredientes.append(item)

    def boil(self):
        if("lead" and "mercury" in self.ingredientes):
            self.output = "gold"
        elif("cheese" and "dough" and "tomato" in self.ingredientes):
            self.output = "pizza"

    def freeze(self):
        if "water" and "air" in self.ingredientes:
            self.output = "snow"

    def wait(self):
        return self.ingredientes

    def get_output(self):
        return self.output

