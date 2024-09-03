class Character:
    def __init__(self, name, health, inventory):
        self.name = name
        self.health = health
        self.inventory = inventory

    def take_damage(self, damage):
        self.health -= damage

    def heal(self, amount):
        self.health += amount

    def take_item(self, item):
        self.inventory.append(item)

    def give_item(self, item):
        self.inventory.remove(item)