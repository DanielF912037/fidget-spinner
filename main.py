from turtle import *

# Initial state of the spinner is null (stable)
state = {'turn': 0, 'color_index': 0}

# Define a list of colors to cycle through
colors = ['blue', 'green', 'yellow', 'red', 'purple', 'orange']

# Draw fidget spinner
def spin():
    clear()

    # Angle of the fidget spinner
    angle = state['turn'] / 10

    # To rotate clockwise, use right; for counterclockwise, use left
    right(angle)

    # Move the turtle forward by the specified distance
    forward(100)

    # Draw a dot with diameter 120 using the current color
    current_color = colors[state['color_index']]
    dot(120, current_color)

    # Move the turtle backward by the specified distance
    back(100)

    "second dot"
    right(120)
    forward(100)

    # Draw the second dot with the next color in the list
    state['color_index'] = (state['color_index'] + 1) % len(colors)
    next_color = colors[state['color_index']]
    dot(120, next_color)

    back(100)

    "third dot"
    right(120)
    forward(100)

    # Draw the third dot with the color after the next color
    state['color_index'] = (state['color_index'] + 1) % len(colors)
    next_color = colors[state['color_index']]
    dot(120, next_color)

    back(100)
    right(120)

    update()

# Animate fidget spinner
def animate():
    if state['turn'] > 0:
        state['turn'] -= 1

    spin()
    ontimer(animate, 20)

# Flick fidget spinner
def flick():
    state['turn'] += 40  # Acceleration of spinner

# Setup window screen
setup(600, 400, 370, 0)
bgcolor("black")

tracer(False)

# Wing of fidget spinner
width(40)
color("blue")

# Keyboard key for the rotation of spinner
onkey(flick, 'space')

listen()
animate()
done()