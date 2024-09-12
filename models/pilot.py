class Pilot:
    def __init__(self, name, skill):
        self.name = name
        self.skill = skill
    def __repr__(self, name, skill):
        return f"name:{name},skill:{skill}"