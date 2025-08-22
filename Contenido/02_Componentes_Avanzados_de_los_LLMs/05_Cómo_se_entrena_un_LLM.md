# Cómo se entrena un modelo de lenguaje grande (LLM) paso a paso

## Resumen

Entrenar un modelo de lenguaje grande (Large Language Model, LLM) implica un proceso extenso que combina grandes volúmenes de información, potente infraestructura tecnológica y variadas técnicas de aprendizaje automático. Comprender cómo se llevan a cabo estos pasos ayuda a aprovechar al máximo el potencial de un LLM para resolver distintos problemas o tareas específicas.

## ¿Qué es y por qué importa el corpus de entrenamiento?

El conjunto de entrenamiento o corpus es la base esencial del desarrollo de un LLM. Este dataset determina directamente qué problemas puede ayudar a resolver nuestro modelo.

* **El corpus está compuesto por textos recolectados**, generalmente vía web scraping.
* **Gigantes tecnológicos como Google recolectan datos** por años para crear datasets internos cuidadosamente curados.
* Para tener datasets de calidad, se requiere infraestructura tecnológica robusta y habilidades humanas para revisión y limpieza.

Este corpus puede llegar a tener tamaños inmensos. Por ejemplo, el modelo Lama cuatro de Meta utiliza cerca de treinta trillones de tokens, equivalentes aproximadamente a ciento nueve terabytes de información textual.

## ¿Cómo se calcula el tamaño de un corpus?

Para estimar el tamaño, se considera un token promedio de cuatro bytes. Treinta trillones de tokens resultan así en alrededor de 109 terabytes de datos textuales.

* **Es importante eliminar duplicados y contenido nocivo del corpus**, asegurando la calidad necesaria para entrenar eficazmente el modelo.

## ¿Qué es la tokenización y para qué sirve?

La tokenización convierte el corpus en unidades mínimas (tokens) que el modelo pueda procesar. Esta transformación es crucial:

* **Tokens podrían ser palabras completas, sílabas o letras individuales.**
* Se utilizan herramientas como TikToker de Hugging Face.

De esta forma, el corpus de entrenamiento es interpretado adecuadamente por el modelo.

## ¿Cómo se construye la arquitectura del LLM?

Una vez tokenizados los datos, seleccionamos o desarrollamos la arquitectura a usar:

* **La arquitectura varía según el uso específico deseado.**
* **Ejemplo:** GPT-2 consiste principalmente en capas de atención y capas de multilayer perceptron apiladas.
* Empresas como Meta hacen pública su arquitectura (open source), facilitando su replicación y adaptación.

## ¿En qué consiste el entrenamiento intensivo del modelo?

El entrenamiento computacional es la fase más costosa y prolongada:

* **Requiere miles de GPUs o TPUs distribuidos en centros especializados de procesamiento.**
* **Cada GPU procesa fragmentos del corpus** y reporta resultados, errores y ajustes al servidor central.
* **Este proceso es altamente repetitivo y dura mucho tiempo**, dependiendo del volumen de datos y tamaño del LLM.

## ¿Qué técnicas se utilizan tras el entrenamiento inicial?

Al finalizar el entrenamiento básico, el LLM aún es general. Para tareas específicas, se ejecuta una fase adicional conocida como fine tuning:

* **Consiste en reentrenar parcialmente el modelo con datos específicos.**
* **Ejemplos prácticos:** adaptación con imágenes médicas o consultas financieras.
* El tiempo de ajuste es considerablemente menor al entrenamiento inicial.

## ¿Qué es el RLHF y cómo mejora el modelo?

El *Reinforcement Learning with Human Feedback* (RLHF) introduce retroalimentación humana para ajustar el modelo según nuestras necesidades y expectativas:

* Humanos evalúan respuestas del modelo, otorgando feedback y premiando conductas correctas.
* Transformación notable: salto de GPT-3 a GPT-4 gracias a la retroalimentación humana implementada.

## ¿Qué ventajas ofrece el aprendizaje por refuerzo no supervisado?

Para reducir el esfuerzo humano, se emplean técnicas donde el modelo aprende por sí mismo, basándose en reglas predefinidas:

* **Aprendizaje offline:** El modelo adquiere comportamientos sin la intervención directa humana.
* **Ejemplo de éxito:** DeepSeek R1, haciendo que el modelo aprenda de manera autónoma, mediante técnicas avanzadas como GRP0.

![Fases de entrenamiento](https://static.platzi.com/media/user_upload/upload-44de8b52-955e-46ae-b9d0-d86affb1bda0.png)

[REGRESAR](../02_Componentes_Avanzados_de_los_LLMs/Intro.md)