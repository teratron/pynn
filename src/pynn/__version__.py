import os

__version__ = '0.1.1'
poetry_config = os.path.join('..', '..', 'pyproject.toml')


def change_version() -> None:
    with open(poetry_config) as handle:
        lines = handle.readlines()

    with open(poetry_config, 'w') as handle:
        for line in lines:
            equal = line.find('=')
            key = line[:equal].strip(' ')
            value = line[equal + 1:].strip(' ')
            if equal > 0 and key == 'version':
                line = line.replace(value, f'"{__version__}"\n')
            handle.writelines(line)
