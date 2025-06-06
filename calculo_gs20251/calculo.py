import numpy as np

def vazao(t):
    # Função de vazão de água (L/min) durante a tempestade.
    return 600 * np.exp(-0.15 * t) * np.sin(0.7 * t)

# Simulação do comportamento da vazão de 0 a 20 minutos
print("Simulação de risco de alagamento:\n")
for t in np.arange(0, 20.5, 0.5):
    valor = vazao(t)
    if valor > 100:
        print(f"[ALERTA] Vazão crítica em t={t:.1f} min: {valor:.2f} L/min")
    else:
        print(f"Vazão em t={t:.1f} min: {valor:.2f} L/min")

