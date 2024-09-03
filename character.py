class Character:
    def __init__(self, name, health, inventory):
        self.name = name
        self.health = health
        self.inventory = inventory

    def take_damage(self, damage):
        self.health -= damage
