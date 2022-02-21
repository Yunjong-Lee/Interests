radar sensor 고도화 기술
https://itfind.or.kr/WZIN/jugidong/1993/file8797866716529755485-199301.pdf

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

라이다 센서의 출력과 같이 모든 객체로부터 반사된 다중 산란점을 포인트-츨라우드로 생성하는 기술[9]  
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


포인트 클라우드 변화량 비교를 통한 동적환경 인식, 2019-0154812  
입자 군집 최적화를 이용한 무인 비행체의 최적 경로 생성 방법, 2020-0031573  
