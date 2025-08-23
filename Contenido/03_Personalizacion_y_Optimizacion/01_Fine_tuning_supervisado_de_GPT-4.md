# Fine tuning supervisado de GPT-4 con datasets médicos

## Resumen

La técnica supervised fine tuning permite ajustar modelos preentrenados como GPT-4 usando conjuntos específicos de datos. Esto es clave cuando modelos generales como ChatGPT carecen de respuestas adecuadas por limitaciones en su entrenamiento inicial.

## ¿Qué es el fine tuning supervisado en la inteligencia artificial?

El fine tuning supervisado significa entrenar un modelo preexistente suministrando claramente tanto el dato como la respuesta esperada. El modelo ajusta sus pesos mediante procesos llamados forward pass y backward pass, procedimientos explicados previamente y esenciales para adaptar el modelo al nuevo contexto.

## ¿Para qué sirve aplicar fine tuning con GPT-4 en OpenAI?

Esta técnica permite darle al modelo la habilidad de responder preguntas específicas que inicialmente no podría contestar bien debido a la limitación de su entrenamiento original:

* Adaptar respuestas a contextos especializados como medicina.
* Incrementar la precisión y calidad de respuestas.
* Controlar extensiones de textos generados para eficiencias mayores y costos operacionales menores.

## ¿Cómo preparar un dataset para fine tuning de GPT-4?

El proceso anterior a la ejecución del fine tuning implica una serie de etapas esenciales para asegurar la calidad del modelo entrenado:

1. **Análisis inicial** del conjunto de datos identificando duplicados, respuestas truncadas, o contenido inapropiado.
2. **Eliminación de registros no óptimos** como entradas duplicadas, información incompleta o expresiones problemáticas mediante herramientas como expresiones regulares con Pandas.
3. **Transformación y formateo del dataset** según la estructura admitida por OpenAI, con campos claramente definidos para roles de asistencia, usuario y sistema.

## ¿Qué tipo de ajustes se requieren para un entrenamiento exitoso?

Algunos aspectos críticos durante la limpieza y filtrado del dataset pueden incluir:

* Comprobación exhaustiva del contenido duplicado o incorrecto.
* Asegurar respuestas completas y evitar desviaciones o datos irrelevantes.
* Mantener un estándar mínimo definido (p.e., respuestas mayores a cincuenta caracteres).

Usar librerías Python como Pandas facilita enormemente estos procesos.

## ¿Qué parámetros configurar durante el fine tuning en OpenAI?

El usuario debe establecer hiperparámetros vitales que optimizan cómo el modelo aprende del nuevo dataset:

* **Batch size**: define el número de iteraciones antes de actualizar los pesos (menor número implica procesos más lentos).
* **Learning rate multiplier**: ajusta el nivel del aprendizaje para evitar mínimos locales.
* **Número de épocas**: automatizable por OpenAI o manualmente controlable para diferentes niveles de detalle en el entrenamiento.

## ¿Qué resultados esperar tras el proceso de fine tuning?

La plataforma OpenAI proporciona múltiples métricas relevantes:

* Cantidad de tokens utilizados, directamente vinculados al costo económico.
* Gráficas detalladas mostrando comportamento de métricas como pérdida (loss) en entrenamiento y validación.
* Precisión (accuracy) del modelo con el conjunto de pruebas (test dataset).

Además, OpenAI ofrece distintas etapas del modelo que permiten comparar rendimiento versus el modelo original mediante la interfaz del Playground, facilitando actualizaciones incrementales para optimizar resultados con iteraciones adicionales sobre el dataset original.

[CODIGO](./Codigos/01_Introduccion_al_Fine_Tuning.ipynb)

[REGRESAR](../03_Personalizacion_y_Optimizacion/Intro.md)