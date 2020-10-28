def create_map(self, map_floor, number_of_rooms):
    # print("Creating rooms...")
    map_floor.create_rooms(number_of_rooms)

    # print("Separating rooms...")
    map_floor.separate_rooms()

    # print("Compressing rooms...")
    map_floor.compress_rooms()

def create_map2(self, map_floor, number_of_rooms):
    map_floor.create_rooms(number_of_rooms)
    map_floor.separate_rooms()
    map_floor.compress_rooms()
