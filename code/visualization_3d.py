# visualization_3d.py
import numpy as np
import plotly.graph_objects as go

def plot_wave_3d_electromagnetic(frecuencia, amplitud_incidente, amplitud_reflejado, amplitud_transmitido, impedancia, coef_reflexion, coef_transmision):
    distancia = np.linspace(0, 1, 500)
    campo_incidente = amplitud_incidente * np.sin(2 * np.pi * frecuencia * distancia)
    campo_reflejado = amplitud_reflejado * np.sin(2 * np.pi * frecuencia * distancia)
    campo_transmitido = amplitud_transmitido * np.sin(2 * np.pi * frecuencia * distancia)

    fig = go.Figure()

    # Campo Incidente
    fig.add_trace(go.Scatter3d(
        x=distancia, y=campo_incidente, z=np.zeros_like(distancia),
        mode='lines', name="Campo Incidente", line=dict(color="blue")
    ))

    # Campo Reflejado
    fig.add_trace(go.Scatter3d(
        x=distancia, y=campo_reflejado, z=np.ones_like(distancia),
        mode='lines', name="Campo Reflejado", line=dict(color="red")
    ))

    # Campo Transmitido
    fig.add_trace(go.Scatter3d(
        x=distancia, y=campo_transmitido, z=2 * np.ones_like(distancia),
        mode='lines', name="Campo Transmitido", line=dict(color="green")
    ))

    # Configuración de la gráfica
    fig.update_layout(
        title_text="Simulación de Campos Electromagnéticos en 3D",
        scene=dict(
            xaxis_title="Distancia (mm)",
            yaxis_title="Amplitud del Campo",
            zaxis_title="Posición Relativa"
        ),
        showlegend=True
    )

    # Agregar anotaciones para impedancia y coeficientes
    fig.add_annotation(
        x=0, y=3, z=2,
        text=f"Impedancia: {impedancia:.2f} Ω",
        showarrow=False,
        font=dict(size=12)
    )

    fig.add_annotation(
        x=0, y=2.7, z=2,
        text=f"Coeficiente de Reflexión Γ: {coef_reflexion:.2f}",
        showarrow=False,
        font=dict(size=12)
    )

    fig.add_annotation(
        x=0, y=2.4, z=2,
        text=f"Coeficiente de Transmisión α: {coef_transmision:.2f}",
        showarrow=False,
        font=dict(size=12)
    )

    fig.show()
