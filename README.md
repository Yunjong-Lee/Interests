# Hybrid Radar System  

- 특징 : “레이더의 기본 기능”과 “RF Signal Detection”을 포함하는 Hybrid 레이더  
- 목적: 주차장이나 좁은 골목 등에서 주행중인 차량방향으로 사람/자동차 등 움직이는 object가 차량 주행방향과 교차되는 경우를 사전에 예측하여 사고를 방지 또는 최소화  
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



##### [211210] 
1. Doppler Effect
  - 정의  
    : 음파 또는 전파의 발생지/수신지가 다가오거나 멀어짐에 따라 수신 주파수가 변화하는 현상
     - 발생점,관측점이 다가올(멀어질) 때 → 수신 주파수가 높아짐(낮아짐)  

  - 도플러 효과 관계식 - 1차원 직선 관계  
    : 이동 파원, 이동 관측자 일 때,  
     ![img](http://www.ktword.co.kr/img_data/2621_4.JPG)  

    : 정지 파원, 이동 관측자 일 때,  
  ![img](http://www.ktword.co.kr/img_data/2621_2.jpg)  
     
    : 이동 파원, 정지 관측자 일 때,  
  ![img](http://www.ktword.co.kr/img_data/2621_3.JPG)
     
  ※ 한편, 빛과 같은 전자기파는 상대론적 고려가 있을 경우 다른 관계식을 따름  
     - 광속은 광원,관측자 이동에 무관하게 일정함  
     ![img](http://www.ktword.co.kr/img_data/2621_1.JPG)  
         . fr : 수신 주파수, v : 이동체 접근 속도, c : 빛 속도, f : 송신 주파수  

  - 도플러 효과 관계식 - 2차원 평면 관계 (각도 고려 필요)  
    : 이동 파원, 정지 관측자 일 때,  
     ![img](http://www.ktword.co.kr/img_data/2621_5.jpg)  
     -  t > 0 : 파원 속도가 양수 즉, 파원이 멀어짐  
     -  t < 0 : 파원 속도가 음수 즉, 파원이 가까워짐  

  - 이동 무선 채널 상의 도플러 효과  
    : 이동 무선단말의 도플러 효과에 따른 주파수 천이량  ☞ 도플러 천이(Doppler Shift) 참조  
    : 무선단말 이동에 따른 도플러 효과에 의해 주파수 변동 특성  ☞ 도플러확산 참조  
     - 다중경로 채널의 시변(時變) 특성 => 도플러 확산 (Doppler Spread) 또는 주파수 분산 초래  
  
2. 도플러 효과에 의한 주파수 변동  
  - 정의  
    . 도플러 천이 (Doppler Shift, Frequency Shift): 무선통신에서 도플러 효과(Doppler Effect)에 따른 겉보기 주파수의 천이/편이  
    . 도플러 주파수 옵셋 (Doppler Frequency Offset): 레이더 등에서의 송신,수신 주파수 간의 차이/편차  

  - 이동 무선단말의 도플러 천이(Doppler Shift, Frequency Shift) 근사 관계식  
    . 이동에 따른 도플러 효과에 의한 겉보기 수신 주파수의 변동 측도(measure)  
     - 도플러 천이는 이동체의 속도, 수신전파 주파수, 전파도래각도(AoA)와 관련됨  
        . θ = 0˚  (전파방향과 반대)  
           ..  fD = (+) (v f / c)  = (+) (v / λ)  
        . θ = 90˚ (전파방향과 수직)  
           ..  fD = 0  
        . θ = 180˚(전파방향과 같음)   
           ..  fD = (-) (v f / c)  = (-) (v / λ)  

     - 도플러 천이(주파수 천이)는 이동방향이 전파방향과 반대면 양(+)/같은 방향이면 음(-)/수직이면 거의 변화없음  

  - 최대 도플러 주파수 천이 근사식 (cos 0˚ = 1)  
     - fDmax : 최대도플러주파수천이, v :이동 속도, c : 빛 속도, fo: 전송 주파수  
     - 최대 도플러 천이는, 전송 주파수 및 이동 속도가 커질수록 커지게 됨  
