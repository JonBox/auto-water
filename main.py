from bottle import static_file, Bottle
import threading
import time
from boards.hardware_factory import get_board
from inputs.moisture_sensor import moisture_sensor
from outputs.water_servo import water_servo
from history import history

board = get_board()
water = water_servo(board)
moisture = moisture_sensor(board)
history = history()
app = Bottle()

def status_recorder_loop():
    while True:
        write_status_to_file()
        time.sleep(60)

def start_background_task():
    thread = threading.Thread(target=status_recorder_loop, daemon=True)
    thread.start()


@app.route('/api/water_on')
def water_on():
    water.turn_on()

@app.route("/api/water_off")
def water_off():
    water.turn_off()

@app.route("/api/status")
def status():
    return {"water_on": water.is_on(), "soil_moisture": moisture.get_moisture_level()}

@app.route("/api/status_history")
def status_history():
    return history.read_status_from_file()

@app.route('/dashboard.html')
def server_static():
    return static_file("dashboard.html", root='static')

def write_status_to_file():
    moisture_readings = moisture.get_moisture_level()
    history.write_status_to_file(water.is_on(), moisture_readings)

if __name__ == "__main__":
    start_background_task()
    app.run(host='0.0.0.0', port=8080, debug=True)