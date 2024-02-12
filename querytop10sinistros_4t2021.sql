select 
* from tabela_arquivo_teste_4t2021 
where DESCRICAO 
like '%EVENTOS%' 
order by tabela_arquivo_teste_4t2021.VL_SALDO_FINAL 
desc limit 10;