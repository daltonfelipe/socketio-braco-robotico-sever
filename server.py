import eventlet
import socketio
from servo import ServoPWM


base = ServoPWM(18)
height = ServoPWM(12)
claw = ServoPWM(13)
front = ServoPWM(19)

io = socketio.Server(ping_timeout=30)

app = socketio.WSGIApp(io, static_files={
    '/': {'content_type': 'text/html', 'filename': 'index.html'}
})

@io.event
def connect(sid, environ):
    print('A user is connected!', sid)
    io.emit('welcome', data='welcome')


@io.on('y-axis')
def move_arm_height(sid, data):
    height.set_angle(float(data))


@io.on('x-axis')
def move_arm_base(sid, data):
    base.set_angle(float(data))


@io.on('estado-garra')
def move_arm_claw(sid, data):
    claw.set_angle(float(data))


@io.on('estado-front')
def move_arm_front(sid, data):
    front.set_angle(float(data))


if __name__ == '__main__':
    eventlet.wsgi.server(eventlet.listen(('', 5000)), app)
