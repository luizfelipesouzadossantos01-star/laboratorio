from pathlib import Path

#Configuração inicial
mapeamento_arquivos={
    "calculo":"Exatas/Calculo",
    "arquitetura":"TI/Programação"
}
pasta_raiz=Path.cwd() / "automacao-arquivos"

# O .glob() varre a pasta e captura apenas os arquivos com a extensão que especificamos.
for caminhopdf in pasta_raiz.glob("*.pdf"):
    arquivo=caminhopdf.name.lower()
    #Varre o dicionario e compara a palavra chave e o arquivo
    for palavra_chave,subpasta in mapeamento_arquivos.items():
        if palavra_chave in arquivo:
            caminho_destino=pasta_raiz / subpasta
            #Garantir que o diretorio e parents exista
            caminho_destino.mkdir(parents=True,exist_ok=True)
            caminhopdf.rename(caminho_destino / caminhopdf.name)
            print(f"Sucesso: {caminhopdf.name} organizado.")
            break
