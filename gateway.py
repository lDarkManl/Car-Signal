from fastapi import FastAPI, APIRouter
from car_rpc import OpenCar, CloseCar, StartEngine, GetFuel, GetAccumulatorCharge, SetTemperatureStartEngine, OpenWindows, GetOilTemp, GetEngineTemp

app = FastAPI()
router = APIRouter()

app.include_router(router)

@router.get('/open')
def request_open_car():
	open_car = OpenCar()
	return open_car()

@router.get('/open_windows')
def request_open_windows():
	open_windows = OpenWindows()
	return open_windows()

@router.get('/close')
def close_car():
	close_car = CloseCar()
	return close_car()

@router.get('/start_engine')
def start_engine():
	start_engine = StartEngine()
	return start_engine()

@router.post('/set_temperature_start_engine')
def set_temperature_start_engine(temperature: int):
	set_temp_start = SetTemperatureStartEngine()
	return set_temp_start(temperature)

@router.get('/get_fuel')
def get_fuel():
	get_fuel = GetFuel()
	return get_fuel()

@router.get('/get_accumulator_charge')
def get_accumulator_charge():
	get_accumulator_charge = GetAccumulatorCharge()
	return get_accumulator_charge()

@router.get('/get_oil_temp')
def get_oil_temp():
	get_oil_temp = GetOilTemp()
	return get_oil_temp()

@router.get('/get_engine_temp')
def get_engine_temp():
	get_engine_temp = GetEngineTemp()
	return get_engine_temp()