# Funcionamiento interno de los grandes modelos de lenguaje

## Resumen

Comprender cómo funcionan los grandes modelos de lenguaje (LLM) como GPT, LLAMA y otros similares es clave para aprovechar al máximo la inteligencia artificial moderna. Estos modelos usan procesos matemáticos avanzados y redes neuronales complejas que hacen posible analizar y generar lenguaje con alta precisión.

## ¿Qué significa tokenizar el lenguaje?

Tokenizar significa dividir el lenguaje humano en pequeñas unidades llamadas tokens, ya sean palabras, sílabas o letras. Aunque parezca infinito, en realidad, el lenguaje posee un número limitado de estas pequeñas unidades:

* El inglés, por ejemplo, utiliza aproximadamente 50,000 tokens.
* Los grandes modelos (como GPT-4) pueden abarcar hasta 256,000 tokens diferentes.

Estos tokens se organizan en espacios multidimensionales según su relación con otras palabras. Palabras con conceptos similares permanecen cercanas unas a otras en estos espacios.

## ¿Cómo funciona el sistema de vectores en LLM?

Cada palabra se representa mediante un vector numérico, que indica su relación con otras palabras. Por ejemplo:

* Vector mujer está muy cerca al vector hombre en términos similares al vector reina y rey por la dimensión de género.
* Palabras como caminé y caminar se sitúan próximas por compartir el vector de tiempo verbal.

Este método permite operaciones matemáticas entre palabras:

* Mamá menos género equivale a pariente.
* Regente más mujer equivale a reina.

## ¿Qué papel juegan las redes neuronales?

Las redes neuronales detectan patrones en la manera en la que las palabras (tokens) aparecen relacionadas en textos reales (llamados corpus de datos).

* Un 70% del corpus es para entrenar la red y un 30%, para probar su efectividad.
* Las redes neuronales poseen capas ocultas que ajustan constantemente valores para reconocer patrones en textos.

Gracias a estos patrones, aprenden cómo las palabras suelen combinarse naturalmente (por ejemplo: después de "yo" generalmente viene "amo") y permiten generar textos coherentes de forma autónoma.

## ¿Qué es la atención y cómo mejora la predicción del lenguaje?

El modelo de atención ayuda a decidir qué palabras anteriores son relevantes para predecir una palabra posterior. Se basa en:

* **Consulta (query)**: el último token escrito (ejemplo: "perro").
* **Llave (key)**: palabras relacionadas cerca de este último token ("gato", "maulla").
* **Valor (value)**: una ecuación matemática que usa esta cercanía para calcular probabilidades y decidir la próxima palabra posible (en este caso, "ladra").
Así, no se analizan todas las palabras, solo aquellas más relevantes, optimizando la eficiencia del modelo.

## ¿Cómo entrenan y ajustan los modelos para comportarse como Chats?

Inicialmente, estos modelos solo autocompletaban textos, no sostenían conversaciones. El proceso RLHF (Reinforcement Learning with Human Feedback) permitió transformar estos modelos en verdaderos chats al recompensarles para que interactuaran y respondieran adecuadamente.

OpenAI, por ejemplo, empleó a miles de personas para enseñar al modelo cómo realizar conversaciones naturales y eficaces.
Este entrenamiento les permite adaptarse para distintas respuestas, no siempre eligiendo la opción más probable, impulsando la creatividad.