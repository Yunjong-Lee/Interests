# 지능형 레이더 기술 동향(Trends in Intelligent Radar Technology)
- 전자통신동향분석 제36권 제2호 2021년 4월

**Abstract** intelligent radar sensors are applied in manu industries applications, such as automobile, aerospace, and various management (traffic, weather, security and survelliances). Furthermore, they are used in smart environments including city, home, and buinding (intelligent motion sensing). ETRI introduces a phased array based intelligent radar for drone detection and human detection radar technology.  

current applications
- ADAS sensor
- motion sensor for home/building/city
- drone, flying car

과힉기술정보통신부 진행 상황: 전파연구센터 지정 및 기술 개발 중
  - 전파 해석 SW 및 플랫폼 개발: 전파응용시스템의 성능분석과 설계를 위한 전파 및 시스템 통합 해석을 위한 SW 및 platform 개발  
    + 전파 응용 시스템 해석 SW: 안테나 특성, 인체 전자파 영향, 실내·외 전파반사, 시스템 성능 분석 등
    + platform: 물체 인식이 가능한 정밀 영상 레이더와 통신 기능을 동시에 수행할 수 있는 융합시스템(상황 인식과 센싱 정보 활용 통신(예: V2X) 및 협동 레이더)
 - 자울주행 센서, 실내 네비게이션, 재난 구조, 보안 등을 위한 지능형 레이다  
  - 기존 레이다 센서가 제공하지 않았던 3차원 빔포밍, 가변 레이더 SoC 등

1. ADAS Radar (mm Radar)
  보행자, 다른 차량, 가드레일 등의 속도/방향 추적(차량 주변), 물체 및 장애물 탐지(원거리)  
  Advantage : 야간, 악천후, 장거리(200m 이상) 적용 가능  
  L.5 차량에 32개 이상 장착 예상  
  - Applications : ACC, FCW, BSD, LCA 등  
  ※ LiDAR의 경우, 안개 상황에서 데이터 수집(수분과 산소 농도가 물체 감지 능력에 미치는 영향), 역광 상황 해결 필요  
  - maker  
    + chip 
      : 경량화, 소형화, 저비용, 기능 통합화(기능별 단일 칩에서 다양한 ADAS 기능 구현이 가능한 통합 칩)
      : RF board (Monolithic Microwave Integrated Circuit, MMIC) + main board (PMIC+MCU) + Antenna
        - MMIC : 인피니언, NXP반도체, ST마이크로일렉트로닉스
        - Antenna : 컨티넨탈, 보쉬
        - PMIC : 인피니언, 보쉬, NXP
        - MCU : 인피니언, 보쉬
    + module
      : 성능/가격별 이원화 예상  
        - 고성능 : 다수 ant + 다수 MMIC + 다수 PMIC와 DL 기능을 갖춘 ECU  
        - 저비용 : 1 MMI (or MCU) + ant + PMIC  
    + system
- 
2. 지능형 motion Sensing (지능형 레이다)  
  그림자, 광선, 빗방울, 곤충의 움직임과 같은 거짓 정보에 민감하지 않음  
  영상 정보를 통해서 얻을 수 없는 물처의 정확한 위치 및 움직음(속도, 방향 등) 제공, 사생활 보호 (카메라 기반 감시시스템 보완 가능)  
  - Applications : 조명제어, 자동문 개폐, 보안 경보 등  
  - maker  
    + 인피니언(60GHz, 도플러) XENSIVTMBGT60LTR11AIP : ISM 밴드에서 동작, 5mW 미만의 전력 소비, 5m 이내의 사람 감지(mobile device 또는 홈 디바이스 등에 적용시 움직임 감지 시 시스템 가동)  
    + BGT60LTR11AIP 단일칩 초고주파 MMIC (인피니언)의 경우, Antenna(1 tx/1 rx)를 패키지에 내장(AIP),  3.3×6.7×0.56mm의 소형 패키지  
  - 드론 식별 레이다 (안티 드론) 
    - Frequency : x-band   
    - 탐지거리 : ~1.5km  
    - azimuth/elevation (º) : 90 / 45  
    - 각도/거리 분해능 : 5º/1m
    - 최대탐지 속도 : 100km
    - 능동위상배열
    
3. 지능형 트래픽 레이더  
  비트센싱, ITS 평가 최상등급 인정('19)  
  24GHz 레이더 + FHD 카메라 결합 DL 모델 경량화 기술 적용 교통정보 실시간 모니터링, 추가로 IoT 기능 내장(교통 정보 서버 전달로 교통량 예측 등 빅데이터 사업 확장 가능)   
  
4. Personal Air Vehicle (PAV) 자율비행 기술
  ※ 한국형 도심항공교통(K-UAM) 로드맵, 도시 권역 30~50km의 이동 거리 비행 목표
  승용차 1시간 이동시 40분 시간 절약 가
  issue 
  - 주변상황 판단 및 통제 기술 및 안정성, 무게, 배터리 용량, 소음 및 항공 교통정리와 인프라 구축 등
  - 주변 물체 인식/분석 기술 등 고도의 센싱 기술, AI 기술, 네트워크 기술
  
5. algorithm
  드론 탐지용 조류 분류 (블레이드의 회전과 날갯짓에 따른 도플러 변이에 대한 특성 비교
  
6. Through The Wall Radar
  IR-UWB 기반, 연기, 벽 및 붕괴된 파편으로 인해 제한된 시야 등 특정 환경에서 물체 인식  
  

