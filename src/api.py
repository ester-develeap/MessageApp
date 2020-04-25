from flask import Flask
from flask import jsonify
from flask import request
from src.message import Message

app = Flask(__name__)

#POST
@app.route("/AddMessage", methods=['POST'])
def add_message():
    new_message = request.get_json()
    Message.listMessage.append(new_message)
    return Message.listMessage[0]



if __name__ == "__main__":
    app.run()

