import json
from pathlib import Path
from funcoes import gerar_grafico, review


RAIZ = Path(__file__).resolve().parent.parent
ARQUIVO_JSON = RAIZ / "data" / "dataset.json"
PASTA_SAIDA = RAIZ / "resultados"


def main():
    with open(ARQUIVO_JSON, encoding="utf-8") as arquivo:
        pacientes = json.load(arquivo)
        
    if not review(pacientes):
        return

    for paciente in pacientes:
        paciente_id = paciente["Patient ID"]
        caminho_saida = PASTA_SAIDA / f"{paciente_id}_peep.png"

        gerar_grafico(paciente, caminho_saida)
        print(f"Gráfico gerado: {caminho_saida.name}")


if __name__ == "__main__":
    main()