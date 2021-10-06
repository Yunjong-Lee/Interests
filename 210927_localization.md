# 이동통신 신호를 이용한 보행자 위치인식 기술  

- 보행자를 위한 실내항법서비스
  + WiFi(신호세기를 거리로 변환) 기반 삼각측량  
  + RF 신호의 감쇄 기반 거리 측정  
  + 핑거프린팅  
    - 서비스 지역에서 미리 임의로 여러 개의 위치를 선정하고 선정한 위치에서 수집한 신호 세기 정보를 DB화하여 matching을 통한 위치를 추정하는 방법  
    - HMM(Hidden Markov Model)으로 표현 가능  
      → 과거의 측위 결과를 반영하여 현재의 위치 측위 정확도를 향상시키는 기법  
      → 여기서 은닉된 상태(hidden state)라 함은 관찰된 값은 있지만 어느 상태에서 해당 값이 관찰됐 는지는 알지 못함을 의미 
      
    ![img](http://fulltext.earticle.net/Data/Org/108/Content/2019/vol_5540/KITS-18-5-156_F3.gif)  
    <Fig. 3> Hidden Markov Model  
      
        
    ![img](http://fulltext.earticle.net/Data/Org/108/Content/2019/vol_5540/KITS-18-5-156_F4.gif)  
    <Fig. 4> State transition of the HMM  
    
    - 장점  
      → 실내환경의 경우, RF 측정치의 잠음 수준이 매우 크고, 전파의 직진성 보장이 어렵기 때문에(multipath propagation) 삼각측량 보다 많이 이용됨 
    - 단점  
      → DB 생성의 어려움 및 사용 제한적  
      + 환경 변화 또는 RF 채널 환경 변화에 의해 쉽게 왜곡/변화되므로, DB map 유지/보수 어려움  
        → cloud sourcing 기법(일반사용자들의 정보를 활용하는 기법) 활용시 개선될 수 있으나, RF 신호의 quality monitoring이 어려워 구현이 어렵다.  
      + RF 신호 세기 정확도 문제  
        → 높은 잡음 수준  
        → 거리에 따른 신호 세기의 감소(거리가 멀수록 변별력이 약해짐) : 많은 수의 RF 신호원 필요  
      +  
  + 스마트폰의 센서들을 활용하여 연속적인 측위를 진행하는 기술
    - 보행자 추측 항법(Pedestrian Dead Reckoning)  
      → 이동 거리에 따라 오차가 누적되는 특징이 있어 단독 사용보다 다른 측위방법을 보완하기 위해 사용
    - 보행자 추측 항법+무향 칼만필터
    - 목표 지역에 미리 구축된 지자기 맵+라디오 핑거프린트+보행자 추측 항법  
      → 각 기법의 결과를 비교 및 보정
  +  
