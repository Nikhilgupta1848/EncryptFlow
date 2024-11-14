from flask import Flask, render_template, request, jsonify
import queue

app = Flask(__name__)
message_queue = queue.Queue()

# Updated Caesar Cipher function for all characters
def caesar_cipher(text, shift, encrypt=True):
    result = ""
    shift = shift if encrypt else -shift
    for char in text:
        shifted_char = chr((ord(char) + shift) % 256)  # Use modulo 256 to keep within ASCII range
        result += shifted_char
    return result

# Route for the main page
@app.route("/")
def index():
    return render_template("index.html")

# Route for sending a message
@app.route("/send", methods=["POST"])
def send_message():
    data = request.json
    message = data.get("message")
    shift = int(data.get("shift"))
    encrypted_message = caesar_cipher(message, shift, True)
    message_queue.put(encrypted_message)
    return jsonify({"queue": list(message_queue.queue)})

# Route for receiving a message
@app.route("/receive", methods=["GET"])
def receive_message():
    if not message_queue.empty():
        encrypted_message = message_queue.get()
        shift = int(request.args.get("shift"))
        decrypted_message = caesar_cipher(encrypted_message, shift, False)
        return jsonify({"decrypted_message": decrypted_message, "queue": list(message_queue.queue)})
    return jsonify({"error": "Queue is empty."}), 404

if __name__ == "__main__":
    app.run(debug=True)
