# Arquitectura GPT-2 y mecanismo de atención en transformadores

## Resumen

La arquitectura GPT-2 y, en particular, el mecanismo de atención, constituyen elementos fundamentales para comprender cómo funcionan los actuales modelos de lenguaje llamados transformadores. Estos modelos emplean técnicas matemáticas para identificar y mantener contexto entre palabras, potenciando su capacidad predictiva y generativa en tareas del procesamiento de lenguaje natural (NLP).

## ¿Qué componentes integran la arquitectura de GPT-2?

GPT-2 se construye principalmente sobre 12 estructuras denominadas transformadores. Cada transformador incluye:

* Una multihead attention.
* Dos capas llamadas layer norm.
* Una capa feed forward.

El aspecto crucial dentro de estos transformadores es el mecanismo de atención, fundamental para mantener la coherencia contextual.

## ¿Cómo opera el mecanismo de atención?

La atención actúa examinando qué palabras previas afectan significativamente a la palabra actual. Matemáticamente se representa así:

$ Atención = \text{softmax}\left( \frac{Q K^T}{\sqrt{d_k}} \right) V $

Aquí describimos el significado de sus componentes:

## ¿Qué significa cada símbolo de la atención?

* **Q (Query)**: representa preguntas provenientes de cada palabra para identificar qué palabras anteriores influyen en su significado.
* **K (Key o llave)**: alude a respuestas aproximadas correspondientes a las preguntas generadas por las consultas (queries).
* **V (Value o valor)**: valores necesarios para modificar adecuadamente los embeddings, manteniendo el contexto correcto.

Cada componente se obtiene multiplicando los embeddings originales por matrices de pesos específicas (Wq, Wk, Wv) que se ajustan durante el entrenamiento del modelo.

## ¿Cómo interactúan estos elementos en un ejemplo práctico?

Si tomamos la frase "Me encanta el color negro, espero algún día tener un gato así", la palabra "negro" afecta directamente a la palabra "gato".

* **Ejemplo de Query (Q)**: la palabra "gato" hace una consulta específica: ¿qué palabras anteriores modifican la palabra actual?
* **Ejemplo de Key (K)**: identifica a "negro" como respuesta precisa, previamente codificada en una matriz entrenada.
* **Ejemplo de Value (V)**: ajusta el embedding original de "gato" hacia uno contextual ("gato negro"), manteniendo la información correcta.

Multiplicando Q por K obtenemos pesos que revelan qué tan relacionadas están las palabras. La operación matemática y la función de softmax reducen la escala numérica para optimizar cálculos, manteniendo la precisión y estabilidad computacional.

## ¿Cuál es el papel de la función Softmax en atención?

Softmax limita la escala numérica de los resultados de la multiplicación QK, transformándolos de un rango inicialmente amplio (desde menos infinito hasta más infinito) a uno manejable y acotado (entre -1 y 1). Esto simplifica y acelera las operaciones informáticas necesarias durante el entrenamiento.

## ¿Qué función cumple la división por raíz cuadrada de dₖ?

La división por la raíz cuadrada de dₖ no afecta directamente al aprendizaje sino que protege la estabilidad numérica del proceso computacional. Previene errores por limitaciones inherentes al hardware y su precisión numérica durante estas operaciones.

## ¿Qué otros elementos acompañan al mecanismo de atención en GPT-2?

Tras el mecanismo de atención, GPT-2 integra componentes comunes del machine y deep learning como:

* Capas layer norm.
* Redes feed-forward.
* Clasificadores tradicionales de tarea (text classifier o task classifier).

Estos elementos complementarios están diseñados para mejorar la generalización y optimizar el comportamiento del modelo.

## ¿Cómo continuar profundizando en GPT-2 y sus bases teóricas?
Para quienes desean profundizar, se recomienda explorar el documento original (paper) de GPT-2 proporcionado por OpenAI. Adicionalmente, los fundamentos teóricos sobre redes neuronales profundas, normalización y clasificadores se encuentran ampliamente documentados en los recursos adicionales brindados durante el curso.

[REGRESAR](../01_Fundamentos_de_los_LLMs/Intro.md)