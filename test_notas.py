import pytest

from notas import calcular_media, obter_situacao, validar_nota


@pytest.mark.parametrize(
    ("nota", "resultado"),
    [
        (0, True),
        (10, True),
        (-1, False),
        (11, False),
        (5, True),
    ],
)
def test_validar_nota(nota, resultado):
    assert validar_nota(nota) is resultado


def test_media_turma_a(notas_exemplo):
    assert calcular_media(notas_exemplo) == 7


def test_media_turma_b(notas_exemplo):
    assert obter_situacao(calcular_media(notas_exemplo)) == "Aprovado"


def test_calcular_media_lista_vazia():
    with pytest.raises(ValueError, match="^lista de notas vazia$"):
        calcular_media([])


@pytest.mark.parametrize(
    ("media", "situacao"),
    [
        (8, "Aprovado"),
        (7, "Aprovado"),
        (6, "Recuperacao"),
        (5, "Recuperacao"),
        (4.9, "Reprovado"),
    ],
)
def test_obter_situacao(media, situacao):
    assert obter_situacao(media) == situacao


def test_matricula_aluno():
    turma = []
    turma.append("Ana")
    assert len(turma) == 1


def test_matricula_outro_aluno():
    turma = []
    turma.append("Bruno")
    assert len(turma) == 1