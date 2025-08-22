# Requisitos de hardware para ejecutar modelos LLM en tu computadora

## Resumen

¿Te gustaría ejecutar modelos LLM (Large Language Models) directamente desde tu computadora personal? Antes de iniciar debes dominar algunos conceptos importantes como CPU, GPU, RAM, VRAM y cuantización.

## ¿Cuál es la diferencia entre CPU y GPU?

La CPU es un procesador general encargado de múltiples tareas en la computadora. Por otro lado, la GPU está especializada en operaciones matemáticas específicas como "m por x más b", esenciales en tareas como los modelos LLM.

## ¿Por qué son importantes la RAM y la VRAM?

## ¿Qué función tiene la memoria RAM?

La **memoria RAM** almacena temporalmente archivos e información activa, como cuando editas una imagen en Photoshop o navegas por múltiples pestañas en Internet. Para ejecutar modelos LLM localmente, se recomienda:

* Un mínimo de 16 GB.
* Preferentemente hasta 64 GB de RAM para un rendimiento óptimo.

## ¿Cuál es el papel de la memoria VRAM?

La VRAM (Video Random Access Memory) está directamente integrada con la GPU. Al estar físicamente cercana, permite una menor latencia y mayor rendimiento. Para ejecutar modelos LLM pequeños o cuantizados, lo ideal es contar con entre 12 y 16 GB de VRAM. Las tarjetas gráficas de consumo alcanzan hasta 36 GB en su gama más alta.

## ¿Qué es y qué beneficios ofrece la cuantización de modelos?

La cuantización permite reducir el peso de los modelos de machine learning, bajando la precisión numérica empleada. Los modelos originalmente entrenados con 16 bits pueden cuantizarse a 8 o 4 bits, disminuyendo su tamaño significativamente. Por ejemplo:

* Un modelo de 100 GB (16 bits) podría reducirse a 25 GB (4 bits).

Estas reducciones facilitan ejecutar modelos grandes en hardware más modesto y accesible.

Ahora que entiendes estos conceptos, en próximas sesiones podrás verificar qué modelos son compatibles con tu equipo utilizando herramientas como Hugging Face y Olama.

```Markdown
🧠 **Ejecutar Modelos LLM en tu PC**
**Conceptos clave que debes dominar**

🔁 **CPU vs. GPU**
🔹 **CPU (Procesador Central)**
Realiza tareas generales del sistema.
Encargado de múltiples tareas.

🔹 **GPU (Procesador Gráfico)**
Especializada en cálculos matemáticos específicos (y= mx+b).
Esencial para tareas de machine learning y modelos LLM.

💾 **RAM y VRAM**
🔸 **RAM (Memoria de Acceso Aleatorio)**
* Almacena temporalmente lo que estás usando.
* Ejemplos: editar imágenes, tener muchas pestañas abiertas.

**Recomendado para LLM:**
✅ Mínimo: 16 GB
✅ Ideal: hasta 64 GB

🔸 **VRAM (Memoria de Video)**
Integrada con la GPU.
Velocidad alta gracias a su cercanía física con el procesador gráfico.

**Recomendado para LLM:**
✅ De 12 a 16 GB para modelos pequeños o cuantizados
🔝 Hasta 36 GB en tarjetas gráficas de gama alta a nivel personal

⚖️ **¿Qué es la Cuantización?**
🔽 **Reducción de tamaño del modelo**
* Baja la precisión numérica: de 16 bits a 8 o 4 bits.
* Menor tamaño, mismo propósito.

📉 **Ejemplo:** Modelo de 100 GB (16 bits) → 25 GB (4 bits)
✅ Permite ejecutar modelos grandes en computadoras modestas.
```

[REGRESAR](../02_Componentes_Avanzados_de_los_LLMs/Intro.md)