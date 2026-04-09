import gymnasium as gym
from stable_baselines3 import PPO

# 1. 환경 생성
env = gym.make("CartPole-v1", render_mode="human")

# 2. PPO 모델 생성
model = PPO("MlpPolicy", env, verbose=1)

# 3. 학습
model.learn(total_timesteps=10000)

# 4. 학습된 모델로 플레이
obs, info = env.reset()

for _ in range(300):
    action, _ = model.predict(obs, deterministic=True)
    obs, reward, terminated, truncated, info = env.step(action)

    if terminated or truncated:
        obs, info = env.reset()

env.close()