# Despliegue de modelos fine-tuned con Hugging Face Endpoints

## Resumen

Optimizar y desplegar modelos entrenados manualmente es posible gracias a los Hugging Face Inference Endpoints, facilitando la integración en servicios y aplicaciones sin complicadas configuraciones técnicas. Aprende paso a paso cómo guardar tu modelo entrenado, subirlo eficientemente a Hugging Face y desplegarlo en la nube para producción.

## ¿Cómo guardar tu modelo fine-tuned?

Tras entrenar tu modelo es esencial guardarlo correctamente. Utiliza el método `save_model` disponible desde tu objeto trainer, especificando claramente el identificador que desees. Esto generará los siguientes archivos clave:

* Configuración sobre adaptadores empleados (Lora).
* Archivos binarios (safe tensors) con los pesos entrenados.
* Configuración relevante para cargarlo posteriormente.

Mantener estos archivos debidamente almacenados posibilitará su uso posterior para inferencia.

## ¿Cuáles son los pasos para subir tu modelo a Hugging Face?

Hugging Face ofrece simplicidad al subir modelos, actuando similar a un repositorio Git adaptado especialmente para machine learning:

1. Creación de un token en Hugging Face con permisos de escritura.
2. Autenticación desde tu Google Colab usando este token.
3. Subir tu modelo mediante trainer.push_to_hub().

Es recomendable escoger cuidadosamente los permisos del token según el nivel de acceso que deseas otorgar, contando con la opción de especificar niveles más detallados si es necesario.

## ¿Qué es y cómo crear un archivo handler.py para inferencia?

Para desplegar efectivamente en Hugging Face Inference Endpoints debes:

* Generar un archivo handler.py que contenga:
* Inicialización del modelo base y adaptadores.
* Carga del tokenizer para procesar entradas.
* Definir la función __call__ para manejar solicitudes de inferencia desde la API.

Este archivo permitirá al endpoint gestionar automáticamente solicitudes provenientes del usuario, realizando inferencia y retornando la información requerida de manera rápida y segura.

## ¿Cómo utilizar Hugging Face Inference Endpoints para despliegue en la nube?

Para desplegar modelos facilmente debes entrar a "Inference Endpoints" de Hugging Face, indicando:

* Proveedor (AWS recomendado).
* Tipo de máquina adecuada (GPU NVIDIA L4 recomendada para optimización).
* Nivel de seguridad (Protected, Hugging Face Restricted o Public según necesidad).
* Configuración de auto-escalado para control económico.

Al usar esta herramienta se evita lidiar con infraestructura complicada, reduciendo significativamente tiempos de configuración e incrementando tu productividad.

## ¿Qué consideraciones de costos debes tener presentes?

Es fundamental seleccionar planos que controlen tus gastos:

* Establece un tiempo limitado para desactivar instancias si no reciben solicitudes (se recomienda una ventana de 15 minutos).
* Inicializa únicamente una réplica por defecto para mantener bajo tu gasto inicial.
* Evalúa cuidadosamente el número de solicitudes que tu endpoint atenderá para elegir correctamente el tamaño y tipo de máquina.

Adicionalmente, mediante el dashboard ofrecido por Hugging Face podrás monitorear y pausar tus endpoints para ajustar fácilmente tus costos operativos.

## ¿Cómo probar rápidamente tu endpoint?

Es posible validar tu endpoint directamente desde el playground disponible, facilitando pruebas rápidas y ajustes inmediatos. También, Hugging Face proporciona opciones detalladas para integrarlo en Python, JavaScript u otros métodos interactivos mediante APIs.

[REGRESAR](../03_Personalizacion_y_Optimizacion/Intro.md)