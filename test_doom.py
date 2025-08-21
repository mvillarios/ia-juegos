import os
import time
import random
import vizdoom as vzd

game = vzd.DoomGame()
game.load_config(os.path.join(vzd.scenarios_path, "my_way_home.cfg")) # or any other scenario file

# Opciones Visuales
game.set_window_visible(True)
game.set_mode(vzd.Mode.ASYNC_PLAYER)
game.set_screen_resolution(vzd.ScreenResolution.RES_640X480)
game.set_screen_format(vzd.ScreenFormat.RGB24)
game.set_render_hud(True)
game.set_render_crosshair(False)

game.init()

episode_count = 500

for episode in range(episode_count):
    game.new_episode()
    total_reward = 0

    while not game.is_episode_finished():
        state = game.get_state()

        # Accion aleatoria sobre el espacio de acciones
        n_buttons = game.get_available_buttons_size()
        action = [random.randint(0, 1) for _ in range(n_buttons)]

        reward = game.make_action(action, 4) # Ejecutar la acción por 4 ticks

    
    print ("Recompensa total del episodio {}: {}".format(episode + 1, game.get_total_reward()))

game.close()