# visualization_3d.py
import numpy as np
import plotly.graph_objects as go

def plot_wave_3d_electromagnetic(frecuencia, amplitud_incidente, amplitud_reflejado, amplitud_transmitido, impedancia, coef_reflexion, coef_transmision):
    # Crear el rango de distancia y los valores de la onda
    distancia = np.linspace(0, 1, 500)
    campo_electrico = amplitud_incidente * np.sin(2 * np.pi * frecuencia * distancia)
    campo_magnetico = (amplitud_reflejado * np.sin(2 * np.pi * frecuencia * distancia)) / impedancia

    fig = go.Figure()

    # Campo Eléctrico (E) en el eje Y
    fig.add_trace(go.Scatter3d(
        x=distancia, y=campo_electrico, z=np.zeros_like(distancia),
        mode='lines', name="Campo Eléctrico (E)", line=dict(color="blue")
    ))

    # Campo Magnético (H) en el eje Z
    fig.add_trace(go.Scatter3d(
        x=distancia, y=np.zeros_like(distancia), z=campo_magnetico,
        mode='lines', name="Campo Magnético (H)", line=dict(color="red")
    ))

    # Configuración de la gráfica con la información en el título
    fig.update_layout(
        title_text=(
            f"Propagación de Onda Electromagnética en 3D<br>"
            f"Impedancia: {impedancia:.2f} Ω | Coef. de Reflexión Γ: {coef_reflexion:.2f} | Coef. de Transmisión α: {coef_transmision:.2f}"
        ),
        scene=dict(
            xaxis_title="Dirección de Propagación (X)",
            yaxis_title="Campo Eléctrico (E)",
            zaxis_title="Campo Magnético (H)"
        ),
        showlegend=True
    )

    fig.show()
