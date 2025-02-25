import os
import tradutor

def gerarcodigo(caminho_arquivo):
    # Verifica se o arquivo foi fornecido
    if not caminho_arquivo:
        print("Erro: Nenhum arquivo especificado.")
        return
    
    # Verifica se o arquivo tem a extensão correta
    if not caminho_arquivo.endswith(".ZzZ"):
        print("Erro: O arquivo deve ter a extensão .ZzZ")
        return
    
    # Verifica se o arquivo existe
    if not os.path.exists(caminho_arquivo):
        print(f"Erro: O arquivo '{caminho_arquivo}' não foi encontrado.")
        return

    # Lê o conteúdo do arquivo .ZzZ
    with open(caminho_arquivo, "r", encoding="utf-8") as arquivo:
        try:
            conteudo = tradutor.traduzir_zzz(arquivo.read())
        except: 
            print("Erro na trodução, verifique o código")
            return
    
    # Define o nome do novo arquivo .pyC:\Users\Leandro\Desktop\ZzZ\Exemplos\Fatorial.ZzZ
    nome_py = caminho_arquivo.replace(".ZzZ", ".py")

    # Escreve o conteúdo no novo arquivo .py
    if(not conteudo):
        return
    with open(nome_py, "w", encoding="utf-8") as arquivo_py:
        arquivo_py.write(conteudo)

    print(f"Arquivo {nome_py} gerado com sucesso!")


gerarcodigo(input("Digite o caminho do arquivo: "))