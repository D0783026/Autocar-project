import socket
import pygame
'''
# define HOST POST
HOST = '172.20.10.4'
PORT = 9090

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((HOST, PORT))'''

#Initialize pygame
pygame.init()

# Used to manage how fast the screen updates
clock = pygame.time.Clock()

# Initialize the joysticks
pygame.joystick.init()

# -------- Main Program Loop -----------
while True:
    # EVENT PROCESSING STEP
    for event in pygame.event.get():  # User did something
        # Possible joystick actions: JOYAXISMOTION JOYBALLMOTION JOYBUTTONDOWN JOYBUTTONUP JOYHATMOTION
        if event.type == pygame.JOYBUTTONDOWN:
            print("Joystick button pressed.")
        if event.type == pygame.JOYBUTTONUP:
            print("Joystick button released.")
        if event.type == pygame.JOYAXISMOTION:
            if joystick.get_axis(1) <= -0.5:
                print("upupupup!!!")
            if joystick.get_axis(1) >= 0.5:
                print("downdown!!!")
            if joystick.get_axis(0) <= -0.5:
                print("leftleft!!!")
            if joystick.get_axis(0) >= 0.5:
                print("rightright!")

    # Get count of joysticks
    joystick_count = pygame.joystick.get_count()

    # For each joystick:
    
    for i in range(joystick_count):
        joystick = pygame.joystick.Joystick(i)
        joystick.init()
        
    # SENDING DATA
    cmd2 = str(joystick.get_axis(1)) #control forward and backward
    cmd2 = cmd2[0:4]
    print('cmd2 : ' + cmd2)
    if cmd2 == '0.0':
        cmd2 = cmd2 + '0'

    cmd1 = str(joystick.get_axis(0)) #control left and right
    cmd1 = cmd1[0:4]
    if cmd1 == '0.0':
        cmd1 = cmd1 + '0'

    cmd3 = str(joystick.get_axis(2))
    cmd3 = cmd3[0:4]
    if cmd3 == '0.0':
            cmd3 = cmd3 + '0'

    cmd4 = str(joystick.get_axis(3))
    cmd4 = cmd4[0:4]
    if cmd4 == '0.0':
            cmd4 = cmd4 + '0'


    cmd = cmd1 + cmd2 + cmd3 + cmd4
    print(cmd1 + '|' + cmd2 + '|' + cmd3 + '|' + cmd4 )
    print('cmd : ' + cmd)
    #s.send(cmd.encode())


    # ALL CODE TO DRAW SHOULD GO ABOVE THIS COMMENT

    # Limit to 20 frames per second
    clock.tick(20)