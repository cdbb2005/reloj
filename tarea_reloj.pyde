vertical_position_1 = 0
vertical_position_2 = 0
vertical_position_3 = 0


def setup():
    size(300, 500)
    
def draw():
    global vertical_position_1
    global vertical_position_2
    global vertical_position_3
    
    background(255)
    fill(map(second(), 0, 59, 255, 0))
    fill(map(minute(), 0, 59, 255, 0))
    fill(map(hour(), 0, 59, 255, 0))
    
    ellipse(width / 6, vertical_position_1, 40, 40)
    
    if vertical_position_1 > height:
        vertical_position_1 = 0
    else:
        vertical_position_1 = map(second(), 0, 59, 0, height)
        
    
    ellipse(width / 2, vertical_position_2, 40, 40)
    
    if vertical_position_2 > height:
        vertical_position_2 = 0
    else:
        vertical_position_2 = map(minute(), 0, 59, 0, height)
        
    
    ellipse(width / 1.2, vertical_position_3, 40, 40)
    
    if vertical_position_3 > height:
        vertical_position_3 = 0
    else:
        vertical_position_3 = map(hour(), 0, 24, 0, height)
