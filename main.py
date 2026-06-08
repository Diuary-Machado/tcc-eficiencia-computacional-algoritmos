from src.motor_benchmark import executar_pipeline_completo
import time

print("="*60)
print(" SISTEMA DE BENCHMARK COMPUTACIONAL - TCC ")
print("="*60)

datasets_para_testar = ["PETR4.SA", "VALE3.SA", "ITUB4.SA"]

tempo_inicio_geral = time.time()

for ativo in datasets_para_testar:
    executar_pipeline_completo(ticker=ativo)

tempo_total = time.time() - tempo_inicio_geral

print("\n" + "="*60)
print(f" BATERIA DE TESTES FINALIZADA COM SUCESSO! ")
print(f" Tempo total de execução: {tempo_total:.2f} segundos")
print(" Vá verificar as pastas 'resultados' e 'graficos'.")
print("="*60)