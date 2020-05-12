# Genetic Algorithm

 - 생물 진화 과정을 모방한 최적화 알고리즘. 
 - 1975년 존 홀랜드(John Holland)에 의해 개발되었는데, 실제 생물 진화 과정의 많은 부분을 차용하였다.
 - local solution에 빠지지 않고 global solution을 구할 확률이 높다는 장점이 있음

### 주요 용어
> - 염색체(Chromosome) : 하나의 해(solution)
> - 유전자(Gene) : 염색체를 구성하는 요소로, 하나의 유전 정보
> - 해집합(Population)  
![image](gen1.png)
> - 적합도(Fitness) : 최적화된 정도로 Loss함수를 정의하고 측정
> - 선택(Selection) : 다음 세대에 물려줄 두 개의 염색체 선택. 선택 방법에는 균등비례 룰렛 휠 선택, 토너먼트 선택 등이 있음
> - 교차(Crossover) : 랜덤으로 교차지점을 선택하여 새로운 자식을 생성
![image](gen2.png)
> - 변이(Mutation) : 생성된 자식 중 일부 유전자의 배열을 바꾸거나 값을 임의로 변경하는 등의 방법으로 돌연변이를 일으킴
![image](gen3.png)


### 순서도
![image](gen4.png)
