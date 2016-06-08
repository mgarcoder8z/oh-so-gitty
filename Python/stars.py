def draw_stars(alist):
    for item in alist:
        if(type(item) == int):
            print('*' * item)
        elif(type(item) == str):
            print(item[0].lower() * len(item))
draw_stars([2,4,"Harry",1,7,"Ron","Hermione"])
