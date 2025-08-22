# RoPE: codificación posicional rotatoria para transformers

## Resumen

**🚀 Contexto rápido: En esta sección vas a ver los términos Rotary Position Embedding y Rotary Position Encoding. Queremos que sepas que ambos se refieren a la misma técnica: RoPE. No te preocupes por la diferencia en los nombres, es solo una cuestión de estilo.** En la mayoría de los artículos y recursos técnicos se usa ***Rotary Position Embedding***, pero el concepto es el mismo: una forma de incorporar la posición en los tokens a través de rotaciones en el espacio vectorial.

El **Rotatory Position Encoding (RoPE)** es una técnica esencial para lograr que los modelos Transformers, como GPT-2, reconozcan la posición específica de cada token dentro de una secuencia. Implementar RoPE mejora notablemente la precisión del modelo reduciendo la carga computacional necesaria durante su entrenamiento.

## ¿Por qué los transformers necesitan RoPE?

Los Transformers no tienen una forma natural de interpretar la ubicación exacta de los tokens en una secuencia. Esto implica que para modelos sin encoding posicional podría resultar idéntica la relación entre tokens cercanos y aquellos muy separados, llevando a una mayor demanda de cómputo para el entrenamiento. RoPE soluciona esto almacenando información sobre la posición mediante el ángulo del embedding.

## ¿Cómo funciona RoPE en la codificación de posición?

En RoPE, cada palabra o token posee un embedding que puede visualizarse en un espacio vectorial bidimensional. Aquí es donde RoPE explota la idea del ángulo:

* Cada embedding tiene un ángulo asociado respecto al eje x.
* Este ángulo (theta) codifica la posición específica del token en la secuencia.
* A medida que avanzamos en la secuencia se rota el embedding según el ángulo theta, permitiendo al modelo retener con precisión la ubicación del token.

Además, RoPE asegura consistencia manteniendo invariantes las distancias relativas entre embeddings, siempre que la cantidad de tokens entre elementos objetivo permanezca constante.

## ¿Cuál es la matemática detrás de RoPE?

RoPE utiliza matrices de rotación del álgebra lineal, en particular empleando funciones trigonométricas:

* Coseno y menos seno en la primera fila.
* Seno y coseno en la segunda fila.

Esta matriz rota los vectores embeddings para codificar su posición relativa dentro de secuencias más grandes. Dado que los embeddings típicos tienen múltiples dimensiones, se dividen en pares dimensionales para aplicar matrices de rotación eficientemente.

Para reducir la carga computacional, RoPE no multiplica directamente grandes matrices, sino que ejecuta operaciones vectoriales:

* División del embedding en grupos de dos dimensiones.
* Aplicación individual de la matriz de rotación por pares.
* Operaciones vectoriales más simples (coseno, seno, suma y producto punto).

## ¿Cómo mejora RoPE el desempeño del modelo?

Integrar RoPE facilita que el modelo entienda con exactitud la distancia entre tokens, aumentando la calidad y velocidad del entrenamiento. La reducción rápida de la pérdida durante el entrenamiento con RoPE es un claro indicador de su eficiencia y de cómo favorece el aprendizaje más ágil del modelo.

Además, ayuda al modelo a discernir qué tan próximos están los tokens en la secuencia a través del producto punto entre vectores, facilitando interpretaciones más exactas durante el entrenamiento y la inferencia.