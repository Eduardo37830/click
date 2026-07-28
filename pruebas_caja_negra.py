"""Casos de prueba de caja negra — Anexo V&V (auditoría click).

Técnica: partición en clases de equivalencia + análisis de valores límite,
sobre IntRange, Choice y flags booleanos. Ejecutado con click.testing.CliRunner.
"""

import click
from click.testing import CliRunner


@click.command()
@click.option("--n", type=click.IntRange(0, 10))
def cmd_intrange(n):
    click.echo(f"n={n}")


@click.command()
@click.option("--n", type=click.IntRange(0, 10, clamp=True))
def cmd_intrange_clamp(n):
    click.echo(f"n={n}")


@click.command()
@click.option("--color", type=click.Choice(["red", "green", "blue"]))
def cmd_choice(color):
    click.echo(f"color={color}")


@click.command()
@click.option("--verbose", is_flag=True, default=False)
def cmd_flag(verbose):
    click.echo(f"verbose={verbose}")


runner = CliRunner()


def test_tc1_intrange_valor_medio_valido():
    """TC1 — partición válida: valor dentro del rango (5 de [0,10])."""
    result = runner.invoke(cmd_intrange, ["--n", "5"])
    assert result.exit_code == 0
    assert result.output.strip() == "n=5"


def test_tc2_intrange_limite_inferior_incluido():
    """TC2 — valor límite: n=0 (frontera inferior, inclusiva)."""
    result = runner.invoke(cmd_intrange, ["--n", "0"])
    assert result.exit_code == 0
    assert result.output.strip() == "n=0"


def test_tc3_intrange_limite_superior_incluido():
    """TC3 — valor límite: n=10 (frontera superior, inclusiva)."""
    result = runner.invoke(cmd_intrange, ["--n", "10"])
    assert result.exit_code == 0
    assert result.output.strip() == "n=10"


def test_tc4_intrange_bajo_el_limite_invalido():
    """TC4 — partición inválida: n=-1, justo bajo la frontera inferior."""
    result = runner.invoke(cmd_intrange, ["--n", "-1"])
    assert result.exit_code == 2
    assert "not in the range" in result.output


def test_tc5_intrange_sobre_el_limite_invalido():
    """TC5 — partición inválida: n=11, justo sobre la frontera superior."""
    result = runner.invoke(cmd_intrange, ["--n", "11"])
    assert result.exit_code == 2
    assert "not in the range" in result.output


def test_tc6_intrange_clamp_ajusta_al_limite():
    """TC6 — valor fuera de rango con clamp=True se ajusta al límite (15 -> 10)."""
    result = runner.invoke(cmd_intrange_clamp, ["--n", "15"])
    assert result.exit_code == 0
    assert result.output.strip() == "n=10"


def test_tc7_choice_valor_valido():
    """TC7 — partición válida: valor presente en el conjunto de Choice."""
    result = runner.invoke(cmd_choice, ["--color", "green"])
    assert result.exit_code == 0
    assert result.output.strip() == "color=green"


def test_tc8_choice_valor_invalido():
    """TC8 — partición inválida: valor ausente del conjunto de Choice."""
    result = runner.invoke(cmd_choice, ["--color", "purple"])
    assert result.exit_code == 2
    assert "is not one of" in result.output


def test_tc9_flag_ausente_usa_default_false():
    """TC9 — partición: flag no provisto, debe tomar el default False."""
    result = runner.invoke(cmd_flag, [])
    assert result.exit_code == 0
    assert result.output.strip() == "verbose=False"


def test_tc10_flag_presente_activa_true():
    """TC10 — partición: flag provisto explícitamente, debe activar True."""
    result = runner.invoke(cmd_flag, ["--verbose"])
    assert result.exit_code == 0
    assert result.output.strip() == "verbose=True"
