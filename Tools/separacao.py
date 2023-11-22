import os
import shutil
import random

# Pasta de origem das imagens
pasta_origem = 'Expressao facial\\new_pb_surprise'

# Pastas de destino para treinamento, validação e teste
pasta_destino_train = 'Expressao facial\\train\\surprise'
pasta_destino_val = 'Expressao facial\\val\\surprise'
pasta_destino_test = 'Expressao facial\\test\\surprise'

# Proporção de divisão (70% treinamento, 15% validação, 15% teste)
proporcao_treinamento = 0.7
proporcao_validacao = 0.15
proporcao_teste = 0.15

# Lista de arquivos JPEG na pasta de origem
arquivos = [arquivo for arquivo in os.listdir(pasta_origem) if arquivo.lower().endswith('.jpg')]

# Embaralhe a lista de arquivos
random.shuffle(arquivos)

# Calcule os índices de divisão
total_arquivos = len(arquivos)
num_treinamento = int(total_arquivos * proporcao_treinamento)
num_validacao = int(total_arquivos * proporcao_validacao)

# Crie as pastas de destino, se ainda não existirem
os.makedirs(pasta_destino_train, exist_ok=True)
os.makedirs(pasta_destino_val, exist_ok=True)
os.makedirs(pasta_destino_test, exist_ok=True)

# Divida os arquivos nas pastas de destino
for i, arquivo in enumerate(arquivos):
    origem = os.path.join(pasta_origem, arquivo)
    if i < num_treinamento:
        destino = os.path.join(pasta_destino_train, arquivo)
    elif i < num_treinamento + num_validacao:
        destino = os.path.join(pasta_destino_val, arquivo)
    else:
        destino = os.path.join(pasta_destino_test, arquivo)
    shutil.copy(origem, destino)

print("Imagens divididas com sucesso.")
