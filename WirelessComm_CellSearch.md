목차  
[1. LTE](##1-LTE)  
[1.1. PHYSICAL LAYER](###1.1.-PHYSICAL-LAYER)  
[1.2. LOGICAL LAYER](###1.2.-LOGICAL-LAYER)  
[1.3. LTE Cell 탐색 절차](###1.3.-LTE-Cell-탐색-절차)  
[2. 5G](#2.-5G)  

- - -
## 1. LTE  
### 1.1. PHYSICAL LAYER  
### 1.2. LOGICAL LAYER  
### 1.3. LTE Cell 탐색 절차  
- 무선단말의 셀 탐색(셀 ID,동기화 등)을 위해 2가지 신호가 전송됨  
  ㄴ. 셀 탐색과정의 복잡성을 감소시키는 목적으로 2가지 신호를 사용  
  ㄴ. Primary Synchronization Signal (PSS)와 Secondary Synchronization Signal (SSS)  
- 절차  
  ㄴ. Cell 탐색(Cell 동기획득) → 동기화 → Cell Selection(물리계층 Cell ID 결정) → Cell 시스템 정보 획득 →  랜덤 엑세스 과정 수행  
  
##### 1.1. Cell Search Procedure  
##### 1.2. Synchronization Procedure  
- 셀의 주파수 동기 : 무선단말 내 발진기와 셀 기지국과의 발진주파수 동기화  
- 셀의 프레임 동기 획득 : 하향링크 프레임의 시작 시점(타이밍)의 획득  
- 셀의 심볼 동기 획득 : 심볼이 존재하는 정확한 구간을 확정

  + UE는 1-slot의 마지막 OFDM 심볼에 있는 PSS를 찾는다.  
  + LTE는 다른 무선시스템과(GSM/GPRS/EDGE, WCDMA/HSPA 또는 CDMA 등)도 HO를 해야하기 때문에 주파수 간 RAT 측정 단순화를 위해 1번과 5번의 서브프레임에서의 PSS가 존재하여 두 번 전송된다.  
  + PSS 검출 후 SSS에 속한 0~167의 cell groud ID를 검출(시작 프레임 정보 획득)한 다음 획득한 Cell ID와 동기화를 진행하면, RS(Reference Signal)이 전송되어 UE와 동기화 한다.  
  + Master Information Block(MIB)는 BCH를 통해 40ms간격으로 전송  

![img](https://t1.daumcdn.net/cfile/tistory/141392445039C4DA3F)  

![img](https://t1.daumcdn.net/cfile/tistory/1624824750406F1E38)  

  + BCH는 2-slot의 한가운데 72개의 부반송파에 걸쳐 전송되는데 이때 사용되는 72개의 부반송파는 PDSCH전송에 사용될 수 없다.  
    : LTE에서 지원하는 가장 작은 대역폭은 1.4Mhz 이며 사용되는 부반송파(RB, 6개)가 72개임  
  + System Information Block(SIB)은 DL-SCH로 전송되어 PDSCH에 맵핑된다.  

- SIB1은 셀과 액세스 할수 있는 정보와 TDD의 특수 서브프레임 구성에 대한 정보 나머지 SIB들의 시간 도메인 스케줄링에 대한 정보가 포함  
- SIB2는 셀에 액세스 할 수 있도록 터미널에서 필요하는 정보(UL cell Bandwidth, 랜덤액세스 파라미터, UL 전력 제어에 연관된 파라미터)를 가지고 있다.  
- SIB3는 셀 재선택에 관련된 정보가 포함  
- SIB4-SIB8은 네이버 셀에 관련된 정보를 포함한다. 이 정보에는 동일 주파수의 네이버 셀, 다른 주파수의 네이버 셀, 그리고 WCDMA/HSPA, GSM, 그리고 CDMA 2000과 같은 non-LTE 네이버 셀에 대한 정보를 포함한다.  
- SIB9는 HeNB의 이름을 포함  
- SIB10-SIB12는 공동 재난 메시지를 포함한다.(예 지진)  
- SIB13에는 MBMS 수신에 대한 중요 정보 포함  

##### 1.4. Random Access Procedure  
UE는 랜덤액세서 채널인 RACH를 통해 eNB에게 프리엠블을 보낸다. 프리엠블의 경우 거리에 따라 정보가 손실 될 수있기 때문에 거리가 길어지면 CP의 길이 또한 길어지게된다.   
프리엠블을 받은 eNB는 사용된 프리엠블로 거리를 추정한  근거로 터미널 전송 타이밍 조정을 하는 명령을 보내고 추가로 업링크 동기를 설립하고 다음 단계에서 사용될 업링크 자원(스케줄)을 할당한다.  

![img](https://t1.daumcdn.net/cfile/tistory/1728613E5039C77412)  

###### ㅁ LTE 전송 단위, LTE Slot, LTE Symbol, Basic Time Unit  
- Resource Block, Resource Grid, Resource Element   
  + 자원 블록  
    ㄴ. 기지국에서 스케줄링하는 기본단위(LTE OFDM에서 주파수축 및 시간축 2차원 상의 블록 모양을 한 할당 가능 자원의 단위)  
    ㄴ. 1 RB = 84 (12x7) resource elements  
    ㄴ. 1 resource element : 여러 특정 부반송파들이 동일 시간간격인 1 symbol에 위치 가능  
    + 하향링크 사용 대역폭에 따른 자원블록 수  
      ㄴ. 1.4 MHz(6), 3 MHz(15), 5 MHz(25), 10 MHz(50, 우리나라 주로 사용), 15 MHz(75), 20 MHz(100)  
    + 특정 사용자 전송속도  
      ㄴ. 특정 사용자에게 할당되는 자원블록(또는 부반송파)의 수에 의존  
  + 자원 그리드  
    ㄴ. 주파수,시간 두 축에 따라 격자화된 구조(LTE에서 정해진 채널이나 신호들이 저마다 격자 내 세분화된 적정 위치에 매핑됨)  
    ㄴ. 축 단위 구분  
       + 주파수축 : Subcarrier(부반송파) 마다 구별 가능  
       + 시간축 : OFDM Symbol(OFDM 심볼) 마다 구별 가능  
  + 자원 요소  
    ㄴ. 가장 작은 물리적인 자원(구별가능한 최소 단위로 그룹화된 비트들): 하나의 부반송파(주파수) 및 하나의 OFDM 심볼(시간)  
       ※ 변조 방식(QPSK,16-QAM,64-QAM)에 따라, 2,4,6 비트(물리채널) 할당  
       
![img](http://www.ktword.co.kr/img_data/4969_1.JPG)  

###### ㅁ LTE Frame  
ㄴ. 구분: LTE FDD (type1) & LTE TDD (type2)  
- LTE FDD  
  
![img](http://www.ktword.co.kr/img_data/5464_1.JPG)  
  
  + Frame  
    ㄴ. **1 radio frame (1 system frame)= 10ms**  
    ㄴ. 1 radio frame의 sample 수     = 307,200 [samples/sec]  
    ㄴ. 1 [초,sec]                    = 100 [radio frames/sec] ( = 30,720,000 [samples/sec])  
  + Subframe  
    ㄴ. 1 radio frame = 10 subframes  = 10ms  
    ㄴ. 0.1 radio frame = **1 subframe  = 1ms** (TTI)  
  + Slot  
    ㄴ. **1 slot = 1 subframe = 0.5ms**  
    ㄴ. 1 radio frame = 20 slots = 10ms  
  + Symbol  
    ㄴ. 1 subframe = 14 symbols  
    ㄴ. 1 slot = 7 symbols  
    ㄴ. modulation type별 symbol/bit : 64QAM(6), 16QAM(4), QPSK(2)  
    ㄴ. 1 symbol : normal CP (Short CP) = 0.5ms/7, extended CP (Short CP) = 0.5ms/6  

## 1.2. Logical Layer
![img](https://t1.daumcdn.net/cfile/tistory/117B8A3F503738CF0D)  
![img](C:\Users\Administrator\AppData\Roaming\Typora\typora-user-images\image-20210806110404704.png)  
[LTE Frame 구조](https://encyfic.tistory.com/11)  

### 1.2.1. downlink  

### 1.2.2. uplink  

#### 1.2.2.1. logical channels  
- DTCH  
- DCCH  
- CCCH  

#### 1.2.2.2. transport channels
- UL-SCH  
- RACH  

#### 1.2.2.3. physical channels
- PUCCH (Physical Uplink Control CHannel) : UE → BS(eNB)  
  . HARQ의 ANK/NACK와 (CQI)Channel Quality Indicator정보를 전송  
  . 예약된 주파수 영역 내에서만 전송(uplink CH BW의 edge쪽의 band에서 resource 블럭 사용)  
  . Uplink Control Information (UCI) 전달  

  ​	-. CQI (Channel Quality Indicator) : downlink radio link quality, 단말에서 수신받을 때 무선 링크의 상태를 기록한 정보

  ​	-. PMI (Precoding Matrix Information) and RI (Ranking Indication) : MIMO mode selection과 구성에 대하여 지원하는 정보

  ​	-. SR (Scheduling Requests) : uplink resource에 대한 요청이 있을 경우 사용

  . format

  ![image-20210806141749449](C:\Users\Administrator\AppData\Roaming\Typora\typora-user-images\image-20210806141749449.png)

  . Tx power : P_pucch = min(P_max,10log10(M_pucch) + P_o_pucch + PL + mcs_pucch + g(j)) 

  ![image-20210806142041992](C:\Users\Administrator\AppData\Roaming\Typora\typora-user-images\image-20210806142041992.png)

- PUSCH

- PRACH

# 2. 5G  
  5G의 물리채널 구조는 LTE와 유사  
  LTE 제어 채널의 문제점을 해결하기 위해 CORSET (Control Resource Set) 개념 도입.  
  LTE에서 NB-IoT를 제외하고 셀 내의 모든 단말기는 기지국에 사용하는 전 대역의 주파수 신호를 수신할 수 있어야 기지국의 제어 신호를 받을 수 있다. 5G에서는 단말기가 수신해야 하는 제어 정보 무선 자원(CORSET)을 기지국이 기지국이 각 단말 별로 할당하기 때문에 기지국이 단말로 할당한 CORSET을 통해서 기지국의 제어정보를 받을 수 있으므로 단말기는 기지국의 주파수 전 대역을 수실할 필요가 없다. CORSET은 각 단말기에 특화된 제어정보 전송을 위한 UE-Specific CORSET과 모든 단말에게 공통적으로 필요한 Common CORSET 두 가지로 나눌 수 있다. Common CORSET은 기지국 시스템 정보를 전송하는데 사용된다.  
  5G의 Downlink는 PBCH (Physical Broadcast CHannel), PDCCH, PDSCH, 3개의 physical ch이 있다. PBCH는 초기 접속에 사용되고, PDCCH는 DCI (Downlink Control Information)을 실어 나르는데 사용된다. DCI에는 사용자 데이터의 자원 영역 위치 및 단말에서 사용자 데이터를 디코딩하기 위해 필요한 정보 등이 포함된다. PDSCH는 사용자 데이터를 전달하는데 사용된다. 변조방식으로는 QPSK, 16QAM, 64QAM, 256QAM이 단말기의 전파 상태에 따라 선택적으로 사용된다.  
  uplink의 physical channel로는 PUSCH, PUCCH, PRACH가 있다. PRACH는 초기 접속에 다용되는데, 단말기에서 기지국으로 Random Access Preamble을 전송한다. PUCCH는 UCI (Uplink Control Information), HARQ-ACK, SR (Scheduling Request)을 전송한다. UCI에는 단말기 전송할 업링크의 사용자 데이터 자원 영역 위치 및 다운링크 사용자 데이터를 단말기가 오류없이 수신했는지 여부를 기지국에 알려주기 위해 필요한 업링크 자원 영역 위치 등이 포함된다.  

## 2.1. Physical Layer
![img](https://postfiles.pstatic.net/MjAxOTAzMDNfMjc3/MDAxNTUxNjE0MDA0NTA1.qo2pDSvjQdMCgXbIYIGXCH3Heol8tfjH0vk3D2fQgJEg.437t3KJYwPBt_oxh9xVUUch7pHiCyMHRyVVHJ2K0Ab4g.PNG.zser2468/image.png?type=w773) 
![img](https://postfiles.pstatic.net/MjAxOTAzMDNfMjEy/MDAxNTUxNjE0MTA2NTc5.dAlxSIUJkieC2UEy2L_O7zJFayz9vy4kcOb0Fi0gH2Ig.eaitqupu3S-GEPCOX8Fs_xu_XZarotG9NsmZdBzfgPcg.PNG.zser2468/image.png?type=w773) 

### 2.1.1. Radio Frame Structure
 참조: 3GPP specification (38.211)  
 frame 종류  
| numerology (μ) | # of symbols | # of subframe | # of slots |
| -------------- | ------------ | ------------- | ---------- |
| 0              | 14           | 10            | 1          |
| 1              | 14           | 20            | 2          |
| 2              | 14           | 40            | 4          |
| 3              | 14           | 80            | 8          |
| 4              | 14           | 160           | 16         |

#### 2.1.1.1. Normal CP, Numerology = 0  
- 1 subframe = 1 slot (radio frame은 10슬롯을 포함).  
- slot 내의 OFDM symbol의 수는 14.
![image-20210805091021648](D:\05.works\21년도\210405_RFDoppler\_img_5g\image-20210805091021648.png)  

#### 2.1.1.2. Normal CP, Numerology = 1
- subframe has 2 slots (radio frame contains 20 slots). The number of OFDM symbols within a slot is 14.

#### 2.1.1.3. Normal CP, Numerology = 2
- subframe has 4 slots (radio frame contains 40 slots). The number of OFDM symbols within a slot is 14.

#### 2.1.1.4. Normal CP, Numerology = 3
- subframe has 8 slots (radio frame contains 80 slots). The number of OFDM symbols within a slot is 14.

#### 2.1.1.5. Normal CP, Numerology = 4
+ subframe has 16 slots (radio frame contains 160 slots). The number of OFDM symbols within a slot is 14.

#### 2.1.1.6 Extended CP, Numerology = 2
+ subframe has 4 slots (radio frame contains 40 slots). The number of OFDM symbols within a slot is 12.

### 2.1.2. Slot Format
+ Slot Format indicates how each of symbols within a single slot is used.  
+ It defines which symbols are used for uplink and which symbols are used for downlink within a specific slot.  
+ In LTE TDD, if a subframe (equivalent to a Slot in NR) is configured for DL or UL, all of the symbols within the subframe should be used as DL or UL. But in NR, the symbols within a slot can be configured in various ways as follows.
  + We don't need to use every symbols within a slot (this can be a similar concept in LAA subframe where only a part of subframes can be used for data transmission).  
  + Single slot can be devided into multiple segments of consecutive symbols that can be used for DL , UL or Flexible.  

## 2.2. Logical Layer  
  5GC : 5G Core network
  gNB : node providing NR user plane and control plane protocol terminations towards the UE, and connected via the NGinterface to the 5GC.
  ng-eNB : node providing E-UTRA user plane and control plane protocl terminations towards the UE, and connected wia the NG interface to the 5GC.

  NG-RAN node : either a gNB or an ng-eNB. gNB는 수신빔을 결정할 때 UE로 부터 수신되는 정보(DL로 측정된 기준)로 가장좋은 수신빔을 선택. UE가 수신빔을 결정할 때는, gNB로 부터 가장 좋은 수신빔이 먼지 전달 받는다(gNB는 UE로부터 받은 업링크 측정된 기준으로 알려줌). 
  The gNB and ng-eNB 
  The AMFThe UPF
  The Session Management function (SMF)
  기존 Evolved Packet System(EPS)의 코어네트워크 구조인 Evolved Packet Core(EPC)의 경우 Mobility Management Entity(MME), Serving Gateway(SGW), Packet Data Network Gateway(P-GW) 등 entity 별로 기능, 연결점, 프 로토콜 등이 정의되어 있다. 반면에 NextGen 코어네트워크에서는 그림 1과 같이 entity가 아닌 네트워크 기능(Network Function, NF) 별로 기능, 연결점, 프로토콜 등이 정의되어 있다. Radio Access Network(RAN)는 새로운 RAT을 사용하는 기지국을 나타낸다. AN은 Wi-Fi와 같은 non-3GPP 접속 기술을 포함한 일반적인 기지국을 나 타낸다. RAN(또는 AN)와 Access and Mobility Function(AMF) 그리고 AN와 User Plane Function(UPF)를 연결하는 참고점을 각각 NG2, NG3로 정의하고 있다.

※ LTE-U (LTE-Unlicensed) 또는 LTE-LAA (License Assisted Access) : 모바일 데이터 트래픽 문제점을 해결하기 위해 5GHz 대역의 비인가 주파수 영역을 사용하는 방안으로, 주파수 공유 접속 기술이나 하향 링크용 대역 확보 기술 등이 있음
  -. 주파수 공유 접속 (LSA: Licensed Shared Access) : 이동통신 이외의 다른 서 비스에서 사용하고 있는 주파수 대역이지만 지역적/시간적으 로 사용이 없을 때 이를 이동통신 주파수로 활용하기 위한 공유 기술
  -. SDL (Supplemental Down Link) : FDD를 고려한 상하향 링크 쌍을 수용하기 위한 주파수 대역 (paired band) 확보가 어려워 트래픽이 더 많은 하향 링크용 대역만 확보하고 이를 주파수 집성기술 (CA: Carrier Aggregation)로 활용하는 기술  

## 2. 무선 환경 지표  
### 2.1. 무선환경 지표  
#### 2.1.1. 셀룰러  
|           | RSSI   | RSRQ  | RSRP   |
| --------- | ------ | ----- | ------ |
|           | LTE/3G | LTE   | LTE    |
| 매우 좋음 | -65    | -5    | ~ -84  |
| 좋음      | ~ -75  | ~ -10 | ~ -102 |
| 보통      | ~ -85  | ~ -10 | ~ -111 |
| 나쁨      | -85 ~  | -11 ~ | -112 ~ |


#### 2.1.2. Wi-Fi  
|      | Wi-Fi    |
| ---- | -------- |
| -30  | 매우좋음 |
| -67  | 좋음     |
| -70  | 보통     |
| -80  | 나쁨     |
| -90  | 매우나쁨 |


### 2.2. 측위  
#### 2.2.1. wi-fi 기반 측위  
현재 위치의 WiFi 신호 세기패턴을 수집한 후, 측위 데이터베이스와 비교하여 위치 추정  

#### 2.2.2. 셀룰러 기반 측위  
기지국이나 중계기 위치 또는 셀룰러 신호의 세기나 상태 등을 이용하여 위치 추정  
WiFi 신호 세기의 비해 변별력이 떨어져 주로 기지국이나 중계기의 위치를 기반으로 위치 추정(셀룰러 서비스를 제공하는 통산사에 의존적, 측위 정확도 낮음)  
참고문헌: Channel State Information-Reference Signal (CSI-RS) 데이터를 이용하여, 위치를 추정하는 방법 (Pecoraro, G., Di Domenico, S., Cianca, E., & De Sanctis, M. 2018, CSI-based fingerprinting for indoor localization using LTE Signals, EURASIP Journal on Advances in Signal Processing, 49. https://doi.org/10.1186/s13634-018-0563-7)

[Analysis of Outdoor Positioning Results using Deep Learning Based LTE CSI-RS Data](http://www.koreascience.kr/article/JAKO202026252144599.page)

-. gNB에서 CSI-RS를 UE로 전송: CSI-RS 재사용 패턴을 Radio resource control (RRC) 메시지를 통해 긴 주기마다 단말에 전송
-. UE는 CSI-RS를 이용하여 gNB에 보고할 CSI 계산 : CSI-RS를 이용하여 단말은 Rank Indicator (RI), Channel Quality Indicator (CQI) 및 Precoding Matrix Indicator (PMI)를 추정하여 기지국에게 피드백(feedback)
-. 수집 시간에 따라 OFDM 심볼마다 진폭 크기의 격차가 크게 변화하는 경우가 발생하므로, 주파수 응답 진폭 그래프를 기반으로 맵 작성
-. OFDM 심볼들의 주파수 응답의 크기 값을 기준으로 중간 값을 갖는 OFDM 심볼만 선택하여 주파수 응답 진폭 그래프 작성
![fig 3.PNG 이미지](http://www.koreascience.kr/ks-full-text-html-image/JAKO202026252144599:3/image.image)
그림. CSI-RS 데이터 수신 장치 (Xillinx Zynq 7000 임베디드 보드에 Analog Devices 사의 RF 카드를 부착하고 수신용 LTE 안테나 2개를 연결한 후, 노트북의 MATLAB과 연동하여 LTE CSI-RS 데이터를 수집)

### 2.3. propagation model
-. 자유공간 전력 전송 방정식: https://arenaofyh.blogspot.com/2018/06/friss.html

#### 2.3.1. 자유공간 경로 손실
자유공간 경로 손실(Free Space Path Loss)은 자유공간에서 통신 시 전자기파 신호의 손실이다.

A. Free Space Path Loss (FSPL) 계산:
![img](https://mblogthumb-phinf.pstatic.net/MjAxNjExMTVfMTEw/MDAxNDc5MTg5OTk4Nzky.LWskWEM2Wpb2Y4AtQUdW9UZluoR-EfhQFB053H4nWEQg.DjNL1ysD4fMa7aL6auyXVZZ7eqA0ZPGVLDxDQp0GU2cg.JPEG.pgwkys/%EC%88%98%EC%8B%9D1-1.JPG?type=w800)  

· λ : 신호의 파장 (meters)
 · f : 신호의 주파수 (herz)  
 · d : 통신 거리 (meters)
 · c : 빛의 속도 ( 3* 10^8 m/s)

B. dB 단위 변환:
![img](https://mblogthumb-phinf.pstatic.net/MjAxNjExMTVfNiAg/MDAxNDc5MTg5OTIzNDUx.xESencByHQBApiT9fmpeiGineBdX88NXVkFRnAxX0iQg.Qx-x4yXTreDxWo_zgetWFqlXPkufct4EnmHkNiTVJbIg.JPEG.pgwkys/%EC%88%98%EC%8B%9D3.JPG?type=w800)   

##### ※ 계산 예
· 통신 방식 : WiFi
· 주파수(f) : 2.4GHz 대역 (채널1 : 2412 MHz로 계산)
· 통신거리(d) : 100 미터

![img](https://mblogthumb-phinf.pstatic.net/MjAxNjExMTVfMjE0/MDAxNDc5MTkyMjI0Mzc3.bU39JGK9x5gP63SG27291JPsXAfl-3V-aSLhlrGnO6Qg.8UFzTcB-uchxHNsaCcdNn_0ewsSe-EKxNn9M09_RTzIg.JPEG.pgwkys/%EC%88%98%EC%8B%9D4.JPG?type=w800)   

위 계산에서, 100미터 떨어진 곳에서 WiFi 신호가 약 80dB 감쇄(이론상)가 일어난다. 실제 쉴드룸에서 두 AP 간격을 1미터로 하고 신호 세기를 읽었을때 약 35~40dB 감쇄. (위 수식에서, 거리를 1미터로 계산 시 40dB로 수신단의 LNA gain 고려시 35~40dB 감쇄 예상)  
이동통신에서는 안테나에서 방사하는 출력이 단말에 얼마나 잘 도달하는지가 중요하다. 기지국에 가까울수록 무선 환경이 좋고, 기지국에서 멀어질수록 무선 환경이 불량하다는 이유가 바로 Pathloss (자연적으로 공기중에서 사라지기 때문) 때문이다.  

수식에서,  
-. 거리의 단위가 m이고, 주파수 단위가 Hz인 경우, 상수는 -147.55  
-. 거리의 단위가 m이고, 주파수 단위가 MHz인 경우: 상수는 -27.55  
1.8GHz 대역의대역에서, 안테나와 100m 떨어진 곳에서의 pathloss는 77.56dB가 된다.  
$$  
= 20log_{10}(100) + 20log_{10}(1800*10^{6})-27.55
= 40 + 65.11 -27.55
= 77.56dB
$$  

-. ref: http://www.ktword.co.kr/test/view/view.php?m_temp1=3635&id=769  
-. ref: https://sites.google.com/site/rokthesis/2-gwanlyeon-yeongu/2-2-gyeonglo-sonsil-model  
-. ref: https://m.blog.naver.com/PostView.naver?isHttpsRedirect=true&blogId=kore2758_&logNo=221261329924  

안전거리 구하기  
![안전거리 구하기](https://img.khan.co.kr/news/2008/12/22/m1222_c.jpg)  

#### 2.3.2. log-distance 경로 손실  
[![img](https://sites.google.com/site/rokthesis/_/rsrc/1482456589473/2-gwanlyeon-yeongu/2-2-gyeonglo-sonsil-model/2-2-1-log-distance-gyeonglo-sonsil-model/1.jpg)](https://sites.google.com/site/rokthesis/2-gwanlyeon-yeongu/2-2-gyeonglo-sonsil-model/2-2-1-log-distance-gyeonglo-sonsil-model/1.jpg?attredirects=0)  
여기서, PL은 평균 경로손실이며, n은 평균 경로 손실 지수로써 주위환경과건물의 구조에 따라 값이 달라진다. d는 송수신기 사이의 거리이며, *𝑋𝜎* 는 표준편차를 갖는 제로평균 대수 정규분포이다.

#### 2.3.3. 다중벽 경로 손실  
[![img](https://sites.google.com/site/rokthesis/_/rsrc/1482456886160/2-gwanlyeon-yeongu/2-2-gyeonglo-sonsil-model/3.JPG?height=103&width=872)](https://sites.google.com/site/rokthesis/2-gwanlyeon-yeongu/2-2-gyeonglo-sonsil-model/3.JPG?attredirects=0)
여기서, n*f* 는 송수신기 사이에 존재하는 벽의 개수, n*w* 는 송수신기 사이에 존재하는 층의 개수, 그리고 a*f* 는 층간 손실계수, l*wi* 는 벽의 종류에 따른 손실을 나타낸다.  


정지된 이동 노드의 위치를 추정
  -. 남궁현, 임일권, 이재광. iBeacon을 활용한 측위 시스템 위치추정 기법. 한국정보통신학회논문지, 19(4):925-932, 2015. 

## 3. 약어
##### ※ CSI-RS(gNB→UE)  
LTE 데이터를 송/수신하는 무선 채널의 상태 정보를 확인하고 왜곡을 보정하거나 복조에 활용하기 위한 참조신호로, 수신하는 위치에 따라 채널 주파수 응답 크기의 변화가 발생한다. 이러한 특성을 활용하여 채널 주파수 응답 크기 진폭맵을 구성한 뒤 딥러닝 기반의 이미지 분류 방법에 적용하여 측위를 수행  

##### ※ RSRQ  
Reference Signal Received Quality, UE에 수신되는 모든 power의 총 크기 대비 Reference Signal power 비율  
        -. RSRQ = (RSRP/RSSI)*RB  

##### ※ RSRP  
Reference Signal Received Power, UE에 수신되는 Reference Signal의 세기.  Handover와 Cell Reselection을 결정하기 위해 cell signal의 강도를 선택하는데 도움을 주는 지표. 5G에서는 SS-RSRP (Synchronization Signal), CSI-RSRP (Channel State Info.)로 2개로 나뉨.

##### ※ RB  
Resource Block, 실제 데이터가 실려 있는 최소 단위의 자원  
  -. 시간 단위 : 1ms, 
  -. 주파수 단위 :  LTE 1개의 sub-carrier(15khz)*12개, 10Mhz 대역폭 기준으로 RB 50개, 3.5G 1개의 sub-carrier(30khz)*12개, 100Mhz 대역폭 기준 RB 273개(28G의 RB는 400M기준 264개 

##### ※ PRB  
기지국 입장에서 RB를 얼마나 사용하는지 나타내는 지표. 높을 수록 트래픽 밀집지역  

##### ※ RS  
Reference Signal, 데이터 변/복조를 위한 채널을 추정하기 위한 Pilot 신호, 처음 호를 열기 위함(위치 고정)  

##### ※ TS   
Traffic Signal=Data Signal, 실제 data가 실리는 자원  

##### ※ RSSI  
Received Strength Indicator, 단말기가 수신하는 모든 신호 세기의 합 (인접채널, noise 등을 모두 포함)  

##### ※ PCI  
Physical Cell Identity, Cell에 할당된 번호, 단말기가 PCI 번호를 보고 통신 가능 (0~503까지)  

##### ※ EARFCN  
Evolved Absolute Radio Frequency Channel Number, 주파수 대역을 말하는 이름  

##### ※ Pcell  
Primary Cell, 가장 우선적으로 강하게 잡고 있는 cell  

##### ※ Scell  
Secondary Cell, CA를 하게 되었을 때 Pcell을 제외한 나머지 CA 동작에 참여한 주파수 대역 cell  

##### ※ RI  
Rank Index, MIMO가 제대로 동작하고 있는지를 판단하는 값. 단말이 가진 무선환경 상태에 따라 RI 요청, 1이면 SIMO, 2이면 MIMO  

##### ※ BLER
Block Error Rate, eNB와 UE간 무선자원을 구성하고 제어하는데 쓰임  

##### ※ TA  
Tracking Area, 단말기가 idle 일때는 특정 cell이 아니라 광범위한 범위 그룹에 위치한 것으로 eNB에게 알려지게 되는데, 그 단위가 TA. 단말기가 망에 접속하거나, 망이 단말기를 깨울 때 특정한 셀로 바로 접속하는 것이 아니라 TA 전체에 신호를 날리고, 그 후 특정 Cell로 신호를 다시 보내게 되는 과정으로 접속 진행  

##### ※ TAC  

Tracking Area Code, LTE 단말의 위치정보, WCDMA는 RNC->MSC를 단위로 기지국을 묶고, LTE는 MME 단위로 가입자를 묶는다. LTE 단말의 위치정보를 등록하기 위해 W 기지국을 기준으로 TAC 등록  

##### ※ CQI  
Channel Quality Indicator, 단말이 무선환경을 분석하여 modulation order 및 coding rate 조합을 보내 는 것(0~15, 높을 수록 good)  

##### ※ MCS  
Modulation and Coding Scheme, Modulation을 결정해 주는 파라미터  

##### ※ LTE-U / LTE-LAA  
LTE-U (LTE-Unlicensed) / LTE-LAA (License Assisted Access), 모바일 데이터 트래픽 문제점을 해결하기 위해 5GHz 대역의 비인가 주파수 영역을 사용하는 방안으로, 다음과 같은 기술들이 있음  
  -. 주파수 공유 접속 (LSA: Licensed Shared Access) : 이동통신 이외의 다른 서 비스에서 사용하고 있는 주파수 대역이지만 지역적/시간적으 로 사용이 없을 때 이를 이동통신 주파수로 활용하기 위한 공유 기술  
  -. SDL (Supplemental Down Link) : FDD를 고려한 상하향 링크 쌍을 수용하기 위한 주파수 대역 (paired band) 확보가 어려워 트래픽이 더 많은 하향 링크용 대역만 확보하고 이를 주파수 집성기술 (CA: Carrier Aggregation)로 활용하는 기술  

##### ※ LSA  
Licensed Shared Access  

##### ※ SDL  
Supplemental Down Link  

##### log-distance 경로 손실 모델 : 
[![img](https://sites.google.com/site/rokthesis/_/rsrc/1482456589473/2-gwanlyeon-yeongu/2-2-gyeonglo-sonsil-model/2-2-1-log-distance-gyeonglo-sonsil-model/1.jpg)](https://sites.google.com/site/rokthesis/2-gwanlyeon-yeongu/2-2-gyeonglo-sonsil-model/2-2-1-log-distance-gyeonglo-sonsil-model/1.jpg?attredirects=0)
여기서, PL은 평균 경로손실이며, n은 평균 경로 손실 지수로써 주위환경과건물의 구조에 따라 값이 달라진다. d는 송수신기 사이의 거리이며, *𝑋𝜎* 는 표준편차를 갖는 제로평균 대수 정규분포이다.

##### 다중벽 경로 손실 모델 : 
[![img](https://sites.google.com/site/rokthesis/_/rsrc/1482456886160/2-gwanlyeon-yeongu/2-2-gyeonglo-sonsil-model/3.JPG?height=103&width=872)](https://sites.google.com/site/rokthesis/2-gwanlyeon-yeongu/2-2-gyeonglo-sonsil-model/3.JPG?attredirects=0)
여기서, n*f* 는 송수신기 사이에 존재하는 벽의 개수, n*w* 는 송수신기 사이에 존재하는 층의 개수, 그리고 a*f* 는 층간 손실계수, l*wi* 는 벽의 종류에 따른 손실을 나타낸다.

##### 정지된 이동 노드의 위치를 추정  
  -. 남궁현, 임일권, 이재광. iBeacon을 활용한 측위 시스템 위치추정 기법. 한국정보통신학회논문지, 19(4):925-932, 2015.  
  
# References  
- path loss calculator (https://www.pasternack.com/t-calculator-fspl.aspx)  


# patents

https://patents.google.com/patent/WO2016111524A1/ko  
무선통신시스템에서 채널상태를 추정하는 방법 및 이를 위한 장치  

https://patents.google.com/patent/WO2013051824A1/ko  
무선 통신 시스템에서 상향링크 전송 전력을 제어하는 장치 및 방법  
