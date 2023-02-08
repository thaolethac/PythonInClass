# --- Beginning ---
# from utils import Rectangle


rectA = Rectangle(10, 20)
assert rectA.length == 20
assert rectA.width == 10

assert rectA.area == 200
rectA.width = 3
assert rectA.area == 60


rectB = Rectangle(10, 2)
assert rectB.perimeter == 24
# --- End ---
# Traceback (most recent call last):
#   File "main.py", line 1, in <module>
#     from utils import Rectangle
# ImportError: cannot import name 'Rectangle' from 'utils' (/home/p10932/utils.py)
