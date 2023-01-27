def turn_right():
    turn_left()
    turn_left()
    turn_left()
   
def jump():
    move()
    turn_left()
    move()
    turn_right()
    move()
    turn_right()
    move()
    turn_left()

number_of_hardles = 6
while number_of_hardles > 0:
    jump()
    if number_of_hardles == 1:
        break
    
    number_of_hardles -= 1