!pip install gradio

import gradio as gr
from collections import Counter

def dashboard(logs):
    lines = logs.split("\n")

    ips = []
    threats = []

    for line in lines:
        parts = line.split()
        if len(parts) >= 2:
            ips.append(parts[0])
            threats.append(parts[1])

    return {
        "Total ataques": len(lines),
        "Top IPs": Counter(ips).most_common(3),
        "Tipos de amenazas": Counter(threats).most_common(3)
    }

iface = gr.Interface(
    fn=dashboard,
    inputs=gr.Textbox(label="Pega logs aquí", lines=10),
    outputs="json",
    title="Dashboard de Ciberseguridad",
    description="Analiza ataques, IPs y amenazas."
)

iface.launch()
