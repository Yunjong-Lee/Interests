# Quantum Computing
※ 양자컴퓨터 제어 기술, 전자통신동향분석 제36권 제3호 2021년 6월  
  
    
      
      
- 개념 및 응용  
  + 개념 : 중첩, 얽힘, 간섭 등 양자역학적 특징을 응용하는 컴퓨팅 기술로, 연산량 및 연산 속도를 크게 증가시킴  
  + 응용 : 암호학, 신소개 개발 등 활용가능  
  
- 핵심 알고리듬  
  + 쇼어 알고리듬 : P.W. Shor, “Algorithms for quantum computation: Discrete logarithms and factoring,” in Proc. Annu. Symp. Found. Comput. Sci., Santa Fe, NM, USA, Nov. 1994, pp. 124-134.  
    ㄴ. 빠른 소인수 분해(암호 해독)  
    ㄴ. 양자 푸리에 변환을 이용하여 RSA 알고리듬 해독  
  + 그로버 알고리듬 : L.K. Grover, “A fast quantum mechanical algorithm for database search,” in Proc. Annu. ACM Symp. Theory Comput., Philadelphia, PA, USA, May 22-24 1996, pp. 212-219.  
    ㄴ. 빠른 탐색 및 최적화  
    ㄴ. 찾고자 하는 값의 확률진폭을 증폭시키는 과정을 반복하여 고전 알고리즘 대비 복잡도↓  
    
- 구성  
  물리계층 및 논리계층으로 나눌 수 있다.  
  + 물리계층  
    ㄴ. 양자 오류 정정 프로세서를 이용하여 양자역학에 기반한 연산 수행  
    ㄴ. 하나의 unit을 형성하여 논리계층과 연결  
    
  + 논리계층  
    ㄴ. 양자 알고리듬에서 요구하는 논리 연산을 수행할 수 있도록 양자 연산을 재조정하거나 양자 알고리듬을 효과적으로 수행할 수 있도록 물리적인 배치를 조정하는 역할  
    
- 양자 칩에 있는 큐비트를 구현하는 방법  
