"""
algorithms/base.py
------------------
Shared names used by every sorting algorithm.

HOW THE ANIMATION WORKS (important for viva!)
---------------------------------------------
Every algorithm is a *generator function*. A generator can pause itself
with `yield` and continue later from the same line.

Each time an algorithm does something interesting it does:

        yield (ACTION, (index1, index2, ...))

The visualizer takes ONE yielded step per animation tick, colours the
bars, draws the frame and then asks for the next step. This is how we
get a smooth animation without freezing the window.
"""

COMPARE = "compare"   # these bars are being compared        -> yellow
SWAP = "swap"         # these bars were swapped              -> red
WRITE = "write"       # this bar was overwritten with value  -> red
PIVOT = "pivot"       # this bar is the pivot                -> purple
SORTED = "sorted"     # these bars are now in final position -> green
