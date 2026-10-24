Resposta 2)
c)
    Primeiro seria feita a identificação dos PEEPs a partir da função review() presente no 'main.py' e construído em 'funcoes.py'. Já sabemos que o código de identificar a PEEP possui os mecanismos de checagem validados pelos testes definidos em 'validação.py'. Logo, basta carregar os arquivos na pasta 'data' para validá-los. 

    Ademais, caso o usuário queira revisar os dados por conta de alguma alteração exibida pelo review(), pode interromper a execução e fazer alguma correção, senão, os gráficos serão gerados refletindo a análise proposta pelo script.

    Por fim, acessando a pasta 'resultados' pode-se checar visualmente os gráficos gerados e as informações contidas nele, como a melhor PEEP identificada, alguma excessão e/ou caso especial. 

Resposta 3)
a)  
    Deve retornar que nenhum PEEP dentro daquele intervalo proposto foi o melhor, sendo um cenário plausível onde um paciente não precisa da tecnologia para auxiliar em sua ventilação mecânica.

b)
    Ao se cruzar mais de uma vez, o algoritmo aponta o nº de cruzamentos, avisando o pesquisador/usuário para revisar os dados. Mesmo que a situação seja a primeira vista clinicamente infactível, isso pode refletir problemas na formatação ou erro do usuário na hora de carregar os dados/montar a base de dados.

c)
    É importante verificar cada um desses cenários diferentes. Uma porcentagem acima de 100 ou abaixo de 0 pode ser um problema de digitação, assim como passos fora de ordem e valores ausentes. O crucial é refletir essas exceções de volta para o operador fazer a validação, caso contrário, há risco do viés do programador corrigir/alterar os dados errados tornando-os falso-positivos. O código ao aplicar o review() exibe todas essas excessões e erros.