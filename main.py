import os
from math import sin, cos
from numpy import arange

def donut(sizeOfDonut, speedX, speedY):
    rotX, rotY = 0, 0
    #clear screen on any terminal OS
    os.system('cls' if os.name == 'nt' else 'clear')
    while True:
        #Fill z[] and b[] with empty data
        z = [0] * 1760
        b = [chr(32)] * 1760
        for j in arange(0, 6.28, 0.07):
            for i in arange(0, 6.28, 0.02):
                c = sin(i)
                d = cos(j)
                e = sin(rotX)
                f = sin(j)
                g = cos(rotX)
                h = d + 2
                #Define the size of donut
                D = 1 * sizeOfDonut / (c * h * e + f * g + 5)
                l = cos(i)
                m = cos(rotY)
                n = sin(rotY)
                t = c * h * g - f * e
                x = int(40 + 30 * D * (l * h * m - t * n))
                y = int(12 + 15 * D * (l * h * n + t * m))
                o = x + 80 * y
                N = int(8 * ((f * e - c * d * g) * m - c * d * e - f * g - l * d * n))
                #Rendering Luminance
                if 22 > y > 0 and 0 < x < 80 and D > z[int(o)]:
                    z[int(o)] = D
                    b[int(o)] = ".,-~:;=!*#$@"[N if N > 0 else 0] #.,-~:;=!*#$@

        # clear screen on any terminal OS every frame
        os.system('cls' if os.name == 'nt' else 'clear')
        for k in range(0, 1761):
            #Print character on screen
            print(b[k] if k % 80 != 0 else chr(10), end="")
            #Speed for rotation
            rotX += 0.00001 * speedX
            rotY += 0.00001 * speedY

if __name__ == '__main__':
    donut(float(input("Enter the size of a donut: ")), float(input("Enter the rotation X of a donut: ")), float(input("Enter the rotation Y of a donut: ")))
