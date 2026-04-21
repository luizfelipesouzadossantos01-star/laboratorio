from pathlib import Path

#Altere estas variáveis com o nome da pasta de origem e onde deseja colocar.
pasta_raiz="automacao-arquivos"
nome_destino="teste"

raiz=Path.cwd() / pasta_raiz
caminho_destino=Path.cwd() / pasta_raiz /nome_destino

#Garantir que a pasta exista
caminho_destino.mkdir(exist_ok=True)

# O .glob() varre a pasta e captura apenas os arquivos com a extensão que especificamos.
for caminhopdf in raiz.glob("*.pdf"):
    if "calculo" in caminhopdf.name.lower():
        #O método .rename serve tanto para renomear o arquivo quanto para movê-lo de diretório.
        caminhopdf.rename(caminho_destino / caminhopdf.name)
        #O .name ignora o caminho completo e extrai apenas o nome final do arquivo (ex: calculo.pdf).
        print(f"Sucesso o arquivo {caminhopdf.name} foi movido para {caminho_destino}.")
