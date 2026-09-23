"""Organize arquivos de uma pasta por extensão."""

import argparse
import shutil
from collections import Counter
from pathlib import Path


def classify_file(file_path: Path) -> str:
    """Retorna a categoria de um arquivo com base na extensão."""
    # TODO: Remova o ponto da extensão e use "outros" quando ela não existir.
    return ""


def list_files(source_dir: Path) -> list[Path]:
    """Retorna somente os arquivos que estão diretamente na pasta de origem."""
    # TODO: Ignore subpastas.
    return []


def organize_files(source_dir: Path, destination_dir: Path) -> tuple[Counter, int, int]:
    """Move arquivos e retorna contagens por categoria, movidos e ignorados."""
    categories = Counter()
    moved_count = 0
    skipped_count = 0

    for file_path in list_files(source_dir):
        category = classify_file(file_path)
        categories[category] += 1
        category_dir = destination_dir / category
        target_path = category_dir / file_path.name

        # TODO: Crie a pasta de categoria e mova o arquivo sem sobrescrever destinos.
        # Atualize moved_count ou skipped_count de acordo com o resultado.

    return categories, moved_count, skipped_count


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description="Organiza arquivos por extensão."
    )
    parser.add_argument("source", type=Path, help="Pasta que contém os arquivos.")
    parser.add_argument(
        "--destino",
        type=Path,
        help="Pasta de destino; por padrão, usa a pasta de origem.",
    )
    return parser.parse_args()


def main() -> None:
    args = parse_args()
    source_dir = args.source
    destination_dir = args.destino or source_dir

    # TODO: Valide que source_dir existe e é uma pasta.
    categories, moved_count, skipped_count = organize_files(
        source_dir, destination_dir
    )

    print("Arquivos encontrados por categoria:")
    for category, count in sorted(categories.items()):
        print(f"- {category}: {count}")
    print(f"Movidos: {moved_count}")
    print(f"Ignorados: {skipped_count}")


if __name__ == "__main__":
    main()
