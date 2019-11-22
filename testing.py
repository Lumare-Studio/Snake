from engine.WindowManager import *

testing_file = open("Testing", "r")
print(testing_file.read())
print(3.5 >= 0)


def on_honor_roll(gpa):
    if gpa >= 3.5:
        return True
    elif 2.0 <= gpa < 3.5:
        return "Keep fighting!"  # This is super duper Giao
    else:
        return False


print(on_honor_roll(3.8))
print(on_honor_roll(3.1))
print(on_honor_roll(1.8))


a = WindowManager("Testing", 500, 500)
c = a.get_canvas()
r = c.create_rectangle(0, 0, 30, 30, fill="red")
c.pack()
a.show_window()

