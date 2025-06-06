#Simulação de Risco de Alagamento

Este projeto simula o comportamento da **vazão de água (em L/min)** durante uma tempestade, avaliando os riscos de alagamento com base em uma função matemática.

##Objetivo

Simular a variação da vazão ao longo do tempo (de 0 a 20 minutos) e emitir alertas quando o valor ultrapassa **100 L/min**, indicando um risco de alagamento.

---

##Lógica da Simulação

A função utilizada para calcular a vazão é:

```python
vazao(t) = 600 * e^(-0.15 * t) * sin(0.7 * t)
