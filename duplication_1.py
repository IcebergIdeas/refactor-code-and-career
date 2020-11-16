import pygame

WHITE = (232, 232, 232)
BLACK = (0, 0, 0)

def display_room_information(self, display_room):
    self.display_room_text(pygame.font.SysFont(None, 32), (70, 20), str(display_room.id))
    info = f"{display_room}"
    self.display_room_text(pygame.font.SysFont(None, 20), (70, 50), info)
    info = f"x:{display_room.rect.x} y:{display_room.rect.y}"
    self.display_room_text(pygame.font.SysFont(None, 20), (70, 70), info)
    info = f"width:{display_room.rect.width} height:{display_room.rect.height}"
    self.display_room_text(pygame.font.SysFont(None, 20), (70, 90), info)
    info = f"connections:"
    for door in display_room.doors:
        info += str(door.destination) + "(" + str(door.coordinates) + "), "
    self.display_room_text(pygame.font.SysFont(None, 20), (70, 110), info)
    info = f"doors:{display_room.doors}"
    self.display_room_text(pygame.font.SysFont(None, 20), (70, 130), info)


def display_room_text(self, font, font_top_left, display_text):
    text = font.render(str(display_text), True, WHITE, BLACK)
    text_rect = text.get_rect()
    text_rect.topleft = font_top_left
    self._room_surface.blit(text, text_rect)
