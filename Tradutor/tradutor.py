import pausa

def traduzir_zzz(codigo_zzz):
    linhas_zzz = codigo_zzz.splitlines()
    codigo_python = ""
    indentacao = 0
    variaveis = {}
    codigo_python += f"{pausa.InsereZzZ()}\n"
    AddPausa = pausa.adicionar_pausa()
    Funcoes = 0
    Retornos = 0
    
    for linha in linhas_zzz:
        linha = linha.strip()

        #Verifica as palavras reservadas e as substitui
        
        if linha.startswith("Questao"):
            nome_funcao = linha.split("Questao")[1].split("{")[0].strip()
            codigo_python += f"def {nome_funcao}:\n"
            codigo_python += f"{' ' * ((indentacao+1) * 4)}{AddPausa}\n"
            Funcoes +=1
        elif linha.startswith("Responder"):
            valor_retorno = linha.split("Responder")[1].strip()
            codigo_python += f"{' ' * (indentacao * 4)}return {valor_retorno}\n"
            Retornos +=1
        elif linha.startswith("Apresentar"):
            valor_print = linha.split("Apresentar")[1].strip()
            codigo_python += f"{' ' * (indentacao * 4)}print({valor_print})\n"
        elif "Anotar" in linha:
            nome_variavel = linha.split("Anotar")[1].split("em")[1].strip()
            codigo_python += f"{' ' * (indentacao * 4)}{nome_variavel} = int(input())\n"
        elif linha.startswith("TemTempo?"):
            condicao = linha.split("TemTempo?")[1].strip().split("{")[0].strip()
            codigo_python += f"{' ' * (indentacao * 4)}if {condicao}:\n"
            codigo_python += f"{' ' * ((indentacao+1) * 4) + AddPausa }\n"
        elif linha.startswith("NaoDeu"):
            codigo_python += f"{' ' * (indentacao * 4)}else:\n"
            codigo_python += f"{' ' * ((indentacao + 1) * 4)}{AddPausa}\n"
        elif linha.startswith("Estudar"):
            codigo_python += f"{' ' * (indentacao * 4)}while True:\n"
            codigo_python += f"{' ' * ((indentacao + 1)* 4)+ AddPausa }\n"
        elif linha.startswith("Terminei"):
            codigo_python += f"{' ' * (indentacao * 4)}break\n"
        else:
            if linha.startswith("#"):
                nome_variavel, valor = linha.split("=", 1)
                nome_variavel = nome_variavel.strip().replace("#", "")
                variaveis[nome_variavel.strip()] = valor.strip()
                codigo_python += f"{' ' * (indentacao * 4)}{nome_variavel.strip()} = {valor.strip()}\n"
            else:
                if linha.endswith ("}"):
                    indentacao -= 1
                    continue
                codigo_python += f"{' ' * (indentacao * 4)}{linha}\n"
        
        if linha.endswith("{"):
            indentacao += 1
    if(Retornos != Funcoes):
        print(Retornos)
        print(Funcoes)
        print("Erro, numero de perguntas e respostas conflitante, dá zero pra ele")
        return
    return codigo_python