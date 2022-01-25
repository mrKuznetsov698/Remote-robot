from flask import Flask, send_file
import Robot

rpinE = 2 #PWM pin
rpinD = 3 #Direction pin
lpinE = 1
lpinD = 0
defaultSpeed = 40

app = Flask(__name__)
motorR = Robot.Motor(rpinE, rpinD)
motorL = Robot.Motor(lpinE, lpinD)


@app.route('/')
def home():
    return send_file('static/index.html')


@app.route('/<file>')
def file_send(file):
    return send_file('static/' + file)


@app.route('/Direction/<dir>')
def runMotors(dir):
    if dir == 'stop':
        motorR.run('stop', 0)
        motorL.run('stop', 0)
    elif dir == 'forward':
        motorR.run('forward', defaultSpeed)
        motorL.run('forward', defaultSpeed)
    elif dir == 'backward':
        motorR.run('backward', defaultSpeed)
        motorL.run('backward', defaultSpeed)
    elif dir == 'right':
        motorR.run('forward', defaultSpeed)
        motorL.run('backward', defaultSpeed)
    elif dir == 'left':
        motorR.run('backward', defaultSpeed)
        motorL.run('forward', defaultSpeed)
    return 'ok'


@app.route('/Speed/<spd>')
def spd_change(spd):
    global defaultSpeed
    defaultSpeed = spd
    print(defaultSpeed)
    return 'ok'


app.run(host='0.0.0.0', port=80)