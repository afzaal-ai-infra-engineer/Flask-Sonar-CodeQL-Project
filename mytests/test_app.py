import importlib.util
import sys
from pathlib import Path

# Load app.py dynamically
app_path = Path(__file__).resolve().parent.parent / "app.py"
spec = importlib.util.spec_from_file_location("app", app_path)
module = importlib.util.module_from_spec(spec)
sys.modules["app"] = module
spec.loader.exec_module(module)

app = module.app
