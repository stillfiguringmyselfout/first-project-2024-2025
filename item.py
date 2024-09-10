class flashlight:

    def __init__(self, name, description):
        self.name = name
        self.description = description
        self.on = False
        self.broken = False

    def turn_on(self):
        if self.on == False and self.broken == False:
            self.on = True
        elif self.broken == True:
            print("The flashlight will not turn on.")
        elif self.on == True:
            print("The flashlight is already on.")
