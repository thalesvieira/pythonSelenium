import re
import os
import shutil

main_folder = r'/Users/thale/Desktop/ProjetoTeste'

# Função que renomeia os Arquivos de acordo com a preferência
def renomearArquivo(file):
    nomeArquivo, file_extension = os.path.splitext(file) # Separando as extensões do arquivos pela lib do os.
    numeroArquivo = re.findall(r'\d+', nomeArquivo) # Encontrar todos os digitos numéricos no nome do arquivo.
    nomePlataforma = 'Teste' #Nome da Plataforma que precisa ser renomeada.

    if not numeroArquivo: # Caso nao tenha numeros no nome, retorna o nome do arquivo atual.
        return file

    numeroArquivo = nomePlataforma + numeroArquivo[0].zfill(5) # Função propria de string para completar com 0 os numeros menores.

    return f'{numeroArquivo}{file_extension}' # Retornando o número do arquivo e a extensão do mesmo.


def LoopArquivo(root, dirs, files):
    for file in files:
        if not re.search(r'\.txt$', file): #Se não achar a extesão do arquivo txt, ele pula para o proximo.
            continue

        new_nomeArquivo = renomearArquivo(file) # Renomeia o arquivo.
        caminhoAntigo = os.path.join(root, file) # Caminho antigo completo com a pasta e sub-pasta.
        caminhoNovo = os.path.join(root, new_nomeArquivo) # Caminho novo completo com a pasta e sub-pasta.

        print(f'Renomeando arquivo "{file}" para "{new_nomeArquivo}"') #Print para mostrar se renomeuou de forma correta.
        shutil.move(caminhoAntigo, caminhoNovo) # Movendo/Renomeando os arquivos na pasta.
        # print (renomearArquivo)

# Entrar no diretório para pegar os arquivos (Pasta principal e diretórios)
def main_loop():
    for root, dirs, files in os.walk(main_folder):
        LoopArquivo(root, dirs, files)


if __name__ == '__main__':
    main_loop()