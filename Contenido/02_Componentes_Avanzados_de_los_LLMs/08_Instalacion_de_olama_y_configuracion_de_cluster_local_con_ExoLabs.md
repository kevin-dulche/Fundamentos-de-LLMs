# Instalación de Olama y configuración de clúster local con ExoLabs

## Resumen

¿Te interesa aprender a ejecutar modelos LLM (Large Language Models) de forma local en tu equipo? A continuación, aprenderás cómo descargar Olama, configurar modelos como DeepSig y utilizar ExoLabs para conectar múltiples computadoras potenciando tu capacidad de procesamiento local para LLMs.

## ¿Cómo se instala y ejecuta Olama de manera local?

**Olama** es una herramienta sencilla para ejecutar modelos LLM de forma local:

1. **Descarga Olama:** Ve a Google, busca Olama, y descarga la versión adecuada para tu sistema operativo (macOS, Windows o Linux).

2. **Instalación:** Una vez descargado el archivo binario, ejecútalo haciendo doble clic y siguiendo los pasos que indica tu sistema operativo (por ejemplo, en macOS selecciona mover a Aplicaciones).

3. **Uso desde terminal:** Abre la terminal y ejecuta Olama para ver los comandos disponibles. Copia desde la web de Olama el comando específico del modelo que quieres ejecutar (por ejemplo, DeepSig r1-7b).

## ¿Cómo interactúa Olama con los modelos LLM?

Al ejecutar un modelo en Olama, este descargará los archivos necesarios (puede tomar varios minutos):

* **Interacción básica:** Realiza preguntas o comandos como "¿cuánto es dos más dos?" para empezar a trabajar.
* **Consumo de recursos:** La descarga y uso del modelo consumen recursos de CPU y memoria, por ejemplo, durante una consulta puede subir el consumo a más de dos gigabytes temporalmente.

## ¿Qué es ExoLabs y cómo potencia el uso local de LLMs?

**ExoLabs** permite conectar múltiples computadoras creando un clúster local de potencia computacional compartida:

* **Concepto principal:** Usa redes peer-to-peer (P2P) como la tecnología detrás de plataformas como Torrent para compartir datos y tareas entre máquinas conectadas.
* **Ventajas:** Reduce costos al utilizar varias computadoras económicas, mejora la privacidad (importante en sectores bancarios o jurídicos) y permite controlar específicamente las configuraciones y costos operacionales.

## ¿Cómo montar un clúster local con ExoLabs?

Estos pasos específicos son clave para conectar varias máquinas con ExoLabs:

* **Equipamiento:** necesitas diversas computadoras conectadas mediante switch y router, pudiendo combinar conexiones Ethernet y WiFi.
* **Configuración y ejecución:** instala ExoLabs en cada máquina; al ejecutar, crea automáticamente una red entre ellas mostrando información como teraflops o memoria disponible.
* **Funcionamiento:** Cada computadora aporta sus capacidades (CPU, GPU, memoria) a la red, haciendo posible ejecutar modelos de gran tamaño que de otro modo requerirían hardware costoso.

## ¿Qué modelos LLM puedes ejecutar localmente con ExoLabs?

Puedes ejecutar modelos de distintos tamaños según la capacidad de memoria acumulada en tu red:

* Modelos como DeepSig r1-70b requieren 70 gigabytes de memoria, completamente alcanzables al conectar varios equipos que sumen dicha capacidad.
* Esta forma de trabajo localiza la informática, especialmente útil si tienes requisitos estrictos sobre información privada.

¿Cuáles son las ventajas concretas de ejecutar LLM en local?

* **Privacidad total:** Los datos sensibles permanecen en tu entorno, clave para industrias sensibles al manejo de información.
* **Control absoluto:** Define exactamente qué quieres ejecutar, cuánto gastar, y cómo ajustar o optimizar tu modelo específicamente para tu caso de uso con técnicas como el fine tuning.

Ahora que conoces cómo instalar Olama, manejar modelos locales e integrar ExoLabs para incrementar capacidad local, puedes aprovechar al máximo el potencial de los modelos LLM de manera segura y controlada.

[REGRESAR](../02_Componentes_Avanzados_de_los_LLMs/Intro.md)