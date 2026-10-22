"""
ui.py
-----
Two small reusable widgets: Button and Slider.
Pygame has no ready-made buttons, so we draw and handle them ourselves.
"""
import pygame
import config


class Button:
    def __init__(self, x, y, width, height, text):
        self.rect = pygame.Rect(x, y, width, height)
        self.text = text
        self.enabled = True      # greyed out and unclickable when False
        self.selected = False    # highlighted (used for the chosen algorithm)

    def draw(self, screen, font):
        mouse_over = self.rect.collidepoint(pygame.mouse.get_pos())
        if not self.enabled:
            color, text_color = config.BTN_DISABLED, config.BTN_TEXT_DISABLED
        elif self.selected:
            color, text_color = config.BTN_SELECTED, (255, 255, 255)
        elif mouse_over:
            color, text_color = config.BTN_HOVER, (255, 255, 255)
        else:
            color, text_color = config.BTN_NORMAL, (255, 255, 255)

        pygame.draw.rect(screen, color, self.rect, border_radius=12)
        label = font.render(self.text, True, text_color)
        screen.blit(label, label.get_rect(center=self.rect.center))

    def is_clicked(self, event):
        """True if this event is a left mouse click on an enabled button."""
        return (
            self.enabled
            and event.type == pygame.MOUSEBUTTONDOWN
            and event.button == 1
            and self.rect.collidepoint(event.pos)
        )


class Slider:
    def __init__(self, x, y, width, minimum, maximum, value, label):
        self.rect = pygame.Rect(x, y, width, 8)   # the thin track
        self.minimum = minimum
        self.maximum = maximum
        self.value = value
        self.label = label
        self.enabled = True
        self.dragging = False

    def _knob_x(self):
        fraction = (self.value - self.minimum) / (self.maximum - self.minimum)
        return int(self.rect.x + fraction * self.rect.width)

    def _set_from_mouse(self, mouse_x):
        fraction = (mouse_x - self.rect.x) / self.rect.width
        fraction = max(0.0, min(1.0, fraction))      # keep between 0 and 1
        self.value = round(self.minimum + fraction * (self.maximum - self.minimum))

    def handle_event(self, event):
        """Returns True if the value changed because of this event."""
        if not self.enabled:
            self.dragging = False
            return False
        old_value = self.value
        grab_area = self.rect.inflate(20, 24)         # easier to click
        if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
            if grab_area.collidepoint(event.pos):
                self.dragging = True
                self._set_from_mouse(event.pos[0])
        elif event.type == pygame.MOUSEBUTTONUP and event.button == 1:
            self.dragging = False
        elif event.type == pygame.MOUSEMOTION and self.dragging:
            self._set_from_mouse(event.pos[0])
        return self.value != old_value

    def draw(self, screen, font):
        text = f"{self.label}: {self.value}"
        color = config.TEXT if self.enabled else config.BTN_TEXT_DISABLED
        screen.blit(font.render(text, True, color), (self.rect.x, self.rect.y - 28))
        pygame.draw.rect(screen, config.SLIDER_TRACK, self.rect, border_radius=4)
        knob_color = config.SLIDER_KNOB if self.enabled else config.BTN_DISABLED
        pygame.draw.circle(screen, knob_color, (self._knob_x(), self.rect.centery), 10)
