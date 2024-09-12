class Aircrapt:
    def __init__(self, type, speed, fuel_capacity):
        self.type = type
        self.speed = speed
        self.fuel_capacity = fuel_capacity

    def __repr__(self, type, speed, fuel_capacity):
        return f"tipe:{type},speed:{speed},fuel_capacity:{fuel_capacity}"
