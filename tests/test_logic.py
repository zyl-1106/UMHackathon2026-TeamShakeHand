# tests/test_logic.py

import pytest

def mock_process_sos_logic(water_level, medical_tags):
    priority = "P3"
    
    if "Chest" in water_level or "Severe Bleeding" in medical_tags:
        priority = "P0"
    elif "Hips" in water_level:
        priority = "P1"
    elif "Knees" in water_level:
        priority = "P2"
        
    return priority

def test_critical_medical_priority():
    result = mock_process_sos_logic("Above Knees", ["Severe Bleeding"])
    assert result == "P0"

def test_chest_water_priority():
    result = mock_process_sos_logic("Chest", [])
    assert result == "P0"

def test_knee_water_priority():
    result = mock_process_sos_logic("Knees", [])
    assert result == "P2"

def test_safe_priority():
    result = mock_process_sos_logic("Ankles", [])
    assert result == "P3"