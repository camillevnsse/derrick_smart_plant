from main import app, socketio

if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=5000)
    socketio.run(app, allow_unsafe_werkzeug=True)
