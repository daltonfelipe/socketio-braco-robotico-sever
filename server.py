import socketio
from app.services.socket import io
from app import create_app


if __name__ == '__main__':
    app = create_app()
    app.wsgi_app = socketio.WSGIApp(io, app.wsgi_app)
    app.run(debug=True, host='0.0.0.0')
