import random
import curses
import curses.ascii

s = curses.initscr()
curses.curs_set(0)
curses.noecho()
sh, sw = s.getmaxyx()
s.keypad(1)
s.timeout(150)

snake_x = sw/4
snake_y = sh/2
snake = [[snake_y, snake_x-i] for i in range(3)]
food = None

def spawn_food():
	global food
	food = None
	while food is None:
	    nf = [random.randint(1, sh-1),random.randint(1, sw-1)]
	    food = nf if nf not in snake else None
	s.addch(food[0], food[1], curses.ACS_PI)

key = curses.KEY_RIGHT
spawn_food()
score = 0
while True:
    s.addstr(0, 0, 'Score:'+str(score))
    next_key = s.getch()
    key = key if next_key == -1 else next_key

    if snake[0][0] in [0, sh] or snake[0][1]  in [0, sw] or snake[0] in snake[1:] or key == curses.ascii.ESC:
        curses.endwin()
        quit()

    new_head = [snake[0][0], snake[0][1]]

    if key == curses.KEY_DOWN or key == ord('s'):
        new_head[0] += 1
    if key == curses.KEY_UP or key == ord('w'):
        new_head[0] -= 1
    if key == curses.KEY_LEFT or key == ord('a'):
        new_head[1] -= 1
    if key == curses.KEY_RIGHT or key == ord('d'):
        new_head[1] += 1

    snake.insert(0, new_head)

    if snake[0] == food:
        score+=1
        spawn_food()
    else:
        tail = snake.pop()
        s.addch(int(tail[0]), int(tail[1]), ' ')

    s.addch(int(snake[0][0]), int(snake[0][1]), 'O')
print('GAMEOVER')
