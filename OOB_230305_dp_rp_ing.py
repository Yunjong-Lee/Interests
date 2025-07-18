### Libraries import
''' Common '''
import os
import time
import numpy as np
import struct
import sys


''' for serial communication ''' 
import serial
import OOB_230305_dp_rm_ing_SerialComm as SERIALCOMM
import serial.tools.list_ports


''' for mmWave parser '''
import OOB_230305_dp_rm_ing_Parser as _PARSER_


''' for heatmap '''
# %matplotlib tk
import matplotlib.pyplot as plt
# import seaborn as sns


''' 23.02.21 
# For graph control '''
# ## 2D plot
import pyqtgraph as pg
from pyqtgraph.Qt import QtGui
from PyQt5 import QtWidgets

# ## 3D plot
from mpl_toolkits.mplot3d import Axes3D


OPTION_HEATMAP = True
OPTION_DETECTEDPOINT_CLOUD = True
OPTION_RANGE_PROFILE = True


''' Configuration file name '''
configFileName = '_xwr68xx_230227_dp_rp_hm.cfg'

CLIport = {}
Dataport = {}

num_of_zones = 8
numRangeBins = 64
numAngleBins = 48


rNa = np.zeros((64, 48)) # [0]*(numRangeBins * numAngleBins)

rates = [0]*num_of_zones
avgPwrs = [0]*num_of_zones
rIdxs = [0]*num_of_zones
aIdxs = [0]*num_of_zones


def Plot_init(win):
    # app = QtGui.QApplication([])
    # # plot detected point
    p_dP = win.addPlot()
    
    # Set the plot 
    p_dP.setXRange(-5,5)
    p_dP.setYRange(-1,10)
    p_dP.setLabel('left', text = 'Y position (m)')
    p_dP.setLabel('bottom', text= 'X position (m)')

    # # plot range profile
    p_rP = win.addPlot()
    
    # Set the plot 
    p_rP.setXRange(1,256)
    p_rP.setYRange(20,120)
    p_rP.setLabel('left', text = 'Peak Value (?)')
    p_rP.setLabel('bottom', text= 'RF Range ()')
    
    return p_dP, p_rP



def update_heatMap(rNa):    
    if OPTION_HEATMAP:
        # rNa = np.random.normal(size=(64, 48)) # test data
        img.setImage(rNa)
        view_box.addItem(img)


def update(): 
    global rNa, rates, avgPwrs, rIdxs, aIdxs
    
    _PARSER_.parser_mmWave(Dataport, configParameters, s, s_rp) # headerBuf, payloadBuf = _PARSER_.parser_mmWave(Dataport, configParameters, s)

    if OPTION_HEATMAP: 
        img.setImage(rNa)
        view_box.addItem(img)
        win.show()
        
    return rNa, rates, avgPwrs, rIdxs, aIdxs


def getSerialPort():
    port_C = 'COM7'
    port_D = 'COM8'
    
#     ports_ = serial.tools.list_ports.comports()
#     
#     for port in ports_:
#         desc = port.description
#         
#         if desc.find('Silicon Labs Dual CP2105 USB to UART Bridge: Standard COM Port') == 0:
#             # data port mapping
#             port_D = port.device
#             
#         if desc.find('Silicon Labs Dual CP2105 USB to UART Bridge: Enhanced COM Port') == 0:
#             # control port mapping
#             port_C = port.device
            
    return port_C, port_D


# global Variables
gBuf = bytes(0)

app = QtWidgets.QApplication(sys.argv)

# pg.setConfigOption(antialias=True)
pg.setConfigOptions(antialias=True)

win = pg.GraphicsLayoutWidget()
win.setWindowTitle(u'Radar Output')
win.resize(1000,600)

if OPTION_HEATMAP:
    # The plotting
    img = pg.ImageItem()
    # img.setImage(data)

    view_box = pg.ViewBox()
    # view_box.addItem(img)

    plot = pg.PlotItem(viewBox=view_box)
    win.addItem(plot)
    
win.show()

detected_point_P, range_profile_P = Plot_init(win)

s = detected_point_P.plot([],[],pen=None,symbol='o')
s_rp = range_profile_P.plot([],[], symbol='t1') # pen=(200,200,200), symbolBrush=(255,0,0), symbolPen='w')

Cport, Dport = getSerialPort()

# Configurate the serial port
CLIport, Dataport = SERIALCOMM.serialConfig(configFileName, Cport, Dport)

# Get the configuration parameters from the configuration file
configParameters = SERIALCOMM.parseConfigFile(configFileName)
# plt.show()

while True:
    try:
        # Update the data and check if the data is okay
        ra_hMap, rates, avgPwrs, rIdxs, aIdxs = update()
        update_heatMap(ra_hMap)
        
        time.sleep(0.1)

    except KeyboardInterrupt:
        CLIport.write(('sensorStop\n').encode())
        print('sensorStop\n')
        
        CLIport.close()
        if CLIport.isOpen():
            print('CLI port is open.')
            CLIport.close()
                            
        Dataport.close()
        if Dataport.isOpen():
            print('Data port is open.')
            Dataport.close()
                            
        break
