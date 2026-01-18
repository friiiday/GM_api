from flask import Flask, request, jsonify
import serial

app = Flask(__name__)

laser = serial.Serial('/dev/ttyACM0', 115200, timeout=1)

@app.route("/send", methods=["POST"])
def send_gcode():
    data = request.json
    gcode = data.get("gcode")

    if not gcode:
        return jsonify({"error": "No G-code provided"}), 400

    laser.write((gcode + "\n").encode())
    return jsonify({"status": "sent", "gcode": gcode})

@app.route("/status")
def status():
    return jsonify({"status": "online"})
