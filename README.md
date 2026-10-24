No diretório `Timpel`, para instalar as bibliotecas utilizadas nesse projeto, use `python -m pip install -r requirements.txt`. 

Para rodar o código principal, basta escrever `python main\main.py`.

Por fim, `python -m pytest .\validação.py -v` é o comando para checar os testes, rode ele no terminal dentro da pasta `main`.

-----------------
## Resposta 2)

### c)

Primeiro, seria feita a identificação das PEEPs a partir da função `review()`, presente no `main.py` e construída em `funcoes.py`. Já sabemos que o código de identificação da PEEP possui os mecanismos de checagem validados pelos testes definidos em `validação.py`. Logo, basta carregar os arquivos na pasta `data` para validá-los.

Ademais, caso o usuário queira revisar os dados por conta de alguma alteração exibida pelo `review()`, pode interromper a execução e fazer alguma correção. Senão, os gráficos serão gerados refletindo a análise proposta pelo script.

Por fim, acessando a pasta `resultados`, pode-se checar visualmente os gráficos gerados e as informações contidas neles, como a melhor PEEP identificada, alguma exceção e/ou caso especial.

## Resposta 3)

### a)

Deve retornar que nenhuma PEEP dentro daquele intervalo proposto foi a melhor, sendo um cenário plausível onde um paciente não precisa da tecnologia para auxiliar em sua ventilação mecânica.

### b)

Ao se cruzar mais de uma vez, o algoritmo aponta o número de cruzamentos, avisando o pesquisador/usuário para revisar os dados. Mesmo que a situação seja, à primeira vista, clinicamente infactível, isso pode refletir problemas na formatação ou erro do usuário na hora de carregar os dados/montar a base de dados.

### c)

É importante verificar cada um desses cenários diferentes. Uma porcentagem acima de 100 ou abaixo de 0 pode ser um problema de digitação, assim como passos fora de ordem e valores ausentes. O crucial é refletir essas exceções de volta para o operador fazer a validação; caso contrário, há risco de o viés do programador corrigir/alterar os dados errados, tornando-os falsos positivos. O código, ao aplicar o `review()`, exibe todas essas exceções e erros.

--------
## Uso de Inteligência Artificial

Ferramentas de inteligência artificial (Claude) foram utilizadas como apoio ao desenvolvimento deste projeto, de maneira responsável e complementar. O auxílio concentrou-se principalmente na configuração e apresentação dos gráficos gerados com Matplotlib (como posicionamento dos avisos em situações limite e tamanho dos eixos para os diferentes dados) e na identificação de ferramentas para testes automatizados, incluindo a biblioteca open-source pytest, cuja utilização foi posteriormente implementada e validada no projeto.

Sugestões fornecidas pela IA foram avaliadas e adaptadas conforme os requisitos do teste, tomando cuidado para manter o olhar crítico no uso da ferramenta.
A utilização da IA teve como objetivo apoiar o aprendizado e a produtividade, sem substituir a análise crítica, a tomada de decisões técnicas ou a validação do código.