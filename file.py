

def startree_with_while_loop():
    height = int(input("Enter the height of the tree:\n"))
    i = 0
    while i < height:
        print(" " * (height - i - 1) + "*" * (2 * i + 1))
        i += 1
        
def startree_with_while_loop_and_trunk():
    height = int(input("Enter the height of the tree:\n"))
    i = 0
    while i < height:
        print(" " * (height - i - 1) + "*" * (2 * i + 1))
        i += 1
    trunk_height = height // 3
    trunk_width = height // 3
    j = 0
    while j < trunk_height:
        print(" " * (height - trunk_width // 2 - 1) + "*" * trunk_width)
        j += 1


def square_with_while_loop():
    size = int(input("Enter the size of the square:\n"))
    i = 0
    while i < size:
        print("*" * size)
        i += 1
        
        
def triangle_with_while_loop():
    height = int(input("Enter the height of the triangle:\n"))
    i = 0
    while i < height:
        print(" " * (height - i - 1) + "*" * (2 * i + 1))
        i += 1  
        
triangle_with_while_loop()

def triangle_with_inner_hole_and_while_loop():
    height = int(input("Enter the height of the triangle:\n"))
    i = 0
    while i < height:
        if i == 0:
            print(" " * (height - i - 1) + "*" * (2 * i + 1))
        else:
            print(" " * (height - i - 1) + "*" + " " * (2 * i - 1) + "*")
        i += 1
        
