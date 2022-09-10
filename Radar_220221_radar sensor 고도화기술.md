# Radar Fundamental
### Radar 구분
- 전자파 송신 형태 (송신파 연속성 여부에 따라 구분)
  + continuous-wave radar : 연속적인 정현파를 송/수신, 상대적으로 구조 단순
    - 하나의 주파수를 가진 파형을 송신 할 경우, 송신 신호가 Target을 맞고 반사 되어진 신호의 Doppler 주파수를 분석하여 Target의 신호와 방향을 파악 (스피드건, 고도계 등)
    - Target의 거리 정보를 얻을 수 없음
      + 거리 정보를 얻기 위하여 FMCW, MFSK 등 방식을 이용
  + pulse radar : 비행물체 감지 등 비교적 복잡
    - 송신 펄스폭은, 0.1~10 ㎲, 수 ㎱, 수 ㎳ 정도, 휴지기간은, 1 ㎲ ~ 10 ㎳ 정도
    - 중요 parameters
      + Pulse Width
      + PRI(Pulse Repetition Interval)  = 1/PRF(Pulse Repetition Frequency)
      + Duty Cycle(Pulse Width/Period of pulse)
      + Peak Power
      + Carrier (Wave) Frequency

- 신호처리 방식 분류
  + 넌 코히런트 : 진폭 및 시간지연 탐지(송수신 위상 변화 탐지 불가)
    - 지도 배경에 2 차원적 표시 제공
    - 표적을 식별하는 운용자 능력에 주로 영향을 받음
  + 도플러 레이더 (코히런트)    : 진폭, 시간지연 및 송수신 위상 변화 모두 탐지 가능
    - 송수신 상대적 움직임(이동 속도, 방향) 등도 감지 가능
    - 표적 운동 특성 및 영상화 능력 가능

### [radar sensor 고도화 기술](https://itfind.or.kr/WZIN/jugidong/1993/file8797866716529755485-199301.pdf)

- 거리, 각도, 속도 해상도 향상을 위한 방안  
  + 거리: 넓은 주파수 대역폭 필요(24GHz → 76~81GHz). 추가로, 안테나, 송수신 소자 설계, 데이터 실시간 처리 기술 필요  
  + 각도: 많은 개수의 수신 안테나 필요.  
               (시분할 MIMO 기술 기반 안테나적용으로 3D cloud point 생성)  
  + 안테나, 송수신회로 및 ADC, 신호처리 단 동기화 기술  
  + 객체의 움직임으로 송신 안테나 스위칭 동안 가상 채널에 수신된 신호들 간 위상차 발생. 이를 보상하기 위한  신호처리 알고리듬 필요  

다중 radar 네트워크 기술  
: 자율 주행을 위한 여러 대의 radar 이용 전방위 상황 탐지  
  - 다중 radar간 동기화 기술(surround 영상 생성 기술) 필요  
  - 중첩 구간을 처리하는 기술  필요  
  - 통합 전파 영상 생성 기술  

4D 영상 기반 객체 인식 radar  
: 레이더에서 탐지된 각 포인트마다 도플러 스펙트럼을 함께 추출  
: 객체 인지율 향상  
: 전파영상과 도플러 성분을 이용한 radar 맞춤형 ML 신호처리 기법 필요  


- - -

자율주행 필요 기능  

라이다 센서의 출력과 같이 모든 객체로부터 반사된 다중 산란점을 포인트-츨라우드로 생성하는 기술[9](https://www.mdpi.com/1424-8220/19/5/1136)  
  - 장점) 포인트 별 도플러 성분을 이용하여 다중 객체 분리 가능  
  - 단점) 낮은 해상도(광학 센서 대비)   
그리드-맵 기술  
: 자율주행을 위해 계획된 경로를 따라 이동  
: 포인트-클라우드 산란 정보를 기반으로 도로 가장자리 추정(도로 구별)  
: 장점) 원거리에 대한 top-view 형태의 맵 생성 가능(거리 정밀도가 높음) 및 정지객체와 이동객체 구분(도플러 탐지 성분 활용) 맵 매핑  
  - edge 추정: 차량 속도와 각 산란점의 도플러 성분 비교  

객체 인지 및 분류  
: 거리+각도 탐지(현 Radar) ==> 거리+각도+구분(거리+각도 + 각 산란점의 도플러 스펙트럼 이용, 보행자 이륜차, 차량 등 구분)  
: 차량의 바퀴로부터 반사된 마이크로 도플러 신호 분석→타깃 차량의 바퀴 위치 추정[14], 차량의 크기 및 운전 방향 예측  

[7] Zhengyu Peng, “Portable Microwave Radar Systems for Short-Range Localization and Life Tracking: A Review,” MDPI, Sensors, Vol.19, No.5, Mar. 2019.  
[14] D. Kellner et al., “Wheel Extraction based on Micro Doppler Distribution using High-Resolution Radar,” IEEE, MTT-S International Conference on Microwaves for Intelligent Mobility, Apr. 2015.  


#### 추가 검토 필요 기술
- 포인트 클라우드 변화량 비교를 통한 동적환경 인식, 2019-0154812  
- 입자 군집 최적화를 이용한 무인 비행체의 최적 경로 생성 방법, 2020-0031573  

- - -

#### [Portable Microwave Radar Systems for Short-Range Localization and Life Tracking: A Review (Published: 6 March 2019)](https://www.mdpi.com/1424-8220/19/5/1136/htm)  
- short range localization and life tracking applications: medical care, CE, ADAS, indoor robots, drone navigation, etc  
- this paper review the recent advances in CW Radar system for short range localization and life tracking applications  
- Researchers have been working on radar applications in **through-wall detecting** [7,8], **indoor localization** [9], **driver assistance** [6,10,11], and **bio-medical applications** [12,13,14,15], etc. (short-range and indoor localization have also been a hot research topic [18,19,20,21,22,23])  
  + camera-based localization: some difficulties in getting accurate depth information of targets  
  + beacon-based solutions and inertial sensors: require the targets to carry the devices all the time  
  + radar sensor: 
    - operational at all the different weather conditions for autonomous driving  
    - remotely detect and monitor tiny vital signs (respiration and heart rate)
        + contrastly, current vital sign measurement devices and wearable technologies require the subject to have direct contact with the devices during the measurement, which affect the accuracy of the measurement results.  
        + 
  + 
- category: waveform type
  + Doppler radar or interferometry radar utilizes a single tone waveform to obtain motion information caused by the Doppler effect [3,40]
    - simple signal processing
    - superior accuracy in motion and displacement measurement (doppler radar)
    - very good option for applications (vital sign detection [41,42,43], sleep monitoring, mechanical vibration detection, structural health monitoring [45,46], etc)
      : do not require range information 
  + FMCW radar uses a modulated CW to sense both the range and doppler information of target
    - better candidate for applications that require range information (localization, fall detection, life activity monitoring and gesture recognition)
    - detect vital signs with the presence of multiple targets (additional range information)
- 
