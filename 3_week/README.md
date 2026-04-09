3. 이번 주에 꼭 남겨야 할 정리 노트

스터디용이라면 아래 6개를 꼭 적어.

1) CartPole observation 4개 의미

보통 이런 축으로 이해하면 된다.

카트 위치
카트 속도
막대 각도
막대 각속도
CartPole 문서의 설명과 관측 구조를 같이 보면 된다.
2) action 의미
0: 왼쪽
1: 오른쪽
환경 문서 기준 이산 행동 공간이다.
3) reward 의미
오래 버티는 것이 보상
누적 reward가 높을수록 잘한 것
4) episode 종료 조건
막대가 너무 기울어짐
카트가 범위를 벗어남
시간 제한 도달
Gymnasium은 terminated와 truncated를 구분해 반환한다.
5) PPO 핵심 한 줄
정책을 좋은 방향으로 업데이트하되 너무 크게 바꾸지 않게 막는 알고리즘
6) MuJoCo에서 느낀 차이
같은 “세우기” 문제여도 더 시뮬레이터스럽다
앞으로 로봇/제어 쪽으로 갈수록 MuJoCo 감각이 중요하다


1일차
Gymnasium 설치
CartPole 랜덤 실행
reset, step, obs, reward 출력해보기
2일차
Stable-Baselines3 PPO로 CartPole 학습
저장/불러오기 해보기
3일차
GPT가 만든 코드 한 줄씩 주석 달기
“환경 / 모델 / 학습 / 평가” 4블록으로 나누기
4일차
reward와 종료 조건 정리
observation 4개 의미 정리
5일차
PPO 유튜브 1~2개 보기
clip, policy, advantage 정도만 정리
6일차
MuJoCo 설치
InvertedPendulum 랜덤 실행
7일차
random disturbance 실험
스터디 발표용으로 “CartPole vs MuJoCo InvertedPendulum 차이” 정리