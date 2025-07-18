###
### Generation : 2022.12.15 
###


# import libraries
import struct
import numpy as np

# # global variables
#from OOB_221226 import s
# global s

''' 23.02.21 
# For graph control '''
# ## 2D plot
import pyqtgraph as pg
from pyqtgraph.Qt import QtGui
# import _230225_draw_plot_func as dp

# ## 3D plot
from mpl_toolkits.mplot3d import Axes3D


### - - - Capturing.
import time
import datetime as Dtime
record = False    
# fourcc = cv2.VideoWriter_fourcc(*'XVID')
ctime_stamp = Dtime.datetime.now().strftime("_%y%m%d_%H%M%S%M")

### - - - Logging.
# w_display = open('D:/'+str(now)+'_display.log', 'w')
w_radar = open('D:/anacondaDir/_06_OOB/logging_raw_data/'+str(ctime_stamp)+'_radar.log', 'w')

# ### variables
# global gBuf
gBuf = bytes(0)


# ### Constants
num_of_zones = 8
numRangeBins = 64
numAngleBins = 48


''' 2023.02.21
# # Defined TLV's '''
MMWDEMO_OUTPUT_MSG_DETECTED_POINTS                      = 1
MMWDEMO_OUTPUT_MSG_RANGE_PROFILE                        = 2
MMWDEMO_OUTPUT_MSG_NOISE_PROFILE                        = 3
MMWDEMO_OUTPUT_MSG_AZIMUT_STATIC_HEAT_MAP               = 4
MMWDEMO_OUTPUT_MSG_RANGE_DOPPLER_HEAT_MAP               = 5
MMWDEMO_OUTPUT_MSG_STATS                                = 6
MMWDEMO_OUTPUT_MSG_DETECTED_POINTS_SIDE_INFO            = 7
MMWDEMO_OUTPUT_MSG_AZIMUT_ELEVATION_STATIC_HEAT_MAP     = 8
MMWDEMO_OUTPUT_MSG_TEMPERATURE_STATS                    = 9


# rangeAzimuth = [0]*(numRangeBins * numAngleBins)
rates = [0]*num_of_zones
avgPwrs = [0]*num_of_zones
rIdxs = [0]*num_of_zones
aIdxs = [0]*num_of_zones    


num_x = 0
num_y = 1
num_z = 2
num_doppler = 3


# ''' 2023.02.23
# # # '''
# def get_pos(pos):
#     x, y, z, doppler = [], [], [], []
#    
#     for a_list in pos:
#         x.append(a_list[num_x])
#         y.append(a_list[num_y])
#         z.append(a_list[num_z])
#         doppler.append(a_list[num_doppler])
#        
#     return x, y, z, doppler


# ### Function : Graphic user interface
''' 2023.02.21 
# # '''
def draw_plot(s, outputDict, s_rp, rp_Value):
    x, y, z, doppler = [], [], [], []
    # xmin, xmax, ymin, ymax, zmin, zmax = -5, 5, 0, 5, -2, 2
    
    if outputDict:
        pos = outputDict.get('pointCloud')

        for a_list in pos:
            x.append(a_list[num_x])
            y.append(a_list[num_y])
            z.append(a_list[num_z])
            doppler.append(a_list[num_doppler])

        s.setData(x,y)
    
    range_, index_ = [],[]

    if all(rp_Value):
        for i in range(len(rp_Value)):
            range_.append(rp_Value[i][0])
            index_.append(i)

        s_rp.setData(index_,range_)
    
    QtGui.QApplication.processEvents()
    
    
''' 2023.02.21
# # '''
def split_data(data):
    start_index, data_len = findStart(data)
    end_index = start_index + [data_len]
    
    data_lists = [0 for i in range(len(start_index))]
    
    for j in range(len(start_index)):
        if end_index[-1]:
            data_lists[j] = data[start_index[j] : end_index[j+1]]

    return data_lists


''' 2023.02.21
# ### Function : find magic word
# #     - data : binary data
# #
# #   return   : index, size of data '''
def findStart(data):
    index = list()
    i = -1
    magic_word: bytes = b'\x02\x01\x04\x03\x06\x05\x08\x07'

    while True:
        i = data.find(magic_word, i+1)
        if i == -1:
            break
        
        index.append(i)
    
    return index, len(data)

''' 2023.02.21
# ### Function : Conversion binary to single 
# #     - data : binary data
# #     - idx  : start address of binary data
# #     - size : size of binary data 
# # 
# #   return   : translated data (integer type) '''
def getbinary_to_single(data, idx, size):
    return int.from_bytes(data[idx:idx+size], byteorder='little')


''' 2023.02.21
# ### Function : Header parser
#
# file:///C:/ti/mmwave_sdk_03_01_01_02/packages/ti/demo/xwr68xx/mmw/docs/doxygen/html/struct_mmw_demo__output__message__header__t.html#ae672ffee68c08fedf3e46cfd3d027fb6
#
# ---
# uint16_t 	magicWord [4]
#  	Output buffer magic word (sync word). It is initialized to {0x0102,0x0304,0x0506,0x0708}. 
#   Definition at line 93 (@ mmw_output.h). & Referenced by MmwDemo_transmitProcessedOutput().
# ---
# uint32_t 	version
#   brief Version: : MajorNum * 2^24 + MinorNum * 2^16 + BugfixNum * 2^8 + BuildNum
#   Definition at line 96 (@ mmw_output.h). & Referenced by MmwDemo_transmitProcessedOutput().
# ---
# uint32_t 	totalPacketLen
#  	Total packet length including header in Bytes. 
#   Definition at line 99 (@ mmw_output.h). & Referenced by MmwDemo_transmitProcessedOutput().
# ---
# uint32_t 	platform
#  	platform type
#   Definition at line 102 (@ mmw_output.h). & Referenced by MmwDemo_transmitProcessedOutput().
# ---
# uint32_t 	frameNumber
#  	Frame number.
#   Definition at line 119 (@ mmw_output.h). & Referenced by MmwDemo_transmitProcessedOutput().
# ---
# uint32_t 	timeCpuCycles
#  	Time in CPU cycles when the message was created. For XWR16xx/XWR18xx: DSP CPU cycles, for XWR14xx: R4F CPU cycles. 
#   Definition at line 108 (@ mmw_output.h). & Referenced by MmwDemo_transmitProcessedOutput().
# ---
# uint32_t 	numDetectedObj
#  	Number of detected objects. 
# ---
# uint32_t 	numTLVs
#  	Number of TLVs. 
#   Definition at line 114 (@ mmw_output.h). & Referenced by MmwDemo_transmitProcessedOutput().
# ---
# uint32_t 	subFrameNumber
#  	For Advanced Frame config, this is the sub-frame number in the range 0 to (number of subframes - 1). 
#   For frame config (not advanced), this is always set to 0.
#   Definition at line 119 (@ mmw_output.h). & Referenced by MmwDemo_transmitProcessedOutput().
# --- '''
def getHeader(data):
    version, totalPacketLen, platform, frameNumber, timeCpuCycles, numDetObj,numTLVs, subFrameNumber = struct.unpack('8I', data)
    return version, totalPacketLen, platform, frameNumber, timeCpuCycles, numDetObj,numTLVs, subFrameNumber



def getPkt(gBuf, input_):
    flag_gBuf = False
    buf = bytes(0)
    
    gBuf = gBuf + input_

    startIdx, len_pkt = findStart(gBuf)
    # print('startIdx :', startIdx, 'pkt length :', len_pkt)
    
    for i in startIdx:        
        totalPktLength_header = getbinary_to_single(gBuf, 8, 4)
        
        if not flag_gBuf:
            len_gBuf = len(gBuf)

        if len_gBuf >= totalPktLength_header:
            buf : bytes = gBuf[i:totalPktLength_header]
            gBuf : bytes = gBuf[totalPktLength_header: ]
            
            flag_gBuf = True
            len_gBuf = len(gBuf)

    # print('>>> buf size :', len(buf), '& gBuf :', len_gBuf)
    return buf, gBuf


''' 2023.02.21 
# ### '''
def splitHeader(data, idx):
    result = list()
    h_ = bytes(0)
    p_ = bytes(0)
    
    h_ = data[8:idx]
    p_ = data[idx:]
            
    result.append(h_)
    result.append(p_)
    
    return result


''' 2022.12.31
# ### '''
def getTLV(data):
    # tlvType, tlvLength = struct.unpack('2I', data)
    return struct.unpack('2I', data)


''' 2022.12.31
# ### '''
def getHeatMap(data):
    # Init Constants. Referenced by config file
    heatmap_Value = []
    
    len_Range_Angle = numRangeBins*numAngleBins 
    
    # Init variables : heatmap result 
    rangeAzimuth = [0]*(numRangeBins * numAngleBins)
    default = np.zeros((numRangeBins,numAngleBins))
    raHMap = np.zeros((numRangeBins,numAngleBins))
            
    addr = 0
    for i in range(len_Range_Angle):
        heatmap_Value = struct.unpack('h', data[addr:addr+2])
        rangeAzimuth[i] = heatmap_Value[0]
        addr += 2
    
    range_azimuth_array = np.array(rangeAzimuth)
    raHMap = range_azimuth_array.reshape(numRangeBins, numAngleBins)
    
    return raHMap


''' 2022.12.31
# ### '''
def getDecisionValues(data):
    # Init variables : decision value 
    retVal_1 = [0]*num_of_zones
    retVal_2 = [0]*num_of_zones
    retVal_3 = [0]*num_of_zones
    retVal_4 = [0]*num_of_zones
            
    addr = 0
    for i in range(num_of_zones):
        retVal_1[i] = struct.unpack('f', data[addr:addr+4])
        addr += 4
        retVal_2[i] = struct.unpack('f', data[addr:addr+4])
        addr += 4
        retVal_3[i] = struct.unpack('H', data[addr:addr+2])
        addr += 2
        retVal_4[i] = struct.unpack('H', data[addr:addr+2])
        addr += 2
                
    return retVal_1, retVal_2, retVal_3, retVal_4


''' 2023.02.21
# ### Point Cloud TLV from SDK '''
def parsePointCloudTLV(tlvData, tlvLength, pointCloud):
    pointStruct = '4f'  # X, Y, Z, and Doppler
    pointStructSize = struct.calcsize(pointStruct)
    numPoints = int(tlvLength/pointStructSize)
    print('[_DETECTED_POINTS] pointStructSize :', pointStructSize, 'numPoints :', numPoints)
    
    for i in range(numPoints):
        try:
            x, y, z, doppler = struct.unpack(pointStruct, tlvData[:pointStructSize])
            # print("\t[%d/%d]"%(i+1, numPoints ), 'output xyz-doppler =', x,y,z,doppler)
        except:
            numPoints = i
            print('Error: Point Cloud TLV Parser Failed')
            break
            
        tlvData = tlvData[pointStructSize:]
        pointCloud[i,0] = x 
        pointCloud[i,1] = y
        pointCloud[i,2] = z
        pointCloud[i,3] = doppler
        
    return numPoints, pointCloud


''' 2023.02.21 
# ### Side info TLV from SDK '''
def parseSideInfoTLV(tlvData, tlvLength, pointCloud):
    pointStruct = '2H'  # Two unsigned shorts: SNR and Noise
    pointStructSize = struct.calcsize(pointStruct)
    numPoints = int(tlvLength/pointStructSize)
    print('[_SIDE_INFO] pointStructSize =', pointStructSize, ', numPoints =', numPoints)
    
    for i in range(numPoints):
        try:
            snr, noise = struct.unpack(pointStruct, tlvData[:pointStructSize])
            # print("\t[%d/%d]"%(i+1, numPoints ), 'output snr & noise =', snr, noise)
        except:
            numPoints = i
            print('Error: Side Info TLV Parser Failed')
            break
        tlvData = tlvData[pointStructSize:]
        # SNR and Noise are sent as uint16_t which are measured in 0.1 dB Steps
        pointCloud[i,4] = snr * 0.1
        pointCloud[i,5] = noise * 0.1
        
    return pointCloud


''' 2023.02.21 
# ### '''
def parseRangeProfile(data, tlvLength):
    numRPs = int(tlvLength / 2)
    values = np.ones((256,1))
    
    for i in range(numRPs):
        rangeProfile = struct.unpack('H', data[2*i:2*i+2])
        values[i] = (rangeProfile[0] * 1.0 * 6.0 / 8.0  / (1 << 8))*10.0
        
    return values


''' 2023.02.24
# # '''
def parseStats(data, tlvLength):
    interProcess, transmitOut, frameMargin, chirpMargin, activeCPULoad, interCPULoad = struct.unpack('6I', data[:24])
#     print("\tOutputMsgStats: %d "%(6))
#     print("\t ChirpMargin:\t%d "%(chirpMargin))
#     print("\t FrameMargin:\t%d "%(frameMargin))
#     print("\t InterCPULoad:\t%d "%(interCPULoad))
#     print("\t ActiveCPULoad:\t%d "%(activeCPULoad))
#     print("\t TransmitOut:\t%d "%(transmitOut))
#     print("\t Interprocess:\t%d "%(interProcess))


''' 2023.02.21 
# ### '''
def parser_mmWave(Dataport, configParameters, s, s_rp):
    global gBuf

    hBuf = bytes(0)
    pBuf = bytes(0)
    
    ENUM_HEADER_LEN_40 = 40 # header_length = 40
    ENUM_TLVHEADER_LEN_8 = 8 # tlvHeaderLength = 8
    ENUM_DETPOINTS_16 = 16 # len_detPoints = 16

    input_ = Dataport.read(Dataport.in_waiting)
    input_time = str(Dtime.datetime.now().strftime("# %y%m%d_%H%M%S_%f"))
    print(input_time, len(input_))
    w_radar.write(input_time +" UART ="+str(input_)+'\n')
            
    if input_:
        d_ = gBuf + input_
        
        sd_list = split_data(d_)
        print(input_time, 'Input =', len(d_), '& split =', len(sd_list))
        sd_list_final = len(sd_list) - 1
        
        if sd_list[-1]:
            # # init heatmap variables
            rangeAzimuth = [0]*(numRangeBins * numAngleBins)
            
            for k in range(len(sd_list)):
                # print('\n', '[', k+1, '] packet :')
                # print("\n[%d/%d] packet"%(k+1, len(sd_list) ))
                pktLen_in_header = getbinary_to_single(sd_list[k], 12, 4)
                split_data_len = len(sd_list[k])

                if not split_data_len == pktLen_in_header:
                    # print('split data length, header recorded value :', split_data_len, ' &', pktLen_in_header)
                    if sd_list_final == k:
                        gBuf = sd_list[k]
                        print('>>> gBuf packet is', input_time)
                        print('\n')
                    else:
                        # 헤더에 기록된 pkt size와 실제 입력 pkt이 같지 않을 경우, 해당 pkt은 버림
                        print('Issue_No_01')
                        pass
                else:
                    gBuf = bytes(0)

                    header_payload = splitHeader(sd_list[k], ENUM_HEADER_LEN_40)
                    # print('payload =', struct.unpack('792b', header_payload[1]))

                    version, totalPacketLen, platform, frameNumber, timeCpuCycles, numDetObj,numTLVs, subFrameNumber = getHeader(header_payload[0])
                    # print('\tnumDetObj =', numDetObj, ',numTLVs =', numTLVs)

                    outputDict = {}
                    outputDict['pointCloud'] = np.zeros((numDetObj, 7), np.float64)
                    outputDict['pointCloud'][:, 6] = 255

                    for i in range(numTLVs):
                        tlvType, tlvLength = getTLV(header_payload[1][:ENUM_TLVHEADER_LEN_8])
                        _payload = header_payload[1][ENUM_TLVHEADER_LEN_8:ENUM_TLVHEADER_LEN_8+tlvLength]
                        # print('\n[',i+1,'-th] type', tlvType,', length=',tlvLength,'& payload size=',len(_payload))

                        header_payload[1] = header_payload[1][ENUM_TLVHEADER_LEN_8+tlvLength:]

                        if (tlvType == MMWDEMO_OUTPUT_MSG_DETECTED_POINTS):
                            outputDict['numDetPoints'], outputDict['pointCloud'] = parsePointCloudTLV(_payload, tlvLength, outputDict['pointCloud'])
                            # print('[_DETECTED_POINTS] outputDict :', outputDict)

                        elif (tlvType == MMWDEMO_OUTPUT_MSG_RANGE_PROFILE):
                            rp_Value = parseRangeProfile(_payload, tlvLength)
                            print('[parser_mmWave] RANGE_PROFILE =', len(rp_Value))

                        elif (tlvType == MMWDEMO_OUTPUT_MSG_NOISE_PROFILE):
                            print('[parser_mmWave] Skip proc ... _NOISE_PROFILE')
                        elif (tlvType == MMWDEMO_OUTPUT_MSG_AZIMUT_STATIC_HEAT_MAP):
                            rNas = getHeatMap(_payload)
                            print('[parser_mmWave] RANGE_AZIMUT_STATIC_HEAT_MAP =', len(rNas))
                            
                        elif (tlvType == MMWDEMO_OUTPUT_MSG_RANGE_DOPPLER_HEAT_MAP):
                            print('[parser_mmWave] Skip proc ... _RANGE_DOPPLER_HEAT_MAP')
                        elif (tlvType == MMWDEMO_OUTPUT_MSG_STATS):
                            parseStats(_payload, tlvLength)
                            print('[parser_mmWave] STATS')
                        elif (tlvType == MMWDEMO_OUTPUT_MSG_DETECTED_POINTS_SIDE_INFO):
                            outputDict['pointCloud'] = parseSideInfoTLV(_payload, tlvLength, outputDict['pointCloud'])
                            # print('[_SIDE_INFO] outputDict :', outputDict)
                        elif (tlvType == MMWDEMO_OUTPUT_MSG_AZIMUT_ELEVATION_STATIC_HEAT_MAP):
                            print('[parser_mmWave] Skip proc ... _AZIMUT_ELEVATION_STATIC_HEAT_MAP')
                        elif (tlvType == MMWDEMO_OUTPUT_MSG_TEMPERATURE_STATS):
                            print('[parser_mmWave] Skip proc ... _TEMPERATURE_STATS')
                            pass
                        
                    # # Run GUI
                    # dp.main()
                    draw_plot(s, outputDict, s_rp, rp_Value)
    else :
        gBuf = bytes(0)            
