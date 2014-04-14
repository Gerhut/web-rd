from pymouse import PyMouse

__all__ = [
    'down',
    'move',
    'up'
]

m = PyMouse()

def down(x, y):
    print('d')
    m.press(x, y)

def move(x, y):
    m.move(x, y)

def up(x, y):
    print('r')
    m.release(x, y)

if __name__ == '__main__':
    down(0, 0)
    up(0, 0)