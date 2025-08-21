Python Gymnasium
========================
Gymnasium es una biblioteca de Python diseñada para crear y gestionar entornos de aprendizaje por refuerzo. Proporciona una interfaz estandarizada para interactuar con diferentes entornos, facilitando el desarrollo y la evaluación de algoritmos de aprendizaje por refuerzo.

Características Principales
------------------------
- **Interfaz Unificada**: Permite interactuar con diversos entornos de manera consistente.
- **Compatibilidad con OpenAI Gym**: Muchos entornos de OpenAI Gym son compatibles, lo que facilita la transición.
- **Soporte para Entornos Personalizados**: Puedes crear tus propios entornos personalizados siguiendo la interfaz estándar.
- **Documentación Completa**: Incluye documentación detallada y ejemplos para facilitar el uso.

Instalación Gymnasium
========================
Para instalar Gymnasium, puedes usar pip. Asegúrate de tener pip instalado y luego ejecuta el siguiente comando:

```bash
pip install gymnasium
```

Paquete Adicionales
------------------------
Estos son algunos paquetes adicionales en caso de error de instalación:

```bash
pip install "gymnasium[atari, accept-rom-license]"
pip install shimmy autorom
pip install gymnasium[other]
```

Aceptar Licencia de ROMs
------------------------
Algunos entornos de Atari requieren que aceptes la licencia de las ROMs. Puedes hacerlo ejecutando el siguiente comando:
```bash
Autorom --accept-license
```

Escenarios Atari
------------------------
Para revisar los escenarios de Atari disponibles, puedes visitar la [documentación oficial de Gymnasium](https://ale.farama.org/environments/).

Instalacion Petting Zoo
========================
Para instalar Petting Zoo, puedes usar pip. Asegúrate de tener pip instalado y luego ejecuta el siguiente comando:
```bash
pip install pettingzoo
```

Es necesario instalar CMake ya que esta compilado en C++
```bash
sudo apt update
sudo apt install -y cmake g++ build-essential
```

Instalación de Dependencias
========================
Para instalar las dependencias necesarias para ejecutar los entornos de Petting Zoo, puedes usar el siguiente comando:
```bash
pip install "pettingzoo[atari]"
```

Usar el siguiente comando para instalar todas las dependencias de Petting Zoo:
```bash
pip install "pettingzoo[all]"
```

Aceptar Licencia de ROMs
------------------------
Al igual que con Gymnasium, algunos entornos de Atari requieren que aceptes la licencia de las ROMs. Puedes hacerlo ejecutando el siguiente comando:
```bash
Autorom --accept-license
```

Enlace de Documentación
------------------------
Para más información sobre Petting Zoo, puedes visitar la [documentación oficial] https://pettingzoo.farama.org/.

Instalacion ViZdoom
========================
Para instalar ViZdoom, puedes usar pip. Asegúrate de tener pip instalado y luego ejecuta el siguiente comando:
```bash
pip install vizdoom
```

Enlace de Documentación
------------------------
Para más información sobre ViZdoom, puedes visitar la [documentación oficial](https://github.com/Farama-Foundation/ViZDoom)


Ejemplos de Codigo que pueden usar
=========================
ViZdoom presenta codigo de ejemplo que puedes usar para comenzar a trabajar con el entorno y que puedes tomar inspiracion para los demas ambientes. [Ejemplo de ViZdoom](https://github.com/Farama-Foundation/ViZDoom/tree/master/examples/python)

Enlaces Extras
=========================
- [PyTorch](https://docs.pytorch.org/docs/stable/index.html): Recomendado para trabajar con ambientes de Gymnasium y Petting Zoo.
- [SMAC](https://github.com/oxwhirl/smac): Un entorno de múltiples agentes para pruebas y entrenamiento. Basado en StarCraft II.
- [Stable Baselines3](https://stable-baselines3.readthedocs.io/en/master/guide/install.html): Una colección de algoritmos de aprendizaje por refuerzo listos para usar, compatible con Gymnasium y Petting Zoo.