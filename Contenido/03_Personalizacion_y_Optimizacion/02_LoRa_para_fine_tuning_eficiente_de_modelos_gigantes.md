# LoRa para fine tuning eficiente de modelos gigantes

## Resumen

## ¿Qué es LoRa y cómo facilita el fine tuning?

¿Quieres adaptar modelos enormes como GPT-4, pero no tienes los recursos de grandes empresas? LoRa, o Low-Rank Adaptation, permite realizar fine tuning sobre modelos gigantes con menos recursos computacionales. En lugar de entrenar la totalidad de un modelo con millones o incluso billones de parámetros, LoRa entrena solamente pequeñas matrices, disminuyendo enormemente el uso de memoria y tiempo del proceso.

## ¿Por qué entrenar con LoRa y no con métodos tradicionales?

Cada nueva versión de grandes modelos lingüísticos (LLMs) aumenta significativamente la cantidad de parámetros. Entrenar todos estos parámetros sería caro y poco escalable para individuos o pequeñas organizaciones. Por ejemplo, GPT-4 tiene alrededor de un trillón de parámetros y su entrenamiento completo requeriría cientos o miles de GPUs. Aquí es donde LoRa destaca:

* Permite entrenar matrices de pesos considerablemente más reducidas (r por d en lugar de d por d).
* Reduce significativamente las operaciones por segundo necesarias.
* Facilita que cualquier usuario pueda realizar procedimientos efectivos de fine tuning.

## ¿Cómo funciona exactamente LoRa?

LoRa aprovecha la llamada hipótesis del rango intrínseco, según la cual con pocos ajustes puntuales en pequeñas matrices es posible adaptar el comportamiento del modelo más grande. Esto implica:

* Congelar la gran matriz de pesos original.
* Crear matrices reducidas que sí serán entrenadas.
* Integrar, al final, estas matrices con la matriz original para adaptar el modelo al nuevo caso de uso.

Si originalmente se necesitaba manejar matrices de pesos gigantes (e.g., 100,000 x 100,000), con LoRa estas matrices pueden reducirse sustancialmente (e.g., 8 x 100,000).

## Implementando LoRa con recursos gratuitos

Usando una cuenta gratuita de Google Colab, y empleando librerías como Parameter Efficient Fine Tuning (PEFT) y transformers de Hugging Face, se puede realizar de manera sencilla:

* Instalar librerías necesarias como PyTorch, PEFT y CUDA.
* Seleccionar instancias gratuitas como la GPU T4.
* Definir claramente hiperparámetros clave para LoRa (e.g., rango de reducción, alpha, dropout).
* Preparar los datos específicos para entrenamiento supervisado.
* Formatear correctamente la entrada usando tokenizers específicos de cada modelo.

Es posible usar modelos open source indicados especialmente para fine tuning, por ejemplo, aquellos identificados con etiquetas como Instruct en Hugging Face. Estos modelos, además de ya estar diseñados para facilitar el fine tuning, permiten realizarlo eficazmente con un menor número de parámetros entrenados.

## Entrena tu modelo con LoRa paso a paso

La ejecución del fine tuning con LoRa en Colab incluye pasos concretos y simples:

* Configurar y cargar tu modelo cuantizado.
* Reducir dimensionalidad con LoRa en matrices puntuales del modelo.
* Preparar y formatear tu dataset correctamente para el entrenamiento supervisado.
* Ejecutar el entrenamiento supervisado, validando constantemente la reducción del loss.

Como resultado del proceso, puedes tener adaptadores específicos para distintos casos de uso, reduciendo el espacio requerido de gigabytes a megabytes.

[CODIGO](./Codigos/02_Estrategias%20Avanzadas%20de%20Fine%20Tunning%20(PEFT,%20SFT,%20LoRa).ipynb)

[REGRESAR](../03_Personalizacion_y_Optimizacion/Intro.md)