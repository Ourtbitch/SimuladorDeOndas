

# Simulador de Ondas Electromagnéticas

## Descripción

Este proyecto consiste en un simulador interactivo diseñado para ayudar a estudiantes a visualizar y comprender conceptos abstractos relacionados con ondas electromagnéticas, tales como propagación, reflexión y transmisión. Este simulador permite modificar parámetros clave y observar cómo afectan las ondas en el espacio, sirviendo como una herramienta educativa que facilita el aprendizaje activo y visual de estos conceptos.

## Características

- **Simulación de ondas electromagnéticas:** El simulador permite ver el comportamiento de ondas electromagnéticas en 2D y 3D.
- **Interfaz interactiva:** La interfaz permite a los usuarios ajustar parámetros como la frecuencia y amplitud de las ondas.
- **Cálculo de coeficientes y propiedades de las ondas:** El usuario puede calcular la impedancia, el coeficiente de reflexión y el coeficiente de transmisión.
- **Visualización personalizable:** La simulación se adapta a diferentes configuraciones de ondas, proporcionando una experiencia visual detallada.

## Requisitos de Instalación

Para ejecutar este proyecto, necesitas instalar Python y las siguientes bibliotecas:

```bash
pip install numpy
pip install matplotlib
pip install plotly
```

## Instrucciones de Uso

1. **Ejecuta la aplicación:** Inicia el programa principal desde `main.py` para abrir la interfaz gráfica.
2. **Cálculo de Impedancia:** Ingresa los valores de permeabilidad y permitividad en sus respectivos campos y presiona el botón "Calcular Impedancia".
3. **Cálculo de Coeficientes de Reflexión y Transmisión:** Ingresa los valores de impedancia (η1 y η2) y presiona "Calcular Coeficientes".
4. **Visualización de Campos:** Ajusta los parámetros de frecuencia, distancia máxima, amplitud de los campos (incidente, reflejado y transmitido) y presiona "Visualizar en 2D" o "Visualizar en 3D" según prefieras.
   - **Nota:** Si intentas visualizar sin haber calculado la impedancia o los coeficientes, se mostrará una advertencia indicando qué cálculos faltan.

## Objetivos del Proyecto

### Objetivo General

Desarrollar un simulador de ondas electromagnéticas que facilite la comprensión de su comportamiento y conceptos relacionados.

### Objetivos Específicos

1. Representar la propagación y reflexión de ondas en un entorno visual interactivo.
2. Permitir la experimentación con distintas configuraciones de ondas para mejorar la comprensión de los principios de la propagación.
3. Evaluar la efectividad del simulador como herramienta de aprendizaje en entornos educativos.

## Estructura del Proyecto

- `main.py`: Script principal para iniciar la interfaz gráfica de usuario.
- `interface.py`: Define la interfaz gráfica y los controles para el cálculo y visualización de ondas.
- `calculator.py`: Incluye funciones para el cálculo de la impedancia y coeficientes de reflexión y transmisión.
- `visualization_2d.py`: Genera la visualización en 2D de las ondas electromagnéticas.
- `visualization_3d.py`: Genera la visualización en 3D de las ondas, mostrando también los valores de impedancia y coeficientes.

## Metodología

La metodología empleada incluye la verificación del funcionamiento de los cálculos y la visualización interactiva, permitiendo ajustar configuraciones de prueba para evaluar la claridad y efectividad del simulador.

## Resultados

Este simulador ayuda a comprender el comportamiento de las ondas electromagnéticas en tiempo real, logrando representar visualmente los efectos de variaciones en los parámetros de las ondas.

---
