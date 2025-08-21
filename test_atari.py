import gymnasium as gym
import ale_py

gym.register_envs(ale_py)

# Crear el entorno de Space Invaders
env = gym.make("ALE/SpaceInvaders-v5", render_mode="human")

obs, info = env.reset()

done = False
total_reward = 0

while not done:
    # Tomar una acción aleatoria (exploración)
    action = env.action_space.sample()
    obs, reward, terminated, truncated, info = env.step(action)

    total_reward += reward
    done = terminated or truncated

print("Recompensa total:", total_reward)

env.close()
