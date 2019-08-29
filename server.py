import eventlet
import socketio

io = socketio.Server(ping_timeout=30)

app = socketio.WSGIApp(io, static_files={
    '/': {'content_type': 'text/html', 'filename': 'index.html'}
})

@io.event
def connect(sid, environ):
    print('A user is connected!', sid)
    io.emit('welcome', data='welcome')


@io.on('y-axis')
def print_y_axis_data(sid, data):
    print('Y-axis: ', data)


@io.on('x-axis')
def print_x_axis_data(sid, data):
    print('XS-axis: ', data)


@io.on('estado-garra')
def estado_garra(sid, msg):
    print(f'Garra: {msg}')


@io.on('estado-front')
def estado_front(sid, msg):
    print(f'Front: {msg}')


if __name__ == '__main__':
    eventlet.wsgi.server(eventlet.listen(('', 5000)), app)
