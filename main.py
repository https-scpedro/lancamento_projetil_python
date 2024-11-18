import formulas as fl
import numpy as np
import matplotlib.pyplot as plt


try:
    V0 = float(input("Digite V0:").strip())
    alpha = float(input("Digite Alpha:").strip())
    t = float(input("Digite o Tempo de Observação:").strip())

except ValueError:
    print("Digite um número válido: :(")
    exit(1)

# Convertendo o angulo para radianos:
alpha_rad = np.radians(alpha)

# Calculando os dados:
try:

    t_total = fl.tempo_total_voo(V0, alpha)
    h_maxima = fl.altura_maxima(V0, alpha)
    d_maxima = fl.distancia_maxima(V0, alpha)

    # Gerando dados para a tragetória:
    t_values = np.linspace(0, t_total, num = 500)
    x_values = [fl.posicao_horizontal(V0, alpha, t) for t in t_values]
    y_values = [fl.posicao_vertical(V0, alpha, t) for t in t_values]

    # Destaques do gráfico:
    pontos_tempo = np.linspace(0, t_total, num = 5)
    pontos_x = [fl.posicao_horizontal(V0, alpha, t) for t in pontos_tempo]
    pontos_y = [fl.posicao_vertical(V0, alpha, t) for t in pontos_tempo]
    velocidades_vx = [fl.velocidade_horizontal(V0, alpha) for t in pontos_tempo]
    velocidades_vy = [fl.velocidade_vertical(V0, alpha, t) for t in pontos_tempo]
    velocidades_resultantes = [fl.velocidade_resultante(V0, alpha, t) for t in pontos_tempo]

except Exception as e:
    print(f"Erro ao calcular {e}")
    exit(1)

# Criando o Gráfico:
plt.figure(figsize = (6, 10))
plt.plot(x_values, y_values, label = "Tragetória de um Projétil", color = "green")

# Marcações de H_max e d_max:
plt.scatter([d_maxima / 2, d_maxima], [h_maxima, 0], color="blue", label="Pontos principais (H_max e d_max)")
plt.axhline(h_maxima, color = "blue", linestyle = "--", linewidth = 0.7)
plt.axvline(d_maxima, color = "blue", linestyle = "--", linewidth = 0.7)

# Vetores de Velocidade:
for i in range(len(pontos_tempo)):
    plt.quiver(
        pontos_x[i], pontos_y[i], velocidades_vx[i], velocidades_vy[i],
        angles = "xy", scale_units = "xy", scale = 1, color = "red", label = "Velocidade (v)"

        if i == 0 
        else ""
    )

#Configurações do Gráfico:
plt.title("Lançamento de Projéteis")
plt.xlabel("Posisão Horizontal (m)")
plt.ylabel("Posição Vertical (m)")
plt.axhline(0, color = "black", linewidth = 0.8)
plt.axvline(0, color = "black", linewidth = 0.8)
plt.legend()
plt.grid()

plt.show()

