#!/usr/bin/env python3
from pathlib import Path

ROOT = Path('/Users/computer/laia-landing-page')
HERMES_HOME = Path.home() / '.hermes'
SOURCE_DIR = HERMES_HOME / 'memories'
TARGET_DIR = ROOT / 'ops' / 'hermes' / 'identity'

FILES = {
    'MEMORY.md': 'MEMORY.md',
    'USER.md': 'USER.md',
}


def main() -> None:
    TARGET_DIR.mkdir(parents=True, exist_ok=True)
    written = []
    for source_name, target_name in FILES.items():
        source = SOURCE_DIR / source_name
        if not source.exists():
            raise SystemExit(f'Missing source file: {source}')
        content = source.read_text()
        target = TARGET_DIR / target_name
        target.write_text(content)
        written.append(str(target))

    print('Exported Hermes identity files:')
    for path in written:
        print(f'- {path}')


if __name__ == '__main__':
    main()
