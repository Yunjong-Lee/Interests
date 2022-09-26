# index

---


# [ROS](https://m.blog.naver.com/PostView.naver?blogId=rich0812&logNo=221465680514&targetKeyword=&targetRecommendationCode=1)  


# SLAM  
  기하학적 SLAM과 Deep learning 기반 SLAM으로 구분

### 1. 기하학적 SLAM  
  임의의 환경에서 획득한 영상 시퀀스로부터 기하학적 계산을 통해 카메라의 위치 및 3차원 지도 생성하는 기법으로, 장점은 ... 그러나, 누적오차 발생되는 단점을 가짐  

#####  1.1. 누적 오차를 줄이는 방법  
    - Filtering (확률분포를 영상 데이터를 획득할 때마다 갱신)  
      + Kalman filter  
        ㄴ 3차원 landmark의 위치를 가우시안 분포로 가정하고 영상 데이터를 획득할 때마다 가우시안 분포를 표현하는 평균 벡터와 공분산을 갱신  
        ㄴ 선형 시스템에 적합  
        ㄴ 비선형 시스템을 위한 unscented Kalman filter 기법 참고  
      + Particle filter  
        ㄴ Rad-Blackwellized particle filter + 키프레임 기법 이용  
  
#####  1.2. Optimization
    - 특징점 기반
      : 상에서 특정 화소들을 이용하여 카메라 위치를 추정하고 3차원 지도를 생성함으로써 처리속도가 빠름  
      
      + 절차 : 영상으로부터 특징점 추출 → 추출된 특징점을 영상 시퀀스에서 추적하여 초기 카메라의 위치 계산 → 3차원 지도 생성 → 랜드마크의 위치들을 카메라의 추정된 자세로 재 투영(re-projection) → 추적된 특징점의 좌표와의 거리 갱신  
      + 특징점 오정합 문제 해결 방안 : RANSAC (Random Sample Consensus)   
    - Direct SLAM  
      : 환경을 조밀하게 모델링 가능, 특징점이 없는 균질한 환경에서 성능 우수  
      
      + 절차 : 두 장의 영상으로부터 카메라의 움직임과 환경에 대한 3차원 정보 획득 → 첫 번째 영상을 두 번째 위치에서의 영상으로 변환 → 두 번째 영상과 밝기 차이 최소화  
      
### 2. Deep learning 기반 SLAM  
  오도메트리 추정(두 영상 사이의 상대적인 자세 변화를 추정)과, 매핑(주변 환경에 대한 공간 모델을 생성)으로 분류한다.
  
#####  2.1. 오도메트리(odometry) 추정  
      
#####  2.2. 매핑(mapping)  








