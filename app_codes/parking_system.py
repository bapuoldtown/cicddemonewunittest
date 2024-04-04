from collections import defaultdict


class ParkingSystem:
    vehicle_list = defaultdict(list)

    def __init__(self, name: str, typ: str):
        self.name = name
        self.typ = typ

    def reserve_mid(self):
        self.vehicle_list["mid_vehicle"].append({self.name: self.typ})

    def reserve_large(self):
        self.vehicle_list["large_vehicle"].append({self.name: self.typ})

    @classmethod
    def display(cls):
        return dict(cls.vehicle_list)


sob = ParkingSystem("grand_i10", "mid")
lob = ParkingSystem("isuzu max", "large")
sob.reserve_mid()
lob.reserve_large()

print(ParkingSystem.display())
