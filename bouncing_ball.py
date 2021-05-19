import tkinter
import time

CANVAS_WIDTH = 600
CANVAS_HEIGHT = 600
CHANGE_X_START = 10
CHANGE_Y_START = 7

def main():
    ball_size = int(input('Enter the size of the ball (1 - 400): '))
    canvas = make_canvas(CANVAS_WIDTH, CANVAS_HEIGHT, 'Continuous Bouncing Ball')
    canvas.configure(bg='black')
    ball = canvas.create_oval(0, 0, ball_size, ball_size, fill='green', outline='green')
    change_x = CHANGE_X_START
    change_y = CHANGE_Y_START
    while True:
        # update world
        canvas.move(ball, change_x, change_y)
        if hit_left_wall(canvas, ball) or hit_right_wall(canvas, ball):
            change_x *= -1
        if hit_top_wall(canvas, ball) or hit_bottom_wall(canvas, ball):
            change_y *= -1
        # redraw canvas
        canvas.update()
        # pause
        time.sleep(1/50)

def make_canvas(width, height, title):
    """
    Creates and returns a drawing canvas
    of the given int size
    """
    top = tkinter.Tk()
    top.minsize(width=width, height=height)
    top.title(title)
    canvas = tkinter.Canvas(top, width=width + 1, height=height + 1)
    canvas.pack()
    return canvas

def hit_left_wall(canvas, object):
    return get_left_x(canvas, object) <= 0

def hit_top_wall(canvas, object):
    return get_top_y(canvas, object) <= 0

def hit_right_wall(canvas, object):
    return get_right_x(canvas, object) >= CANVAS_WIDTH

def hit_bottom_wall(canvas, object):
    return get_bottom_y(canvas, object) >= CANVAS_HEIGHT

def get_left_x(canvas, object):
    return canvas.coords(object)[0]

def get_top_y(canvas, object):
    return canvas.coords(object)[1]

def get_right_x(canvas, object):
    return canvas.coords(object)[2]

def get_bottom_y(canvas, object):
    return canvas.coords(object)[3]


if __name__ == '__main__':
    main()
