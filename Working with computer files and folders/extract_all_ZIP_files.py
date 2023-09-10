from pathlib import Path
import zipfile

destination_path = Path('destination')
for path in destination_path.rglob('*.zip'):
    with zipfile.ZipFile(path, 'r') as zf:
        final_path = destination_path / Path(path.stem)
        zf.extractall(path=final_path)
