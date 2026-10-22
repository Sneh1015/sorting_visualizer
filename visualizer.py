"""
visualizer.py
-------------
The Visualizer owns the array, runs the chosen algorithm step by step
and draws the bars. It does NOT know about buttons or sliders.
"""
import random
import pygame
import config
from algorithms.base import COMPARE, SWAP, WRITE, PIVOT, SORTED

# which colour each kind of step uses
ACTION_COLORS = {
    COMPARE: config.BAR_COMPARE,
    SWAP: config.BAR_SWAP,
    WRITE: config.BAR_SWAP,
    PIVOT: config.BAR_PIVOT,
}


class Visualizer:
    def __init__(self, size):
        self.area = pygame.Rect(config.BAR_AREA)
        self.array = []
        self.generator = None        # the running algorithm (None = idle)
        self.highlights = {}         # bar index -> colour for this step
        self.sorted_indices = set()  # bars already in their final place
        self.finish_index = None     # used for the green "finished" sweep
        self.comparisons = 0
        self.swaps = 0
        self.timer = 0.0             # milliseconds collected since last step
        self.generate_array(size)

    # ---------- state ----------
    @property
    def is_busy(self):
        """True while an algorithm or the finishing sweep is running."""
        return self.generator is not None or self.finish_index is not None

    def generate_array(self, size):
        """Make a new random array and reset everything."""
        self.array = [
            random.randint(config.MIN_VALUE, config.MAX_VALUE) for _ in range(size)
        ]
        self.generator = None
        self.finish_index = None
        self.highlights = {}
        self.sorted_indices = set()
        self.comparisons = 0
        self.swaps = 0
        self.timer = 0.0

    def start(self, algorithm):
        """Start animating `algorithm` on the current array."""
        if self.is_busy:
            return
        # If the user presses start on an already sorted array, make a fresh one
        if self.sorted_indices or self.array == sorted(self.array):
            self.generate_array(len(self.array))
        self.generator = algorithm(self.array)   # does not run yet, just created
        self.timer = 0.0

    def stop(self):
        """Abort the animation (used when the array is regenerated)."""
        self.generator = None
        self.finish_index = None

    # ---------- animation ----------
    def update(self, dt_ms, speed):
        """Called once per frame. dt_ms = time since last frame in ms."""
        self.timer += dt_ms
        delay = config.DELAY_BASE - speed        # same formula as the JS project
        steps_done = 0
        # a frame is ~16 ms, so for small delays we do several steps per frame
        while self.is_busy and self.timer >= delay and steps_done < 60:
            self.timer -= delay
            steps_done += 1
            if self.generator is not None:
                self._next_algorithm_step()
            else:
                self._next_finish_step()
        if not self.is_busy:
            self.timer = 0.0

    def _next_algorithm_step(self):
        try:
            action, indices = next(self.generator)   # run algorithm to next yield
        except StopIteration:
            self.generator = None                    # algorithm finished
            self.highlights = {}
            self.finish_index = 0                    # begin the green sweep
            return

        if action == SORTED:
            self.sorted_indices.update(indices)
            self.highlights = {}
            return

        self.highlights = {i: ACTION_COLORS[action] for i in indices}
        if action == COMPARE:
            self.comparisons += 1
        elif action in (SWAP, WRITE):
            self.swaps += 1

    def _next_finish_step(self):
        """Turn the bars green from left to right when sorting is complete."""
        self.sorted_indices.add(self.finish_index)
        self.finish_index += 1
        if self.finish_index >= len(self.array):
            self.finish_index = None

    # ---------- drawing ----------
    def draw(self, screen):
        pygame.draw.rect(screen, config.PANEL, self.area, border_radius=10)
        pygame.draw.rect(screen, config.PANEL_BORDER, self.area, 2, border_radius=10)

        n = len(self.array)
        if n == 0:
            return
        padding = 10
        usable_w = self.area.width - 2 * padding
        usable_h = self.area.height - 2 * padding
        bar_w = usable_w / n

        for i, value in enumerate(self.array):
            if i in self.highlights:
                color = self.highlights[i]
            elif i in self.sorted_indices:
                color = config.BAR_SORTED
            else:
                color = config.BAR_DEFAULT

            height = max(2, int(value / config.MAX_VALUE * usable_h))
            x = self.area.x + padding + int(i * bar_w)
            next_x = self.area.x + padding + int((i + 1) * bar_w)
            width = max(1, next_x - x - 1)               # 1 px gap between bars
            y = self.area.bottom - padding - height
            pygame.draw.rect(screen, color, (x, y, width, height), border_radius=2)
