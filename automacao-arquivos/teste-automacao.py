from pathlib import Path

#Altere estas variáveis com o nome do arquivo inicial e da pasta de origem.
arquivo="calculo.pdf"
pasta_raiz="automacao-arquivos"

#Pasta que deseja colocar os arquivos
pasta_destinada="teste"

arquivo_caminho= Path.cwd() / pasta_raiz / arquivo
pasta_destinada=Path.cwd() / pasta_raiz /pasta_destinada

arquivo_caminho.rename(pasta_destinada / arquivo_caminho.name)

#O método .rename serve tanto para renomear o arquivo quanto para movê-lo de diretório.
#O .name ignora o caminho completo e extrai apenas o nome final do arquivo (ex: calculo.pdf).