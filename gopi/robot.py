import time
import gopigo_client


robot_debug = True
robot_speed = 100


def pause(t=0.5):
    if t > 5.0:
        duration = 5.0
    elif t < .2:
        duration = .2
    else:
        duration = t
    print('sleep = ', duration)
    time.sleep(duration)


def forward(duration=0.5):
    print('robot_controller, forward, robot_debug =', robot_debug)
    if not robot_debug:
        gopigo_client.set_speed(robot_speed)
        gopigo_client.set_left_speed(robot_speed+5)
        gopigo_client.stop()
        gopigo_client.fwd()
        pause(duration)
        gopigo_client.stop()


def backward(duration=0.5):
    print('robot_controller, backward, robot_debug =', robot_debug)
    if not robot_debug:
        gopigo_client.set_speed(robot_speed)
        gopigo_client.stop()
        gopigo_client.bwd()
        pause(duration)
        gopigo_client.stop()


def left(duration=0.5):
    print('robot_controller, left, robot_debug =', robot_debug)
    if not robot_debug:
        gopigo_client.set_speed(robot_speed)
        gopigo_client.stop()
        gopigo_client.left()
        pause(duration)
        gopigo_client.stop()


def left_rot(duration=0.5):
    print('robot_controller, left_rot, robot_debug =', robot_debug)
    if not robot_debug:
        gopigo_client.set_speed(robot_speed)
        gopigo_client.stop()
        gopigo_client.left_rot()
        pause(duration)
        gopigo_client.stop()


def right(duration=0.5):
    print('robot_controller, right, robot_debug =', robot_debug)
    if not robot_debug:
        gopigo_client.set_speed(robot_speed)
        gopigo_client.stop()
        gopigo_client.right()
        pause(duration)
        gopigo_client.stop()


def right_rot(duration=0.5):
    print('robot_controller, right_rot, robot_debug =', robot_debug)
    if not robot_debug:
        gopigo_client.set_speed(robot_speed)
        gopigo_client.stop()
        gopigo_client.right_rot()
        pause(duration)
        gopigo_client.stop()


def stop(duration=0.5):
    print('robot_controller, stop, robot_debug =', robot_debug)
    if not robot_debug:
        gopigo_client.set_speed(robot_speed)
        gopigo_client.stop()
        pause(duration)


def distance():
    print('robot_controller, distance, robot_debug =', robot_debug)
    d = 0
    if not robot_debug:
        d = gopigo_client.us_dist(0)
        print('robot_controller, distance =', d)
    return d


def blink(times=5):
    times = times if times < 10 else 5
    print('robot_controller, blink, robot_debug =', robot_debug)
    if not robot_debug:
        for i in range(times):
            gopigo_client.led_on(0)
            gopigo_client.led_on(1)
            gopigo_client.led_off(0)
            gopigo_client.led_off(1)


def volt():
    print('robot_controller, volt, robot_debug =', robot_debug)
    v = 0
    if not robot_debug:
        v = gopigo_client.volt()
        print('robot_controller, volt =', v)
    return v


def servo(position):
    print('robot_controller, servo, robot_debug =', robot_debug)
    position = position if 0 <= position <= 180 else 90
    if not robot_debug:
        gopigo_client.servo(position)


if __name__ == '__main__':
    robot_debug = False
    left(.5)
    right(1)
    forward(2)
    stop()
    backward(10)
    distance()

