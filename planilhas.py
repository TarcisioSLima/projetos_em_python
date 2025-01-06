import pyautogui as pc
import time as tempo

pc.press("win")
tempo.sleep(2)
pc.write("Edge")
tempo.sleep(2)
pc.press("enter")
tempo.sleep(5)
# entrar no link 
pc.write("localhost:820/formulario_s_banco/index.html")
pc.press("enter")
tempo.sleep(5)

import pandas as pd # type: ignore


tabela = pd.read_csv("C:/Users/tarci/OneDrive/Área de Trabalho/Projetos-Git/projetos_em_python/dados_de_exemplo/planilhas/dados_teste.csv")

print(tabela)

for linha in tabela.index:
    #pc.click(x=653, y=294)
    pc.press("tab")
    pc.write(str(tabela.loc[linha, "Nome"]))
    pc.press("tab")

    dado_empresa = tabela.loc[linha, "Empresa"]
    if not pd.isna(dado_empresa):
        pc.write(str(dado_empresa))
    pc.press("tab")

    pc.write(str(tabela.loc[linha, "Cidade"]))
    pc.press("tab")
    pc.write(str(tabela.loc[linha, "Estado"]))
    pc.press("tab")
    pc.write(str(tabela.loc[linha, "Endereço"]))
    pc.press("tab")
    pc.write(str(tabela.loc[linha, "Nro"]))
    pc.press("tab")

    dado_complemento = tabela.loc[linha, "Complemento"]
    if not pd.isna(dado_complemento):
        pc.write(str(dado_complemento))
    pc.press("tab")

    dado_bairro = tabela.loc[linha, "Bairro"]
    if not pd.isna(dado_bairro):
        pc.write(str(dado_bairro))
    pc.press("tab")

    dado_cep = tabela.loc[linha, "Bairro"]
    if not pd.isna(dado_cep):
        pc.write(str(dado_cep))
    pc.press("tab")

    pc.write(str(tabela.loc[linha, "Pais"]))
    pc.press("tab")

    pc.press("enter")
    pc.scroll(5000)