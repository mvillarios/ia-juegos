from pettingzoo.atari import mario_bros_v3
import time

env = mario_bros_v3.env(render_mode="human", max_cycles=5000)  # Initialize the environment with human rendering, max cycles es el numero de pasos

env.reset()  # Reset the environment to start a new episode

for agent in env.agent_iter():
    obs, reward, termination, truncation, info = env.last()  # Get the last observation, reward, and termination status
    action = env.action_space(agent).sample() if not termination else None  # Sample a random action if the episode is not terminated
    env.step(action)

    time.sleep(0.005) # Sleep for a short duration to control the speed of the game

env.close()  # Close the environment after the episode ends