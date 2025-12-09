
import json
import os
from pathlib import Path
from typing import Optional, Dict, Any

from .utils import bee2bee_home

CONFIG_FILE = "config.json"

DEFAULT_CONFIG = {
    # Default local supervisor for dev
    # Using 4002/4003 as 8000/4001 are often blocked/busy on Windows
    "bootstrap_url": "ws://127.0.0.1:4003", 
    "p2p_port": 0,    # Random
    "api_port": 4002
}

def get_config_path() -> Path:
    return bee2bee_home() / CONFIG_FILE

def load_config() -> Dict[str, Any]:
    path = get_config_path()
    if not path.exists():
        return DEFAULT_CONFIG.copy()
    try:
        return json.loads(path.read_text(encoding="utf-8"))
    except Exception:
        return DEFAULT_CONFIG.copy()

def save_config(config: Dict[str, Any]):
    path = get_config_path()
    path.write_text(json.dumps(config, indent=2), encoding="utf-8")

def get_bootstrap_url() -> str:
    # Env var overrides config
    env = os.getenv("BEE2BEE_BOOTSTRAP")
    if env:
        return env
    
    cfg = load_config()
    return cfg.get("bootstrap_url", DEFAULT_CONFIG["bootstrap_url"])

def set_bootstrap_url(url: str):
    cfg = load_config()
    cfg["bootstrap_url"] = url
    save_config(cfg)
