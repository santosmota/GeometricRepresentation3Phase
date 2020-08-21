import tkinter as tk
from tkinter import filedialog
import csv
#from mpl_toolkits.mplot3d import axes3d
import matplotlib.pyplot as plt
import numpy as np
from matplotlib.animation import FuncAnimation
from numpy import genfromtxt

###############################################################
# open file
###############################################################
root = tk.Tk()
root.withdraw()
file_path = filedialog.askopenfilename()

if file_path is None:
    print('File not chosen.')
    quit()
else:
    dadostranspostos = genfromtxt(file_path, delimiter='\t')
    #with open(file_path, newline='') as csvfile:
    #    dados = csv.DictReader(csvfile)
        #data = list(csv.reader(csvfile))
    #    for row in dados:
    #        print(row)
        #    print(row['time'], row['Va'], row['Vb'], row['Vc'])
    dados = np.transpose(dadostranspostos)

#print(dados[0])

##################################################
# Constants and figures
##################################################
fig = plt.figure(figsize=plt.figaspect(0.45))
abcscalars1 = fig.add_subplot(1,2,1)
abcspace = fig.add_subplot(1,2,2, projection='3d')

##################################################
# Plotting mains voltages
##################################################
abcscalars1.plot(dados[0], dados[1], color='red', label='va')
abcscalars1.plot(dados[0], dados[2], color='darkgreen', label='vb')
abcscalars1.plot(dados[0], dados[3], color='blue', label='vc')

abcscalars1.plot(dados[0], dados[4], color='red', linestyle='dotted', label='PLLa')
abcscalars1.plot(dados[0], dados[5], color='darkgreen', linestyle='dotted', label='PLLb')
abcscalars1.plot(dados[0], dados[6], color='blue', linestyle='dotted', label='PLLc')

##################################################
# Settings of abc scalars chart
##################################################
#abcscalars1.set_xlim([0.00, 2*np.pi])
abcscalars1.set_xlim([0.09, 0.14])
abcscalars1.set_ylim([-1.5, 1.5])
#abcscalars1.set_xlabel('angle')
#abcscalars1.set_xlabel('time (rad)')
abcscalars1.set_xlabel('time (s)')
abcscalars1.set_ylabel('mains')
abcscalars1.grid(False)
#abcscalars1.set_xticks([])
#abcscalars1.set_yticks([])
#abcscalars1.set_zticks([])

##################################################
# Settings of abc space chart
##################################################
#abcspace.view_init(azim=-45, elev=20)
abcspace.view_init(azim=45, elev=35.26) #top view from zero sequence line
abcspace.set_proj_type('ortho')
abcspace.set_xlim([-1,1])
abcspace.set_ylim([-1,1])
abcspace.set_zlim([-1,1])
#abcspace.set_xlabel('a')
#abcspace.set_ylabel('b')
#abcspace.set_zlabel('c')
abcspace.set_xticks([])
abcspace.set_yticks([])
abcspace.set_zticks([])
abcspace.set_axis_off()
#abcspace.xaxis.set_pane_color((1.0, 1.0, 1.0, 0.0))#use if only the background is to be white
#abcspace.yaxis.set_pane_color((1.0, 1.0, 1.0, 0.0))
#abcspace.zaxis.set_pane_color((1.0, 1.0, 1.0, 0.0))
##################################################
# Plotting Balanced Plane
##################################################
balancedplaneamplitude = 0
nsampbalplane = 361
anglesoneturn = np.linspace(start=0, stop=2*np.pi, num=nsampbalplane, endpoint=True)
if balancedplaneamplitude > 0:
    balancedplanecircle = np.zeros((3, nsampbalplane))
    balancedplanecirclephaseshift = np.array([0, -2 * np.pi / 3, 2 * np.pi / 3])
    for numphase in range (0, 3):
        balancedplanecircle[numphase, :] = (balancedplaneamplitude
                                            * np.cos(anglesoneturn + balancedplanecirclephaseshift[numphase]))
    abcspace.plot(balancedplanecircle[0, :],
                  balancedplanecircle[1, :],
                  balancedplanecircle[2, :],
                  color='blue',
                  linewidth=0.5)

    balancedplanelines = np.ones((3, 50))
    anglestep = 10
    for i in range(0,10,1):
        for numphase in range(0, 3, 1):
            balancedplanelines[numphase, i * 5] = balancedplanecircle[numphase, anglestep * i]
        for numphase in range(0, 3, 1):
            balancedplanelines[numphase, i * 5 + 1] = balancedplanecircle[numphase, 180 - anglestep * i]
        for numphase in range(0, 3, 1):
            balancedplanelines[numphase, i * 5 + 2] = balancedplanecircle[numphase, 180 + anglestep * i]
        for numphase in range(0, 3, 1):
            balancedplanelines[numphase, i * 5 + 3] = balancedplanecircle[numphase, 360 - anglestep * i]
        for numphase in range(0, 3, 1):
            balancedplanelines[numphase, i * 5 + 4] = balancedplanecircle[numphase, anglestep * i]
    abcspace.plot(balancedplanelines[0, :],
                  balancedplanelines[1, :],
                  balancedplanelines[2, :],
                      color='blue', label='a+b+c=0 plane',
                      linewidth=0.5)

##################################################
# Plotting a b c base vectors
##################################################
showabcbases = True
baselength = 1
#quiverpivot = 'middle'
quiverpivot = 'tail'
if showabcbases:
    abcspace.quiver(0, 0, 0, 1, 0, 0, length=baselength,
                    pivot=quiverpivot, arrow_length_ratio=0.025,
                    linewidth=1, linestyle='dotted',
                    color='black')
    abcspace.quiver(0, 0, 0, 0, 1, 0, length=baselength,
                    pivot=quiverpivot, arrow_length_ratio=0.025,
                    linewidth=1, linestyle='dotted',
                    color='black')
    abcspace.quiver(0, 0, 0, 0, 0, 1, length=baselength,
                    pivot=quiverpivot, arrow_length_ratio=0.025,
                    linewidth=1, linestyle='dotted',
                    color='black')
    abcspace.text(baselength/2, 0, 0, 'a', (0, 1, 0))
    abcspace.text(0, baselength/2, 0, 'b', (0, 1, 0))
    abcspace.text(0, 0, baselength/2, 'c', (0, 1, 0))

##################################################
# Plotting a b c in scalargraph + abcspace + timeslide
##################################################
mainsquiver = abcspace.quiver([0], [0], [0], dados[1, 100], dados[2, 100], dados[3, 100], arrow_length_ratio=0.1,
                              color='black', label='mains')

pllquiver = abcspace.quiver([0], [0], [0], dados[4, 100], dados[5, 100], dados[6, 100], arrow_length_ratio=0.1,
                              color='magenta', label='pll')

#aquiver = abcspace.quiver(0, 0, 0, 1, 0, 0, length=1,
#                          pivot='tail', arrow_length_ratio=0.2, color='red')
#bquiver = abcspace.quiver(0, 0, 0, 0, 1, 0, length=-0.5,
#                          pivot='tail', arrow_length_ratio=0.2, color='green')
#cquiver = abcspace.quiver(0, 0, 0, 0, 0, 1, length=-0.5,
#                          pivot='tail', arrow_length_ratio=0.2,
#                          color='blue')

timeslide, = abcscalars1.plot([0,0], [-2,2], color='black', linestyle='dashed')

##################################################
# Plotting a b c path
##################################################
#pathquiver = abcspace.plot(dados[1, 0:10], dados[2, 0:10], dados[3, 0:10],
#                           color='black', linestyle='dotted', linewidth=0.5)
pathquiver = abcspace.plot(dados[1,:], dados[2,:], dados[3,:],
                           color='black', linestyle='dotted', linewidth=0.5)


##################################################
# Plotting a b c legends
##################################################
abcspace.legend()
abcscalars1.legend(loc='lower right')

rotate3dspace = False
cadaumporsi = 0
showmainsquiver = True

def update(i):
    global mainsquiver, pllquiver
    global timeslide
    global pathquiver
    global aquiver, bquiver, cquiver

    timeslide.remove()

    if showmainsquiver:
        mainsquiver.remove()
        pllquiver.remove()
        mainsquiver = abcspace.quiver([0], [0], [0], dados[1, i], dados[2, i], dados[3, i], arrow_length_ratio=0.1,
                                      color='black')
        pllquiver = abcspace.quiver([0], [0], [0], dados[4, i], dados[5, i], dados[6, i], arrow_length_ratio=0.1,
                                      color='magenta')

    if cadaumporsi == 1:
        aquiver.remove()
        bquiver.remove()
        cquiver.remove()
        aquiver = abcspace.quiver(0, 0, 0, 1, 0, 0, length=dados[1, i],
                                  pivot='tail', arrow_length_ratio=0.2, color='red')
        bquiver = abcspace.quiver(0, 0, 0, 0, 1, 0, length=dados[2, i],
                                  pivot='tail', arrow_length_ratio=0.2, color='green')
        cquiver = abcspace.quiver(0, 0, 0, 0, 0, 1, length=dados[3, i],
                                  pivot='tail', arrow_length_ratio=0.2,
                                  color='blue')
    if cadaumporsi == 2:
        aquiver.remove()
        bquiver.remove()
        cquiver.remove()
        aquiver = abcspace.quiver(0, 0, 0, 1, 0, 0, length=dados[1, i],
                                  pivot='tail', arrow_length_ratio=0.2, color='red')
        bquiver = abcspace.quiver(dados[1, i], 0, 0, 0, 1, 0, length=dados[2, i],
                                  pivot='tail', arrow_length_ratio=0.2, color='green')
        cquiver = abcspace.quiver(dados[1, i], dados[2, i], 0, 0, 0, 1, length=dados[3, i],
                                  pivot='tail', arrow_length_ratio=0.2,
                                  color='blue')

    timeslide, = abcscalars1.plot([dados[0, i], dados[0, i]],
                                  [-2, 2],
                                  color='black', linestyle='dashed')
    #if i>2:
    #    pathquiver = abcspace.plot(dados[1, 0:i], dados[2, 0:i], dados[3, 0:i],
    #                               color='black', linewidth=1)

    if rotate3dspace:
        deltaelevconstant = -45
        deltaelevdangle = -2*deltaelevconstant/180
        if i < 180:
            abcspace.view_init(azim=45, elev=deltaelevdangle * i + deltaelevconstant)
        else:
            abcspace.view_init(azim=45, elev=-deltaelevdangle * (i - 180) - deltaelevconstant)

animacao = FuncAnimation(fig, update, frames=len(dados[0]), interval=10)
plt.show()