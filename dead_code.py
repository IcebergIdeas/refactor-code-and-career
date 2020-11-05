def test_if_hall_clips_room(self):
    room1 = Room(412, 323, 61, 74)
    # room3 = Room(300, 300, 50, 100)
    # room3.id = 3
    room1.id = 3
    # line = ((350, 350), (400, 350))
    room1.id = 1
    line = ((386, 360), (412, 360))
    clipped_line = room1.rect.clipline(line)
    self.assertTrue(clipped_line)
