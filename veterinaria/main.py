import time
import crud

# tua parte ai antonio

print("Carregando base de dados de pacientes...")

inicio = time.time()  # Registra o tempo exato antes de começar a leitura!!
crud.carregar(arquivo_escolhido)  
fim = time.time()     # Registra o tempo depois!!

tempo_leitura = fim - inicio
print(f"Segunda Etapa Concluída com Sucesso!")
print(f"Tempo computacional de leitura: {tempo_leitura:.4f} segundos.")