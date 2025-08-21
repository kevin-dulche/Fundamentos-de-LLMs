# Fundamentos de PyTorch para modelos de machine learning

## Resumen

PyTorch es un framework robusto creado por Meta, anteriormente Facebook, diseñado específicamente para construir modelos de machine learning y deep learning. Ofrece recursos variados y librerías que facilitan desarrollar arquitecturas neuronales complejas desde cero o con cierta base previa.

## ¿Qué es un tensor en PyTorch?

El elemento central de PyTorch es el tensor, una estructura similar a una lista, vector o matriz en Python. Básicamente, se trata de una estructura n-dimensional manejada internamente según filas y columnas requeridas para almacenar datos numéricos. En machine learning, estos tensores constituyen la base sobre la que se procesan los modelos.

## ¿Cuál es el rol de Autograd en PyTorch?

Un aspecto fundamental de PyTorch es Autograd, un sistema computacional diseñado para realizar automáticamente la derivación parcial. Sin Autograd, los cálculos de derivadas parciales para modelos grandes consumirían demasiado tiempo manualmente. Con este mecanismo, PyTorch automatiza estos procedimientos mediante aproximaciones que facilitan notablemente la creación y ajuste de modelos avanzados.

## ¿Qué es el optimizer y cómo ayuda a entrenar modelos?

El optimizer es otro componente clave que maneja el aprendizaje del modelo mediante métodos específicos como el popular algoritmo Adam. Este realiza ajustes internos (por ejemplo, utilizando back propagation) y determina el learning rate, ayudando a que el modelo supere mínimos locales y optimizando su aprendizaje.

## Tipos de optimizadores disponibles:
* Adam
* Adam X
* Adam W
* Adam Z

## ¿Cómo implementar un modelo MLP con PyTorch paso a paso?

Utilizando PyTorch, la creación de un modelo Multi Layer Perceptron (MLP) sigue estos pasos simples pero indispensables:

1. Importación y configuración: 

```Python 
import torch 
import torch.nn as nn 
import torch.optim as optim 
import torch.nn.functional as F 
import time
```

2. Definir la arquitectura de red neuronal: 
```Python 
class MLP(nn.Module):
    def __init__(self, input_dim, hidden_dim, output_dim):
        super(MLP, self).__init__()
        self.fc1 = nn.Linear(input_dim, hidden_dim)
        self.fc2 = nn.Linear(hidden_dim, output_dim)

    def forward(self, x):
        x = F.relu(self.fc1(x))
        x = self.fc2(x)
        return x
```

3. Entrenamiento y optimización:

4. Instanciar el modelo con dimensiones específicas.

5. Elegir la función de pérdida (error cuadrático medio).

6. Seleccionar un optimizer, frecuentemente Adam.

7. Crear datos ficticios y ejecutar entrenamiento. 

```Python
model = MLP(10, 100, 1) 
criterion = nn.MSELoss() 
optimizer = optim.Adam(model.parameters(), lr=0.01)
```

## ¿Es posible entrenar modelos con GPU en PyTorch?
Sí, PyTorch permite usar GPU para acelerar los procesos. El paso para verificar disponibilidad es sencillo:

```Python
device = torch.device("cuda" if torch.cuda.is_available() else "cpu")
```

Luego, transfiriendo nuestros tensores al dispositivo elegido, podemos reducir significativamente los tiempos de procesamiento de grandes conjuntos de datos o arquitecturas más complejas.

## Ejemplo práctico de uso con GPU:

```Python
x = torch.randn(2000000, 10).to(device)
y = torch.randn(2000000, 1).to(device)
```
[CODIGO](./Codigos/06_PyTorch_MLP.ipynb)

[REGRESAR](../01_Fundamentos_de_los_LLMs/Intro.md)