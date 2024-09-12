class Target:

    def __init__(self, name, priority, let,lon):
        self.name = name
        self.priority = priority
        self.let = let,
        self.lon = lon

    def __repr__(self):
        return f"Name: {self.name}, priority: {self.priority}, distance: {self.distance}"