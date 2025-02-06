---
date: 2025-02-05 17:03:25
layout: post
---


※ flow chart of 3D People Counting Demo Implementation using mmWave SDK components.  
```mermaid  
flowchart TD  
    Host -->|Configuration| MSS  
    MSS --> |Point Cloud/Tracking| Host  
    
    subgraph App
        direction LR
        MSS
        DSS
    end
    
    MSS --> mmWaveLib(mmWave Lib)
    MSS --> DPM_M(DPM_mss)
    DPM_M --> DPC_HWA(DPC:objdetrangehwa.c)
    DPC_HWA --> DPU_RangeHWA
    DPC_HWA --> DPU_Tracker
    
    mmWaveLib --> mmWaveLink(mmWave Link)
    mmWaveLink --> mmWaveFEM(mmWave Front End)
    MSS --> DPU_Tracker
    
    DSS --> DPM_d
    DPM_d --> DPC_d(DPC:objectdetection.C)
    DPC_d --> DPU(Low Level Processing channel: radarProcess.c)
    DPU --> ConstantFalseAlarmRate
    DPU --> DOA2D/caponBF
```
 

## 1.1. Application (3D People Counting Application Level)  

Application is split between MSS and DSS. DSS and MSS call the DPM APIs through which they control the configuration and execution of DPCs.  
MSS also controls the radar front end, and communicates with the Host.  
---  

## 1.2. mmWave Lib  

The mmWave Lib module is a higher layer control running on top of mmWaveLink and LLD API (drivers API).  

<details>
    mmWave Lib module은 mmWaveLink와 LLD API(드라이버 API) 위에서 실행되는 상위 제어 계층이다.  
</details>  

radar fem을 control하는 App을 위한 API set을 제공한다.  
mmWave module은 R4F (MSS)에서만 실행한다.
---

## 1.3. mmWave Link  
control layer  

--- 

## 1.4. Data-path Manager (DPM)  

---

# Code Review  


- Pcount3DDemo_dssInitTask
  + 'ptrProcChainCfg'에 gDPC_ObjectDetectionCfg (프로세스 체인 구조체[^procChainCfg]) 정의

- gDPC_ObjDetRangeHWACfg   
  : ~~objdetrangehwa.c in '..\common\dpc\objdetrangehwa\src' (Global used to register Object Detection DPC in DPM)~~  
  : 

- DPC_ObjectDetection_execute [^DPC_ObjectDetection_execute]  
  + DPU_RangeProcHWA_process (in objdetrangehwa.c)
  + DPU_radarProcess_process
    - rangeProcHWA_dcRangeSignatureCompensation ("calib DC processing"이 enable 조건에서)




---
[^ procChainCfg]: objewctdetection.c in '..\common\dpc\capon3d\src'에 선언되어 있음  
[^DPC_ObjectDetection_execute] : relation이 3곳 나타남, 파일은 동일
