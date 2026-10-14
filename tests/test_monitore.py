import pytest

def test_get_fuel(get_fuel):
	assert float(get_fuel().decode('utf-8')) == 5

def test_set_temperature_start_engine(set_temp):
	assert set_temp(20).decode('utf-8') == 'success'

def test_get_accumulator_charge(get_accum):
	assert float(get_accum().decode('utf-8')) == 13