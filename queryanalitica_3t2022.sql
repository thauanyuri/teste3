use teste3ic;

select 
* from tabela_arquivo_relatorio_cadop 
join tabela_arquivo_teste_3t2022
on tabela_arquivo_relatorio_cadop.Registro_ANS = tabela_arquivo_teste_3t2022.REG_ANS
order by tabela_arquivo_teste_3t2022.VL_SALDO_FINAL 
desc limit 10;
  