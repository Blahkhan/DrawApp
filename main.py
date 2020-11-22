import pyautogui, time, math

def square():
    print("After 5 seconds, a spirala be driven")
    time.sleep(5)
    distance = 200
    while distance > 0:
        pyautogui.drag(distance, 0, duration=0.5)   # move right
        distance -= 5
        pyautogui.drag(0, distance, duration=0.5)   # move down
        pyautogui.drag(-distance, 0, duration=0.5)  # move left
        distance -= 5
        pyautogui.drag(0, -distance, duration=0.5)  # move up

def circle():
    print("After 5 seconds, a okrąg be driven")
    print("You must hold left mouse button!!!")
    time.sleep(5)
    # Radius
    R = 150
    # measuring screen size
    (x,y) = pyautogui.size()
    # locating center of the screen
    (X,Y) = pyautogui.position(x/2,y/2)
    # offsetting by radius
    pyautogui.moveTo(X+R,Y)

    for i in range(360):
        # setting pace with a modulus
        if i%6==0:
            pyautogui.moveTo(X+R*math.cos(math.radians(i)),Y+R*math.sin(math.radians(i)))






print("Welecome to python driver 3000")
print("Type 1 for Spirala, 2 for Okrąg")
type = input()
if type == "1":
    square()
elif type == "2":
    circle()
