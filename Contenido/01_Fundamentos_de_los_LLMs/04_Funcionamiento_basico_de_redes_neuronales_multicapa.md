# Funcionamiento básico de redes neuronales multicapa

## Resumen

Las redes neuronales, específicamente los multilayer perceptron (MLP), son una tecnología esencial en machine learning. Estas redes, conocidas como feed forward, poseen estructuras claras con múltiples capas, incluyendo una capa de entrada, varias capas ocultas y una capa de salida.

## ¿Qué son las redes neuronales multilayer perceptron?

Los multilayer perceptron son redes neuronales que se componen principalmente de tres capas:

* **Capa de entrada**: esta depende directamente del problema que se enfrenta. Por ejemplo, el español con cincuenta mil palabras tendría un número idéntico de neuronas en esta capa.
* **Capas ocultas**: en estas capas se lleva a cabo el aprendizaje del modelo, permitiendo entender las características y propiedades del lenguaje o problema específico.
* **Capa de salida**: también depende del problema planteado y su número suele coincidir con la capa de entrada para tareas como predicción de palabras.

## ¿Cómo funciona una neurona en una red neuronal?

Cada neurona en las capas ocultas posee tres componentes básicos:

* **Peso (weight)**: señala la importancia de una característica específica para el modelo.
* **Sesgo (bias)**: ayuda a la red neuronal a no memorizar exacta y rígidamente los datos del entrenamiento inicial.
* **Función de activación**: permite captar patrones en los datos proporcionados, basándose en cómo se activan las neuronas del cerebro humano.

Estas neuronas realizan cálculos matemáticos partiendo de datos de entrada, que multiplican por pesos específicos. Luego se suma el sesgo, resultando en una función lineal básica, a la que posteriormente se añade una función no lineal que permite modelar comportamientos complejos.

## ¿Qué es la función de pérdida y cómo mide el aprendizaje?

La función de pérdida determina si la red neuronal está realmente aprendiendo. Básicamente, compara los resultados predichos por la red con los resultados reales conocidos, siendo el objetivo reducir esta diferencia al máximo, idealmente hasta el valor cero. Una función común para evaluar la pérdida en problemas lineales es el error cuadrático medio.

## ¿En qué consiste el método Back Propagation?

El método de back propagation (propagación hacia atrás) consiste en tomar el valor obtenido en la función de pérdida para actualizar los pesos y sesgos de la red neuronal. Este método emplea conceptos matemáticos avanzados, como derivadas y derivadas parciales, buscando mínimos locales en la función de pérdida para mejorar continuamente el aprendizaje del modelo.

## ¿Qué indica el teorema universal de aproximación?

Este teorema establece que cualquier problema que pueda formularse matemáticamente puede aproximarse mediante una red neuronal, siempre que sean usadas funciones de activación no lineales. Esto permite modelar distintos tipos de comportamientos, incluyendo curvas complejas y espacios multidimensionales.

## ¿Qué limitaciones tienen los multilayer perceptron?

Los MLP presentan dificultades para captar contextos más amplios, como frases o párrafos, algo esencial para comprender adecuadamente el lenguaje humano. Por esta razón, surgieron estructuras que manejan mejor esta complejidad, tales como:

* **LSTM (Long Short-Term Memory)**: conservan información contextual extendida.
* **CNN (Convolutional Neural Networks)**: capturan información espacial o de contexto visual.

Otra limitación relevante es el problema conocido como vanishing gradients, donde el modelo queda atrapado en mínimos locales sin importar la potencia de cálculo empleada. Técnicas como el dropout pueden ayudar a mitigar esto.

[REGRESAR](../01_Fundamentos_de_los_LLMs/Intro.md)