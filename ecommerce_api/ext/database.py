import json
from pathlib import Path

import settings

db = None


def init_app(_):
    root_folder = Path(__file__).parent.parent.parent
    full_filepath = root_folder / settings.DATABASE_FILENAME

    global db
    db = json.loads(full_filepath.read_text())
