import pytest

def test_open_car(open_car):
	assert open_car().decode('utf-8') == 'car opened'

def test_close_car(close_car):
	assert close_car().decode('utf-8') == 'car closed'

def test_start_engine(start_engine):
	assert start_engine().decode('utf-8') == 'engine started'

	