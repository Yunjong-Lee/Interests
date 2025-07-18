
###
### Generation : 2022.12.15 
###

import serial
import time
import numpy as np
import struct
import pyqtgraph as pg
from pyqtgraph.Qt import QtGui
from sklearn.cluster import dbscan
import pandas



def serialConfig(configFileName, control_port, data_port):
    global CLIport
    global Dataport
    
    CLIport = serial.Serial(control_port, 115200) # serial.Serial('COM7', 115200)
    Dataport = serial.Serial(data_port, 921600) # serial.Serial('COM8', 921600)
    
    config = [line.rstrip('\r\n') for line in open(configFileName)]
    
    for i in config:
        print(i)
        CLIport.write((i + '\n').encode())
        # CLIport.write(('Done\n').encode())
        
        time.sleep(0.03)
    
    return CLIport, Dataport



def parseConfigFile(configFileName):
    configParameters = {}
    config = [line.rstrip('\r\n') for line in open(configFileName)]
    
    for i in config:
        splitWords = i.split(" ")
        numRxAnt = 4
        numTxAnt = 3
        
        if "profileCfg" in splitWords[0]:
            startFreq = int(float(splitWords[2]))
            print('--- startFreq :', startFreq)
            idleTime = int(splitWords[3])
            print('--- idleTime :', idleTime)
            rampEndTime = float(splitWords[5])
            print('--- rampEndTime :', rampEndTime)
            freqSlopeConst = float(splitWords[8])
            print('--- freqSlopeConst :', freqSlopeConst)
            numAdcSamples = int(splitWords[10])
            print('--- numAdcSamples :', numAdcSamples)
            numAdcSamplesRoundTo2 = 1

            while numAdcSamples > numAdcSamplesRoundTo2:
                numAdcSamplesRoundTo2 = numAdcSamplesRoundTo2 * 2
            print('--- numAdcSamplesRoundTo2 :', numAdcSamplesRoundTo2)
            digOutSampleRate = int(splitWords[11])
            print('--- digOutSampleRate :', digOutSampleRate)
        elif "frameCfg" in splitWords[0]:
            chirpStartIdx = int(splitWords[1])
            print('--- chirpStartIdx :', chirpStartIdx)
            chirpEndIdx = int(splitWords[2])
            print('--- chirpEndIdx :', chirpEndIdx)
            numLoops = int(splitWords[3])
            print('--- numLoops :', numLoops)
            numFrames = int(splitWords[4])
            print('--- numFrames :', numFrames)
            framePeriodicity = float(splitWords[5])
            print('--- framePeriodicity :', framePeriodicity)
        elif "vitalSignsCfg" in splitWords[0]:
            rangeStart = float(splitWords[1])
            print('--- rangeStart :', rangeStart)
            rangeEnd = float(splitWords[2])
            print('--- rangeEnd :', rangeEnd)
            
    numChirpsPerFrame = (chirpEndIdx - chirpStartIdx + 1) * numLoops
    print('--- numChirpsPerFrame :', numChirpsPerFrame)
    
    configParameters["numDopplerBins"] = numChirpsPerFrame / numTxAnt
    configParameters["numRangeBins"] = numAdcSamplesRoundTo2
    configParameters["rangeResolutionMeters"] = (3e8 * digOutSampleRate * 1e3) / (2 * freqSlopeConst * 1e12 * numAdcSamples)
    configParameters["rangeIdxToMeters"] = (3e8 * digOutSampleRate * 1e3) / (2 * freqSlopeConst * 1e12 * configParameters["numRangeBins"])
    configParameters["dopplerResolutionMps"] = 3e8 / (2 * startFreq * 1e9 * (idleTime + rampEndTime) * 1e-6 * configParameters["numDopplerBins"] * numTxAnt)
    
    # configParameters["maxRange"] = (300 * 0.9 * digOutSampleRate) / (2 * freqSlopeConst * 1e3)
    # configParameters["maxVelocity"] = 3e8 / (4 * startFreq * 1e9 * (idleTime + rampEndTime) * 1e-6 * numTxAnt)
    # configParameters["rangeStart"] = rangeStart
    # configParameters["rangeEnd"] = rangeEnd
       
    return configParameters

