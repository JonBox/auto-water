import asyncio
from contextlib import asynccontextmanager
from bottle import route, static_file, Bottle
from inputs.moisture_sensor import moisture_sensor
from outputs.water_servo import water_servo
from history import history


water = water_servo()
moisture = moisture_sensor()
history = history()
app = Bottle()

@asynccontextmanager
async def lifespan():
    asyncio.create_task(status_recorder_loop())
    yield

@app.route('/water_on')
def water_on():
    water.turn_on()

@app.route("/water_off")
def water_off():
    water.turn_off()

@app.route("/status")
def status():
    return {"water_on": water.is_on(), "soil_moisture": moisture.get_moisture_level()}

@app.route("/status_history")
def status_history():
    return history.read_status_from_file()

@app.route("/history_chart")
def status_recorder():
    return static_file(history.chart_data(), root=".", mimetype="image/png")

def write_status_to_file():
    (moisture_value, moisture_voltage) = moisture.get_moisture_level()
    history.write_status_to_file(water.is_on(), moisture_value, moisture_voltage)

async def status_recorder_loop():
    while True:
        write_status_to_file()
        await asyncio.sleep(60)

if __name__ == "__main__":
    app.run(host='localhost', port=8080, debug=True)