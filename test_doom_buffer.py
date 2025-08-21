import os
import time
import random
import vizdoom as vzd

import cv2

game = vzd.DoomGame()
game.load_config(os.path.join(vzd.scenarios_path, "deadly_corridor.cfg")) # or any other scenario file

# Opciones Visuales
game.set_window_visible(True)
game.set_mode(vzd.Mode.ASYNC_PLAYER)
game.set_screen_resolution(vzd.ScreenResolution.RES_640X480)
game.set_screen_format(vzd.ScreenFormat.BGR24)
game.set_render_hud(True)
game.set_render_crosshair(False)

# Enables depth buffer.
game.set_depth_buffer_enabled(True)

# Enables labeling of in game objects labeling.
game.set_labels_buffer_enabled(True)
# See also labels_buffer.py example for more explanations.

# Enables buffer with top down map of the current episode/level .
game.set_automap_buffer_enabled(True)
game.set_automap_mode(vzd.AutomapMode.OBJECTS)
game.set_automap_rotate(False)
game.set_automap_render_textures(False)

game.init()

episode_count = 500
sleep_time = 0.028  # seconds

for episode in range(episode_count):
    game.new_episode()
    total_reward = 0

    while not game.is_episode_finished():
        state = game.get_state()

        # Accion aleatoria sobre el espacio de acciones
        n_buttons = game.get_available_buttons_size()
        action = [random.randint(0, 1) for _ in range(n_buttons)]

        reward = game.make_action(action, 4) # Ejecutar la acción por 4 ticks

        # Map buffer, in the same format as screen buffer.
        # Shows top down map of the current episode/level.
        automap = state.automap_buffer
        if automap is not None:
            cv2.imshow("ViZDoom Map Buffer", automap)

        cv2.waitKey(int(sleep_time * 1000))

    
    print ("Recompensa total del episodio {}: {}".format(episode + 1, game.get_total_reward()))

game.close()