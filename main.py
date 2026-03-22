import asyncio
from contextlib import asynccontextmanager
from fastapi import FastAPI
import uvicorn
from inputs.moisture_sensor import moisture_sensor
from outputs.water_servo import water_servo
from history import history
from fastapi.responses import FileResponse


water = water_servo()
moisture = moisture_sensor()
history = history()

@asynccontextmanager
async def lifespan(app: FastAPI):
    asyncio.create_task(status_recorder_loop())
    yield

app = FastAPI(lifespan=lifespan)

@app.get("/water_on")
async def water_on():
    water.turn_on()

@app.get("/water_off")
async def water_off():
    water.turn_off()

@app.get("/status")
async def status():
    return {"water_on": water.is_on(), "soil_moisture": moisture.get_moisture_level()}

@app.get("/status_history")
async def status_history():
    return history.read_status_from_file()

@app.get("/history_chart")
async def status_recorder():
    return FileResponse(history.chart_data())

def write_status_to_file():
    (moisture_value, moisture_voltage) = moisture.get_moisture_level()
    history.write_status_to_file(water.is_on(), moisture_value, moisture_voltage)

async def status_recorder_loop():
    while True:
        write_status_to_file()
        await asyncio.sleep(60)

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)
