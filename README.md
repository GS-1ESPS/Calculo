# Simulação de Risco de Alagamento

Este projeto simula a vazão de água durante tempestades para identificar momentos críticos que podem causar alagamentos.

## 📋 Descrição

O código calcula a vazão de água (em L/min) ao longo do tempo usando um modelo matemático que combina:
- Decaimento exponencial da vazão
- Componente oscilatório (variações durante a tempestade)

## ⚙️ Funcionalidades

- Cálculo da vazão a cada 30 segundos (0.5 min)
- Detecção automática de vazões críticas (>100 L/min)
- Sistema de alertas para riscos de alagamento
- Saída formatada com dados temporais

## Como Usar

1. Clone o repositório:
   ```bash
   git clone [URL_DO_REPOSITORIO]
