import socketio
from servo import ServoPWM

io = socketio.Server(async_mode='threading', ping_timeout=30)

base = ServoPWM(18)
height = ServoPWM(12)
claw = ServoPWM(13)
front = ServoPWM(19)

connected_users = []

@io.event
def connect(sid, environ):
    connected_users.append(sid)
    data = {
        'connected_users_length': len(connected_users),
        'sid': sid
    }
    io.emit('connected-users', data=data)


@io.event
def disconnect(sid):
    connected_users.remove(sid)
    print(connected_users)
    data = {
        'connected_users_length': len(connected_users),
        'sid': sid
    }
    io.emit('connected-users', data=data)


@io.on('y-axis')
def move_arm_height(sid, data):
    height.set_angle(float(data))
    io.emit('height-value', data=data)


@io.on('x-axis')
def move_arm_base(sid, data):
    base.set_angle(float(data))
    io.emit('base-value', data=data)


@io.on('estado-garra')
def move_arm_claw(sid, data):
    claw.set_angle(float(data))
    io.emit('claw-value', data=data)


@io.on('estado-front')
def move_arm_front(sid, data):
    front.set_angle(float(data))
    io.emit('front-value', data=data)

