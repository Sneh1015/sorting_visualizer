"""
main.py
-------
Entry point of the Sorting Visualizer.
Run with:   python main.py

It creates the window, the buttons and sliders, and runs the main loop:
    1. handle events (mouse clicks)
    2. update the animation
    3. draw everything
"""
import sys
import pygame

import config
from algorithms import ALGORITHMS
from ui import Button, Slider
from visualizer import Visualizer


class App:
    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode((config.WINDOW_WIDTH, config.WINDOW_HEIGHT))
        pygame.display.set_caption(config.TITLE)
        self.clock = pygame.time.Clock()

        self.title_font = pygame.font.SysFont("arial", 36, bold=True)
        self.font = pygame.font.SysFont("arial", 18)
        self.small_font = pygame.font.SysFont("arial", 16)

        self.visualizer = Visualizer(config.DEFAULT_SIZE)
        self.selected_name = "Bubble Sort"
        self._create_widgets()
        self._refresh_widget_states()
        self.running = True

    # ---------- building the interface ----------
    def _create_widgets(self):
        # one button per algorithm, laid out in a centred row
        names = list(ALGORITHMS.keys())
        btn_w, btn_h, gap = 140, 40, 10
        total = len(names) * btn_w + (len(names) - 1) * gap
        x = (config.WINDOW_WIDTH - total) // 2
        self.algo_buttons = []
        for name in names:
            self.algo_buttons.append(Button(x, config.ALGO_BUTTON_Y, btn_w, btn_h, name))
            x += btn_w + gap

        self.speed_slider = Slider(60, config.SLIDER_Y, 300, config.MIN_SPEED,
                                   config.MAX_SPEED, config.DEFAULT_SPEED, "Speed")
        self.size_slider = Slider(740, config.SLIDER_Y, 300, config.MIN_SIZE,
                                  config.MAX_SIZE, config.DEFAULT_SIZE, "Size")

        y = config.BOTTOM_BUTTON_Y
        self.start_button = Button(310, y, 220, 44, "Start Sorting")
        self.new_button = Button(570, y, 220, 44, "Generate New Array")

    def _refresh_widget_states(self):
        """Enable / disable widgets depending on whether we are sorting."""
        busy = self.visualizer.is_busy
        for button in self.algo_buttons:
            button.enabled = not busy
            button.selected = button.text == self.selected_name
        self.start_button.enabled = not busy
        self.size_slider.enabled = not busy     # like the original: locked while sorting

    # ---------- events ----------
    def handle_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.running = False
                return

            # algorithm selection
            for button in self.algo_buttons:
                if button.is_clicked(event):
                    self.selected_name = button.text

            # start sorting
            if self.start_button.is_clicked(event):
                self.visualizer.start(ALGORITHMS[self.selected_name])

            # new array (allowed any time - it also stops a running sort)
            if self.new_button.is_clicked(event):
                self.visualizer.stop()
                self.visualizer.generate_array(self.size_slider.value)

            # sliders
            self.speed_slider.handle_event(event)
            if self.size_slider.handle_event(event):
                self.visualizer.generate_array(self.size_slider.value)

    # ---------- drawing ----------
    def draw(self):
        self.screen.fill(config.BACKGROUND)

        title = self.title_font.render("Sorting Visualizer", True, config.TITLE_COLOR)
        self.screen.blit(title, title.get_rect(center=(config.WINDOW_WIDTH // 2, 35)))

        for button in self.algo_buttons:
            button.draw(self.screen, self.small_font)
        self.speed_slider.draw(self.screen, self.font)
        self.size_slider.draw(self.screen, self.font)

        self.visualizer.draw(self.screen)
        self._draw_legend_and_stats()

        self.start_button.draw(self.screen, self.font)
        self.new_button.draw(self.screen, self.font)
        pygame.display.flip()

    def _draw_legend_and_stats(self):
        """Colour legend on the left, counters on the right (under the bars)."""
        y = config.BAR_AREA[1] + config.BAR_AREA[3] + 15
        items = [
            (config.BAR_DEFAULT, "Unsorted"),
            (config.BAR_COMPARE, "Comparing"),
            (config.BAR_SWAP, "Swap / Write"),
            (config.BAR_PIVOT, "Pivot"),
            (config.BAR_SORTED, "Sorted"),
        ]
        x = 25
        for color, text in items:
            pygame.draw.rect(self.screen, color, (x, y + 3, 16, 16), border_radius=3)
            label = self.small_font.render(text, True, config.TEXT)
            self.screen.blit(label, (x + 22, y))
            x += 22 + label.get_width() + 22

        stats = (f"{self.selected_name}   |   Comparisons: {self.visualizer.comparisons}"
                 f"   |   Swaps/Writes: {self.visualizer.swaps}")
        label = self.small_font.render(stats, True, config.TITLE_COLOR)
        self.screen.blit(label, (25, y + 30))

    # ---------- main loop ----------
    def run(self):
        while self.running:
            dt = self.clock.tick(config.FPS)          # ms since last frame
            self.handle_events()
            self.visualizer.update(dt, self.speed_slider.value)
            self._refresh_widget_states()
            self.draw()
        pygame.quit()
        sys.exit()


if __name__ == "__main__":
    App().run()
