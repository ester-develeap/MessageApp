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
    return new_message

#GET
@app.route("/GetMessage", methods=['GET'])
def get_message_application():
    applicationId=request.args.get('applicationId',type = int)
    list_messages = [element for element in Message.listMessage if element["application_id"]==applicationId]
    return jsonify(list_messages)





if __name__ == "__main__":
    app.run()

