# Sorting Visualizer (Python + Pygame)

A visual tool that demonstrates how different sorting algorithms work by animating an array of bars.

## Features

- Visualizes 7 sorting algorithms
- Adjustable array size and sorting speed
- Generates a new random array
- Displays sorting progress with animated bars

## Algorithms

- Bubble Sort
- Selection Sort
- Insertion Sort
- Merge Sort
- Quick Sort
- Radix Sort
- Shell Sort

## Technologies Used

- Python
- Pygame

## Project Structure

- `main.py` — Application entry point
- `visualizer.py` — Array visualization and drawing
- `ui.py` — Buttons and sliders
- `config.py` — Configuration and constants
- `algorithms/` — Sorting algorithm implementations
- `requirements.txt` — Required Python packages

## Run on Windows

Make sure Python 3.13 and Git are installed.

Open a terminal in the project folder and run:

```bash
py -3.13 -m venv venv
venv\Scripts\activate
python -m pip install -r requirements.txt
python main.py
```

## Purpose

This project helps learners understand sorting algorithms through interactive visual demonstrations.
