# Leyes de escalado y modelos multimodales en inteligencia artificial

## Resumen

Las leyes de escalado y los modelos multimodales son esenciales en el ámbito actual de la inteligencia artificial. Aumentar los parámetros, la cantidad de datos y la capacidad computacional mejora el desempeño, aunque con retornos decrecientes tras cierto punto. A su vez, los modelos multimodales combinan diferentes tipos de información, permitiendo aplicaciones avanzadas en diversos contextos.

## ¿Qué son las leyes de escalado?

Las leyes de escalado revelan cómo mejora previsiblemente el rendimiento de un modelo al incrementar ciertos recursos clave. Estos recursos son:

* **Parámetros del modelo**.
* **Datos disponibles para entrenamiento**.
* **Capacidad computacional**.

Es clave equilibrarlos: un modelo amplio sin suficientes datos o al revés implica desperdicio de potencial. OpenAI comprobó esto con GPT-3: más parámetros y datos mejoraron consistentemente tareas de generación y comprensión textual, aunque presentar retornos cada vez menores al aumentar repetidamente los recursos invertidos.

La relación entre el rendimiento y los recursos sigue una ley matemática conocida como ley de potencia, mostrando cómo al aumentar recursos específicos, los errores o pérdidas disminuyen con predictibilidad.

## ¿Por qué son importantes los modelos multimodales?

Combinar múltiples modalidades de datos, como textos, imágenes, audio y videos, permite a los modelos multimodales tener una comprensión más robusta y contextual del mundo. Algunos ejemplos actuales significativos incluyen:

* **CLIP (OpenAI)**: asocia imágenes a descripciones textuales, permitiendo búsquedas visuales simples mediante lenguaje natural.
* **DALL-E (OpenAI)**: genera imágenes coherentes a partir de descripciones claras, posibilitando aplicaciones creativas en diseño gráfico.
* **Flamingo (DeepMind)**: destaca por su aprendizaje rápido y generación de conocimiento usando poquísimos ejemplos, integrando texto, imágenes, audio y video.

Entre sus ventajas destacan una comprensión contextual mejorada y calidad alta en contenido generado. Sin embargo, implican desafíos importantes como:

* Diseñar arquitecturas especializadas por tipo de datos.
* Alto costo computacional.
* Métodos específicos de preprocesamiento, fusión y alineación modal para representación coherente.

## ¿Cuáles son las aplicaciones prácticas de la multimodalidad?

Actualmente, existen aplicaciones reales muy diversas que ilustran la importancia de estos modelos. Ejemplo concreto es la aplicación móvil Chat LLM, con modelos como **O1**, que permite cargar diferentes tipos de datos (texto, imágenes, videos, audios) y procesarlos integrado con aprendizaje reforzado para dar respuestas contextualizadas y precisas. Otros modelos, como **O3 mini**, no poseen capacidades multimodales, lo cual es fundamental considerar al seleccionar tecnologías para proyectos específicos.

Experimentar personalmente con estas tecnologías puede aportar experiencia valiosa sobre su potencial y limitaciones en distintos escenarios prácticos. Por ello, se recomienda explorar diferentes LLM, observando cómo procesan modalidades variadas de información.

[REGRESAR](../02_Componentes_Avanzados_de_los_LLMs/Intro.md)