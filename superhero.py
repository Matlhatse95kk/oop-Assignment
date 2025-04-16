class Superhero:
    def _init_(self, name, power, secret_identity):
        self.name = name
        self.power = power
        self._secret_identity = secret_identity  # Encapsulated attribute

    def use_power(self):
        return f"{self.name} uses {self.power}!"

    def reveal_secret(self):
        return f"My secret identity is {self._secret_identity}."

class Villain(Superhero):
    def _init_(self, name, power, secret_identity, evil_scheme):
        super()._init_(name, power, secret_identity)
        self.evil_scheme = evil_scheme

    def use_power(self):  # Override for polymorphism
        return f"{self.name} uses {self.power} to {self.evil_scheme}!"

# Example usage:
hero = Superhero("Spider-Man", "web-slinging", "Peter Parker")
print(hero.use_power())  # Output: Spider-Man uses web-slinging!

villain = Villain("Green Goblin", "pumpkin bombs", "Norman Osborn", "terrorize the city")
print(villain.use_power())  # Output: Green Goblin uses pumpkin bombs to terrorize the city!
print(villain.reveal_secret())  # Output: My secret identity is Norman Osborn.