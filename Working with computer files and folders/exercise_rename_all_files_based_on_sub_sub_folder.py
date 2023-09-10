from pathlib import Path

root_dir = Path('exercise1')
file_paths = root_dir.glob('**/*')
for path in file_paths:
    if path.is_file():
        parent_folder = path.parts
        subfolders = path.parts[1:3]
        if subfolders[1] not in path.name:
            new_filename = subfolders[0] + '-' + subfolders[1] + '-' + path.name
            # new_filename = "-".join(subfolders) + '-' + path.name
            new_filpath = path.with_name(new_filename)
            path.rename(new_filpath)
