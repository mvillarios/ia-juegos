import gymnasium as gym # Importa la libreria gymnasium

# Initialise the environment
env = gym.make("LunarLander-v2", render_mode="human") # Crear el entorno con gym.make
# El id del entorno es "LunarLander-v3"
# render_mode="human" permite visualizar el entorno. rgb_array es para entrenamiento o pruebas sin visualización.

# Reset the environment to generate the first observation
observation, info = env.reset() # Resetea el entorno al estado inicial y obtiene la primera observación
for _ in range(1000): # Loop for 1000 steps
    # this is where you would insert your policy
    action = env.action_space.sample() # Elige una accion aleatoria valida del entorno, en un agente de verdad aqui iria la politica/red neuronal

    observation, reward, terminated, truncated, info = env.step(action) # Avanza un paso en el entorno con la accion elegida

    # Print the current observation and reward
    print(f"Observation: {observation}, Reward: {reward}")                                                    

    # If the episode has ended then we can reset to start a new episode
    if terminated or truncated:
        observation, info = env.reset()

env.close()