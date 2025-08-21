# Tokenización, vectorización y embeddings en LLMs

## Resumen

Los LLMs como ChatGPT entienden nuestras comunicaciones mediante procesos matemáticos específicos llamados tokenización, vectorización y embeddings. Estos métodos permiten transformar el lenguaje natural, audios e imágenes en información que una máquina puede comprender y procesar eficazmente.

## ¿Qué es la tokenización y cómo funciona?

La **tokenización** consiste en dividir textos en partes más pequeñas y manejables llamadas tokens. Un token puede ser una palabra, como en el ejemplo: "hola ¿cómo estás?", que se divide en tres tokens individuales: hola, cómo, y estás. Además de por palabras, la tokenización puede ser por subpalabras o fragmentos.

## ¿Cómo se lleva a cabo la vectorización?

Luego de tokenizar, continúa el proceso con la vectorización que consiste en asignar vectores o grupos numéricos a cada token inicial. En nuestro ejemplo:

* "hola" podría ser representado como (1,2)
* " cómo" como (1,3)
* "estás" como (3,4)

Estos vectores se crean inicialmente de forma aleatoria. Después, es posible representarlos en un plano cartesiano para visualizar sus relaciones.

## ¿Por qué es importante el proceso de embedding?

El embedding optimiza y ubica estratégicamente estos vectores, agrupándolos cerca de otros con significados similares. Con ejemplos como rey, hombre y reina, al aplicar álgebra vectorial:

* Rey - hombre = Reina

Obtenemos nuevos significados a partir de cálculos matemáticos. Esto facilita abordar conceptos abstractos en modelos numéricos, mejorando las capacidades del LLM.

## ¿Cómo utilizar Hugging Face y PyTorch para LLMs con tokenización y embeddings en Python?
Usando las librerías Transformers (Hugging Face) y Torch (PyTorch), los procesos mencionados pueden aplicarse en Python.

## Tokenización con Hugging Face

Instalando primero Transformers:


```Bash
!pip install transformers
```
Luego, cargando el tokenizer:

```Python
from transformers import BertTokenizer
tokenizer = BertTokenizer.from_pretrained('bert-base-uncased')
tokens = tokenizer.tokenize("hola, ¿cómo estás?")
```

Esto segmentará tu texto según el modelo utilizado, ya sea en palabras o subpalabras.

## Embeddings con PyTorch

La implementación de embeddings mediante PyTorch:

```Python
import torch
from transformers import BertModel

model = BertModel.from_pretrained('bert-base-uncased')
king_embedding = model.embeddings.word_embeddings(torch.tensor(tokenizer.convert_tokens_to_ids(["king"])))
man_embedding = model.embeddings.word_embeddings(torch.tensor(tokenizer.convert_tokens_to_ids(["man"])))
queen_embedding = model.embeddings.word_embeddings(torch.tensor(tokenizer.convert_tokens_to_ids(["queen"])))
```

Esto permite transformar tokens en vectores y posteriormente evaluar la similitud entre ellos mediante la función coseno:

```Python
cosine_similarity = torch.nn.CosineSimilarity(dim=0)
similitud = cosine_similarity(king_embedding, queen_embedding)
```

Los valores cercanos a 1 indican mucha similitud y aquellos cercanos a -1 indican diferencias considerables.

[CODIGO](./Codigos/03_Tokenizacion.ipynb) 

## ¿Qué puedes practicar con estos conceptos?

Te invitamos a practicar cambiando las palabras en los ejemplos dados. Explora relaciones entre palabras, por ejemplo, animales similares al gato o al perro. Gracias a estos conceptos, puedes profundizar tus conocimientos sobre cómo los grandes modelos del lenguaje comprenden nuestro mundo.

[REGRESAR](../01_Fundamentos_de_los_LLMs/Intro.md)