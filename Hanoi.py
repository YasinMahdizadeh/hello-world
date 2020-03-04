def Hanoi(tower, now, goal, idle):
    if tower > 1:
        
        Hanoi(tower-1, now, idle, goal)
        print(tower, "From", now, "to", goal)
        Hanoi(tower-1,idle, goal, now)
    
    if tower == 1:
        print(tower, "From", now, "to", goal)

Hanoi(3,'A','B','C')   
