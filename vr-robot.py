num_1 = 0

def when_started1():
    global num_1
    num_1 = 1750
    while True:
        num_1 = num_1 + -50
        pen.set_pen_color(GREEN)
        pen.move(DOWN)
        drivetrain.drive_for(FORWARD, num_1, MM)
        drivetrain.turn_for(RIGHT, 90, DEGREES)
        drivetrain.drive_for(FORWARD, num_1, MM)
        drivetrain.turn_for(RIGHT, 90, DEGREES)
        drivetrain.drive_for(FORWARD, num_1, MM)
        drivetrain.turn_for(RIGHT, 90, DEGREES)
        drivetrain.drive_for(FORWARD, num_1, MM)
        drivetrain.turn_for(RIGHT, 90, DEGREES)

vr_thread(when_started1)
