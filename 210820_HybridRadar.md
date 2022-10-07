# Radar for hidden Object detection @ 221007

- 특징 : 
- 목적 : 주차장이나 좁은 골목 등에서 주행중인 차량방향으로 사람/자동차 등 움직이는 object가 차량 주행방향과 교차되는 경우를 사전에 예측하여 사고를 방지 또는 최소화

- Object 검출 방법
  - 1. tx Ant.를 통해 기준 각도(0도)로 신호를 방사하여 물체에 반사되어 돌아오는 신호를 수신한다. 이 신호를 기준 반사 신호라 하고,
  - 2. tx 방사 각도를 조정하여 기준각도와 다른 각도로 신호를 방사하여 물체에 반사되어 돌아오는 신호를 수신한다. 이 신호를 왜곡 반사 신호라 한다.
  - 기준 반사신호와 왜곡 반사신호를 비교하면 왜곡 반사신호의 경우 왜곡된 각도와 비례하는 도래각을 가지게된다. 
  - 3. 도래각 계산한다.
    + 도래각 계산을 통해 전방의 물체가 다이렉트 경로에 존재하는지 반사 경로에 존재하는지 확인된다.
  - a → b → c 과정을 반복하면 누적하면 물체의 이동 및 ghost 등을 판단 할 수 있다.

<br>  
 
# Hybrid Radar System  
  
- 특징 : “레이더의 기본 기능”과 “RF Signal Detection”을 포함하는 Hybrid 레이더  
- 목적 : 주차장이나 좁은 골목 등에서 주행중인 차량방향으로 사람/자동차 등 움직이는 object가 차량 주행방향과 교차되는 경우를 사전에 예측하여 사고를 방지 또는 최소화  
- 기능  
- 구조  
그림 4.
- N-LOS object 검출 방법  
  RF Signal Detection 기능을 활성화시켜 주변의 RF 신호들을 수신하여 RSRQ(RSSI,LQI, RS 등) 등 신호세기를 측정 및 tracking하여 주행중인 상황에서, 차량 주변에 움직이는 물체를 추정  
  
  .. 보행자(or 자동차)가 P0에서 P1 방향으로 이동 중이고, 자동차 V1이 주행(직진) 중 일 때
RF signal 검출영역(우측)에 근접하면 RF signal이 검출되며(RF signal 검출영역(좌측)에서는 검출이 안됨) RF signal의 세기는 낮다.
P0 에서 P1 방향으로 이동하면서 RF signal의 세기는 점점 증가됨
RF signal 세기를 기반으로 접근 속도 추정 및 V1의 속도 및 핸들각을 이용하여 충돌 가능성 판정
RF signal 세기를 기반으로 정지 상태의 물체와 이동 상태의 물체 추정 가능

  
  ![image-20210820181953059](C:\Users\Administrator\AppData\Roaming\Typora\typora-user-images\image-20210820181953059.png)
  
  
- LOS object와 N-LOS object 구별  
RF Detector로 검출된 object 중에서 Radar로 검출된 object 제거 방법  
RF Detector로 검출된 신호 중에서 기지국 신호 구분  
RF Detector로 검출된 신호 중에서 LOS 신호 구분  
RF Detector로 검출된 object의 신호 세기와 Radar로 검출된 object의 신호 세기 및 방향 정보로 추정함  




