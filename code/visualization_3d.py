# visualization_3d.py
import numpy as np
import plotly.graph_objects as go

def plot_wave_3d_electromagnetic(frecuencia, amplitud, velocidad=3e8, tamaño=1, tiempo=0.001, impedancia=None, gamma=None, alpha=None):
    """
    Visualiza la propagación de una onda electromagnética en 3D, con los campos eléctrico y magnético.
    Incluye anotaciones de impedancia y coeficientes de reflexión y transmisión.
    """
    x = np.linspace(0, tamaño, 50)
    z = np.linspace(0, tamaño, 50)
    X, Z = np.meshgrid(x, z)

    # Campos eléctrico y magnético con desfase de 90 grados
    E = amplitud * np.sin(2 * np.pi * frecuencia * (X / velocidad + tiempo))
    B = amplitud * np.sin(2 * np.pi * frecuencia * (X / velocidad + tiempo + np.pi / 2))

    fig = go.Figure()
    fig.add_trace(go.Surface(z=E, x=X, y=Z, colorscale='Viridis', opacity=0.6, name='Campo Eléctrico'))
    fig.add_trace(go.Surface(z=B, x=X, y=Z, colorscale='Plasma', opacity=0.6, name='Campo Magnético'))

    # Anotaciones de impedancia y coeficientes en el título
    title_text = "Propagación de Onda Electromagnética en 3D"
    if impedancia is not None:
        title_text += f"<br>Impedancia: {impedancia:.2f} Ω"
    if gamma is not None:
        title_text += f"<br>Coeficiente de Reflexión Γ: {gamma:.2f}"
    if alpha is not None:
        title_text += f"<br>Coeficiente de Transmisión α: {alpha:.2f}"

    fig.update_layout(
        title=title_text,
        scene=dict(
            xaxis_title="Espacio",
            yaxis_title="Propagación",
            zaxis_title="Amplitud del Campo",
            xaxis=dict(showbackground=True, backgroundcolor="lightgrey"),
            yaxis=dict(showbackground=True, backgroundcolor="lightgrey"),
            zaxis=dict(showbackground=True, backgroundcolor="lightgrey")
        ),
        width=800, height=800
    )
    fig.show()
