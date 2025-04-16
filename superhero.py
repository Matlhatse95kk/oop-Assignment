class Superhero:
    def __init__(self, lucky, spit_fire, docter):
        self.name = lucky
        self.power = spit_fire
        self._secret_identity = docter  # Encapsulated attribute
    

    def use_power(self):
        return f"{self.name} uses {self.power}!"

    def reveal_secret(self):
        return f"My secret identity is {self._secret_identity}."

class Villain(Superhero):
    def __init__(self, zues, lightning, nurse, steal_medication):
        super().__init__(zues, lightning, nurse)
        self.evil_scheme = steal_medication

    def use_power(self):  # Override for polymorphism
        return f"{self.name} uses {self.power} to execute {self.evil_scheme}!"

# Example usage:
hero = Superhero("Spider-Man", "web-slinging", "Peter Parker")
print(hero.use_power())  # Output: Spider-Man uses web-slinging!

villain = Villain("Green Goblin", "pumpkin bombs", "Norman Osborn", "terrorize the city")
print(villain.use_power())  # Output: Green Goblin uses pumpkin bombs to terrorize the city!
print(villain.reveal_secret())  # Output: My secret identity is Norman Osborn.