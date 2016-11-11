import random

world={}
empty=[]

is_move = False

def init_world():
    for y in range(4):
        for x in range(4):
            set_xy((x,y),0)
    set_xy(random.choice(empty),random.choice([2,4]))
    set_xy(random.choice(empty),random.choice([2,4]))


def get_xy(location):
    return world[location]


def set_xy(location,value):
    world[location] = value
    if location in empty and value != 0:
        empty.remove(location)
    elif location not in empty and value == 0:
        empty.append(location)


def print_world():
    for y in range(4):
        print 45*'='
        for x in range(4):
            v = get_xy((x,y))
            if v != 0:
                print "%4s%6s"%(v,'||'),
            else:
                print "%4s%6s"%(' ','||'),
        print '\n'
    print 45*'='


def is_side(location):
    x,y=location
    if x == 0 or x == 3 or y == 0 or y == 3:
        return True
    else:
        return False


def is_out(location):
    x, y = location
    if x < 0 or x > 3 or y < 0 or y > 3:
        return True
    else:
        return False

def next_step(location,where):
    x,y = location
    if 'a' == where:
        return (x-1,y)
    if 'd' == where:
        return (x+1,y)
    if 'w' == where:
        return (x,y-1)
    if 's' == where:
        return (x,y+1)


def where_to_go(location,where):
    now = location
    if is_side(now) and is_out(next_step(now,where)):
        return now
    now = next_step(location,where)
    if get_xy(now) != 0:
        return now
    return where_to_go(now,where)


opposite={'a':'d','d':'a','w':'s','s':'w'}
key={'a':0,'d':1,'s':1,'w':0}

def move_all(direct):
    global is_move
    ha = key[direct]
    for y in range(4):
        for x in range(4):
            location = (abs(x-3*ha),abs(y-3*ha))
            now = location
            now_value = get_xy(location)

            if now_value == 0:
                continue
            else:
                goal = where_to_go(now,direct)
                #side
                if goal == now:
                    continue
                goal_value = get_xy(goal)
                #move ot side
                if goal_value == 0:
                    set_xy(goal,now_value)
                    set_xy(now,0)
                #plus
                elif goal_value == now_value:
                    set_xy(goal,goal_value+now_value)
                    set_xy(now,0)
                #stand by
                elif next_step(goal,opposite[direct]) == now:
                    continue
                else: 
                	set_xy(next_step(goal,opposite[direct]),now_value)
                	set_xy(now,0)
                is_move = True


def check_death():
	if empty:
		return False
	for x in range(4):
		for y in range(4):
			if y == 3:
				continue
			if get_xy((x,y)) == get_xy((x,y+1)):
				return False
	for y in range(4):
		for x in range(4):
			if x == 3:
				continue
			if get_xy((x,y)) == get_xy((x+1,y)):
				return False
	return True


def show_empty():
	tmp = 1
    for y in range(4):
    	for x in range(4):
    		if y == tmp:
				print '\n'
				tmp+=1
    		if (x,y) in empty:
    			print (x,y),
    		else:
    			print '      ',
	print '\n'


def run():
    global is_move
    init_world()
    while True:
    	# show_empty()
        print_world()
        move = raw_input("your move!\n")
        if move not in ('a','s','w','d','q'):
            print 'error input'
            continue
        if move == 'q':
            return
        move_all(move)
        
        if check_death():
        	print_world()
        	print 'you dead sb!!!'
        	return
        if is_move:
        	set_xy(random.choice(empty), random.choice([2, 4]))
        	is_move = False

run()