# import necessary modules
import math
import os

# clear the terminal screen
os.system('cls')

# define the function to generate the donut
def donut():
    
    # define the characters to be used to draw the donut
    chars = ['.', ',', '-', '~', ':', ';', '=', '!', '*', '#', '$', '@']
    
    # create arrays of sine and cosine values for performance optimization
    sinn = [math.sin(i) for i in range(628)]
    cosn = [math.cos(i) for i in range(628)]
    
    # initialize arrays for the z-buffer and character buffer
    z = [0] * 1760
    b = [' '] * 1760
    
    # iterate over the horizontal and vertical angles of the donut
    for j in range(0, 628, 7):
        for i in range(0, 628, 2):
            # calculate sine and cosine values for the current angles
            cosj = cosn[j]
            sini = sinn[i]
            sinj = sinn[j]
            cosi = cosn[i]
            
            # calculate values based on the formula for a donut
            cosj2 = cosj + 2
            mess = 1 / (sini * cosj2 * math.sin(A) + sinj * math.cos(A) + 5)
            t = sini * cosj2 * math.cos(A) - sinj * math.sin(A)
            x = int(40 + 30 * mess * (cosi * cosj2 * math.cos(B) - t * math.sin(B)))
            y = int(11 + 15 * mess * (cosi * cosj2 * math.sin(B) + t * math.cos(B)))
            o = x + 80 * y
            N = int(8 * ((sinj * math.sin(A) - sini * cosj * math.cos(A)) * math.cos(B) - sini * cosj * math.sin(A) - sinj * math.cos(A) - cosi * cosj * math.sin(B)))
            
            # update the z-buffer and character buffer if the new value is closer to the viewer
            if y < 22 and y > 0 and x < 80 and x > 0 and mess > z[o]:
                z[o] = mess
                b[o] = chars[N if N > 0 else 0]
    
    # print the character buffer to the terminal screen and return the updated angle values
    print("\033[0;0H" + "".join(b))
    return A + 0.12, B + 0.10

# initialize the horizontal and vertical angles
A = 0
B = 0

# animate the donut by repeatedly calling the donut() function
while True:
    A, B = donut()
