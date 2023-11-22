import os
import cv2

# Diretório contendo as imagens
pasta_imagens = 'facial_expression/surprise'

# Lista de arquivos na pasta
arquivos = os.listdir(pasta_imagens)
# Ângulo de rotação desejado (em graus)
angulo_rotacao = 90  # Você pode ajustar o ângulo conforme necessário

# Loop para processar todas as imagens na pasta
for arquivo in arquivos:
    # Verifica se o arquivo é uma imagem (pode adicionar extensões adicionais se necessário)
    if arquivo.lower().endswith(('.png', '.jpg', '.jpeg', '.bmp', '.gif')):
        # Caminho completo para a imagem
        caminho_imagem = os.path.join(pasta_imagens, arquivo)
        
        # Carregue a imagem original em grayscale
        original_image = cv2.imread(caminho_imagem, cv2.IMREAD_GRAYSCALE)

        # Rotação da imagem
        rows, cols = original_image.shape
        M = cv2.getRotationMatrix2D((cols / 2, rows / 2), angulo_rotacao, 1)
        rotated_image = cv2.warpAffine(original_image, M, (cols, rows))

        # Salve a imagem rotacionada com um nome diferente (pode personalizar o nome)
        nome_saida = 'rotacionada_' + arquivo
        caminho_saida = os.path.join(pasta_imagens, nome_saida)
        cv2.imwrite(caminho_saida, rotated_image)

print("Rotação concluída para todas as imagens na pasta.")