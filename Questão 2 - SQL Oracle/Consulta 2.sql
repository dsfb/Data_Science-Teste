SELECT ALUNOS.NOME FROM ALUNOS
WHERE ALUNOS.RA NOT IN (SELECT HISTORICO.RA FROM HISTORICO, DISCIPLINAS
WHERE HISTORICO.COD_DISC = DISCIPLINAS.COD_DISC AND
HISTORICO.NOTA <6)
