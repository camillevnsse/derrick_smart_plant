# lancer le serveur principal et le socket
from main import app, socketio

if __name__ == "__main__":
    app.run(debug=True, port=5000)
    socketio.run(app, allow_unsafe_werkzeug=True)
