import pytest
from flask import Flask
import importlib.util
import sys
from pathlib import Path

# Dynamically load app.py
app_path = Path(__file__).resolve().parent.parent / "app.py"
spec = importlib.util.spec_from_file_location("app", app_path)
module = importlib.util.module_from_spec(spec)
sys.modules["app"] = module
spec.loader.exec_module(module)

app = module.app
client = app.test_client()

def test_home_status_code():
    """Test that the home page returns HTTP 200"""
    response = client.get("/")
    assert response.status_code == 200

def test_home_content():
    """Test that home page contains expected text"""
    response = client.get("/")
    assert b"Afzaal DevOps" in response.data
