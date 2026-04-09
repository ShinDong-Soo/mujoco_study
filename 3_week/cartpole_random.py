# 그냥 랜덤으로 플레이 화면만 보기
# 구조만 정확히 이해

import gymnasium as gym

env = gym.make("CartPole-v1", render_mode="human")
obs, info = env.reset()

# 핵심
for _ in range(300):
    action = env.action_space.sample()
    obs, reward, terminated, truncated, info = env.step(action)

    if terminated or truncated:
        obs, info = env.reset()

env.close()

'''
현재 상태를 본다
행동을 고른다
실제로 행동한다
결과를 받는다
'''