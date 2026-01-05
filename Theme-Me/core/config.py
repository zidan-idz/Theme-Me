import json
import os
from pathlib import Path

CONFIG_DIR = Path.home() / ".theme-me"
CONFIG_FILE = CONFIG_DIR / "config.json"

DEFAULT_CONFIG = {
    "current_theme": None,
    "current_font": None,
    "current_background": None,
    "first_run": True
}

def load_config():
    if not CONFIG_FILE.exists():
        save_config(DEFAULT_CONFIG)
        return DEFAULT_CONFIG
    
    try:
        with open(CONFIG_FILE, "r") as f:
            return json.load(f)
    except Exception:
        return DEFAULT_CONFIG

def save_config(config):
    if not CONFIG_DIR.exists():
        CONFIG_DIR.mkdir(parents=True, exist_ok=True)
        
    with open(CONFIG_FILE, "w") as f:
        json.dump(config, f, indent=2)

def update_config(key, value):
    config = load_config()
    config[key] = value
    save_config(config)
