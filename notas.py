def validar_nota(nota):
    """Retorna True quando a nota está no intervalo de 0 a 10."""
    return 0 <= nota <= 10


def calcular_media(notas):
    """Calcula a média das notas ou sinaliza uma lista vazia."""
    if not notas:
        raise ValueError("lista de notas vazia")

    return sum(notas) / len(notas)


def obter_situacao(media):
    """Classifica a situação do aluno a partir da média."""
    if media >= 7:
        return "Aprovado"
    if media >= 5:
        return "Recuperacao"
    return "Reprovado"