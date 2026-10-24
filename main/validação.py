import pytest
from funcoes import identificar_peep

def criar_etapas(peep, hiper, colapso):
    return [
        {
            "PEEP": p,
            "Hyperdistension": h,
            "Collapse": c,
        }
        for p, h, c in zip(peep, hiper, colapso)
    ]

def test_identifica_peep_anterior_ao_cruzamento():#caso de funcionamento normal
    etapas = criar_etapas(
        peep=[15, 12, 9],
        hiper=[60, 40, 20],
        colapso=[10, 30, 50],
    )
    resultado = identificar_peep(etapas)
    assert resultado == 12


#quando não há cruzamento entre as duas curvas, não se aplica o critério de melhor
#peep. Logo o retorno é None
def test_retorna_none_quando_nao_ha_cruzamento():
    etapas = criar_etapas(
        peep=[15, 12, 9],
        hiper=[60, 50, 40],
        colapso=[10, 20, 30],
    )
    resultado = identificar_peep(etapas)
    assert resultado is None

#múltiplos cruzamentos não fazem sentido dado que
#o comportamento da hiperdistensão e colapso dos alvéolos do paciente
#deve ser monótono em relação à PEEP, que exibe comportamento monótono também
def test_rejeita_multiplos_cruzamentos():
    etapas = criar_etapas(
        peep=[15, 12, 9, 6],
        hiper=[60, 20, 60, 20],
        colapso=[10, 50, 10, 50],
    )
    with pytest.raises(ValueError):
        identificar_peep(etapas)

#Para conjuntos de dados muito curtos a função rejeita a entrada
#dado que os dados não refletem a redução periódica característica da
#titulação de PEEP
def test_rejeita_menos_de_duas_etapas():
    etapas = criar_etapas(
        peep=[12],
        hiper=[40],
        colapso=[30],
    )
    with pytest.raises(ValueError):
        identificar_peep(etapas)

#É possível ordenar os valores em ordem decrescente mas isso 
#vai de encontro à ética da pesquisa e portanto é melhor
#o próprio pesquisador revisar, validar ou corrigir os dados
def test_rejeita_peep_fora_de_ordem():
    etapas = criar_etapas(
        peep=[15, 9, 12],
        hiper=[60, 40, 20],
        colapso=[10, 30, 50],
    )
    with pytest.raises(ValueError):
        identificar_peep(etapas)

#idem ao teste acima.
def test_rejeita_percentual_fora_do_intervalo():
    etapas = criar_etapas(
        peep=[15, 12, 9],
        hiper=[60, 110, 20],
        colapso=[10, 30, 50],
    )
    with pytest.raises(ValueError):
        identificar_peep(etapas)

#outra situação onde é melhor o pesquisador revisar os dados que foram 
#coletados
def test_rejeita_valor_ausente():
    etapas = criar_etapas(
        peep=[15, 12, 9],
        hiper=[60, None, 20],
        colapso=[10, 30, 50],
    )
    with pytest.raises(ValueError):
        identificar_peep(etapas)
