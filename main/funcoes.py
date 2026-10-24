import math
from pathlib import Path
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

def identificar_peep(etapas):
    if len(etapas) < 2:
        raise ValueError("São necessários pelo menos dois registros.")

    peep = []
    diferencas = []

    for etapa in etapas:
        try:
            p = etapa["PEEP"]
            hiper = etapa["Hyperdistension"]
            colapso = etapa["Collapse"]
        except KeyError as erro:
            raise ValueError(
                f"Campo ausente nos dados: {erro}. Por favor, revise a"\
                "base de dados"
            ) from erro

        for valor in (p, hiper, colapso):
            if (
                isinstance(valor, bool)
                or not isinstance(valor, (int, float))
                or not math.isfinite(valor)
            ):
                raise ValueError("Os dados contêm valores inválidos.")

        if not (0 <= hiper <= 100 and 0 <= colapso <= 100):
            raise ValueError("Os percentuais devem estar entre 0 e 100.")

        peep.append(p)
        diferencas.append(hiper - colapso)

    if any(peep[i] <= peep[i + 1] for i in range(len(peep) - 1)):
        raise ValueError("A PEEP deve estar em ordem decrescente. Por favor, revise" \
        "a base de dados")


    cruzamentos = []
    tolerancia = 1e-9

    for i in range(len(diferencas) - 1):
        atual = diferencas[i]
        proxima = diferencas[i + 1]

        if atual * proxima < 0:
            cruzamentos.append(peep[i])

    for i, diferenca in enumerate(diferencas):
        if abs(diferenca) <= tolerancia:
            if i == 0:
                raise ValueError(
                    "Não há uma etapa anterior ao primeiro ponto."
                )

            antes = diferencas[i - 1]
            depois = diferencas[i + 1] if i + 1 < len(diferencas) else None

            if depois is None or antes * depois < 0:
                cruzamentos.append(peep[i - 1])

    if len(cruzamentos) == 0:
        return None

    if len(cruzamentos) > 1:
        raise ValueError(
            f"Foram encontrados {len(cruzamentos)} cruzamentos. Por favor, revise os dados"
        )

    return cruzamentos[0]

def review(pacientes):
    resultados = []

    if isinstance(pacientes, dict):
        pacientes = [pacientes]

    for paciente in pacientes:
        paciente_id = paciente.get("Patient ID", "ID desconhecido")
        etapas = paciente.get("Titration Steps", [])

        try:
            peep = identificar_peep(etapas)

            if peep is None:
                melhor_peep = "Nenhum cruzamento"
            else:
                melhor_peep = peep

            erro = ""

        except ValueError as excecao:
            melhor_peep = None
            erro = str(excecao)

        resultados.append({
            "ID": paciente_id,
            "Melhor PEEP identificada": melhor_peep,
            "Erro": erro
        })

    df = pd.DataFrame(resultados)

    print("\nREVISÃO DOS RESULTADOS")
    print(df.to_string(index=False))

    while True:
        resposta = input(
            "\nProsseguir com a geração dos gráficos? (y/n): "
        ).strip().lower()

        if resposta == "y":
            return True

        elif resposta == "n":
            print("Execução interrompida pelo usuário.")
            return False

        else:
            print("Resposta inválida. Digite 'y' ou 'n'.")

def gerar_grafico(paciente, caminho_saida, passo_x=2, passo_y=10):
    etapas = paciente["Titration Steps"]
    paciente_id = paciente["Patient ID"]

    peep = [etapa["PEEP"] for etapa in etapas]
    hiper = [etapa["Hyperdistension"] for etapa in etapas]
    colapso = [etapa["Collapse"] for etapa in etapas]

    aviso = None

    try:
        peep_selecionada = identificar_peep(etapas)
    except ValueError as erro:
        peep_selecionada = None
        aviso = str(erro)

    fig, ax = plt.subplots(figsize=(11.69, 8.27))

    ax.plot(
        peep, hiper,
        marker="o", markersize=6, linewidth=2,
        label="Hiperdistensão",
    )
    ax.plot(
        peep, colapso,
        marker="s", markersize=6, linewidth=2,
        label="Colapso",
    )

    ax.set_title(
        f"Titulação de PEEP — Paciente {paciente_id}",
        fontsize=18,
        pad=16,
    )
    ax.set_xlabel("PEEP (cmH₂O)", fontsize=14)
    ax.set_ylabel("Percentual (%)", fontsize=14)
    y_dados = max(max(hiper), max(colapso))
    y_topo = max(math.ceil(y_dados / passo_y) * passo_y, passo_y)  # nunca menor que 1 passo
    ax.set_yticks(np.arange(0, y_topo + passo_y, passo_y))
    ax.set_ylim(-passo_y / 2, y_topo + passo_y / 2)
    x_min = math.floor(min(peep) / passo_x) * passo_x
    x_max = math.ceil(max(peep) / passo_x) * passo_x
    ax.set_xticks(np.arange(x_min, x_max + passo_x, passo_x))
    ax.set_xlim(x_min - passo_x / 2, x_max + passo_x / 2)

    ax.tick_params(labelsize=12)
    ax.grid(True, linestyle="--", alpha=0.35)
    ax.legend(fontsize=12)
    ax.invert_xaxis()
    ax.tick_params(labelsize=12)
    ax.grid(True, linestyle="--", alpha=0.35)
    ax.legend(fontsize=12)

    if aviso:
        ax.text(
            0.02, 0.96,
            f"Aviso: {aviso}",
            transform=ax.transAxes,
            va="top",
            ha="left",
            fontsize=11,
            wrap=True,
            bbox={"facecolor": "white", "alpha": 0.9},
        )

    elif peep_selecionada is None:
        ax.text(
            0.02, 0.96,
            "Nenhum cruzamento identificado",
            transform=ax.transAxes,
            va="top",
            ha="left",
            fontsize=11,
        )

    else:
        ax.axvline(
            peep_selecionada,
            color="black",
            linestyle="--",
            linewidth=1.8,
        )

        ax.text(
            0.98, 0.96,
            f"Melhor PEEP:\n{peep_selecionada:g} cmH₂O",
            transform=ax.transAxes,
            ha="right",
            va="top",
            fontsize=11,
            fontweight="bold",
            bbox={
                "facecolor": "white",
                "alpha": 0.9,
                "edgecolor": "none",
            },
        )

    fig.subplots_adjust(
        left=0.10,
        right=0.96,
        bottom=0.12,
        top=0.88,
    )

    caminho_saida = Path(caminho_saida)
    caminho_saida.parent.mkdir(parents=True, exist_ok=True)

    fig.savefig(
        caminho_saida,
        dpi=300,
        facecolor="white",
    )

    plt.close(fig)
