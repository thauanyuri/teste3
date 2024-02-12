import wget
from zipfile import ZipFile

link1 = 'https://dadosabertos.ans.gov.br/FTP/PDA/demonstracoes_contabeis/2021/1T2021.zip'
nome_arquivo_1 = '2021_1T.zip'
link2 = 'https://dadosabertos.ans.gov.br/FTP/PDA/demonstracoes_contabeis/2021/2T2021.zip'
nome_arquivo_2 = '2021_2T.zip'
link3='https://dadosabertos.ans.gov.br/FTP/PDA/demonstracoes_contabeis/2021/3T2021.zip'
nome_arquivo_3 ='2021_3T.zip'
link4='https://dadosabertos.ans.gov.br/FTP/PDA/demonstracoes_contabeis/2022/4T2021.zip'
nome_arquivo_4 ='2021_4T.zip'
link5='https://dadosabertos.ans.gov.br/FTP/PDA/demonstracoes_contabeis/2022/1T2022.zip'
nome_arquivo_5='2022_1T.zip'
link6='https://dadosabertos.ans.gov.br/FTP/PDA/demonstracoes_contabeis/2022/2T2022.zip'
nome_arquivo_6='2022_2T.zip'
link7='https://dadosabertos.ans.gov.br/FTP/PDA/demonstracoes_contabeis/2022/3T2022.zip'
nome_arquivo_7='2022_3T.zip'

link8='https://dadosabertos.ans.gov.br/FTP/PDA/demonstracoes_contabeis/2022/4T2022.zip'
nome_arquivo_8='2022_4T.zip'

link9='https://dadosabertos.ans.gov.br/FTP/PDA/operadoras_de_plano_de_saude_ativas/Relatorio_cadop.csv'
nome_arquivo_9='ANS_aquivo.csv'

download_primeiro_arquivo = wget.download(link1, nome_arquivo_1)
download_segundo_arquivo = wget.download(link2, nome_arquivo_2)
download_terceiro_arquivo = wget.download(link3, nome_arquivo_3)
download_quarto_arquivo = wget.download(link4, nome_arquivo_4)
download_quinto_arquivo = wget.download(link5, nome_arquivo_5)
download_sexto_arquivo = wget.download(link6, nome_arquivo_6)
download_setimo_arquivo = wget.download(link7, nome_arquivo_7)
download_oitavo_arquivo = wget.download(link8, nome_arquivo_8)
download_oitavo_arquivo = wget.download(link9, nome_arquivo_9)


zip = ZipFile('2021_1T.zip', 'w')
zip.extractall()

zip = ZipFile('2021_1T.zip', 'w')
zip.extractall()

zip = ZipFile('2021_1T.zip', 'w')
zip.extractall()

zip = ZipFile('2021_1T.zip', 'w')
zip.extractall()

zip = ZipFile('2022_1T.zip', 'w')
zip.extractall()

zip = ZipFile('2022_2T.zip', 'w')
zip.extractall()

zip = ZipFile('2022_3T.zip', 'w')
zip.extractall()

zip = ZipFile('2022_4T.zip', 'w')
zip.extractall()
