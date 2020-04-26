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
def get_message():
    applicationId=request.args.get('applicationId', default = None ,type = int)
    sessionId=request.args.get('sessionId', default = None , type = str)
    messageId = request.args.get('messageId', default=None, type=str)
    list_messages = [element for element in Message.listMessage if element["application_id"]==applicationId or element["session_id"]==sessionId or element["message_id"]==messageId ]
    if messageId != None and list_messages.__len__()==1:
        return jsonify(list_messages[0])
    return jsonify(list_messages)

#Delete
@app.route("/DeleteMessage", methods=['DELETE'])
def delete_message():
    applicationId=request.args.get('applicationId', default = None ,type = int)
    sessionId=request.args.get('sessionId', default = None , type = str)
    messageId = request.args.get('messageId', default=None, type=str)
    count=Message.listMessage.__len__()
    if applicationId != None:
        Message.listMessage = [element for element in Message.listMessage if element["application_id"] != applicationId]
    if sessionId != None:
        Message.listMessage = [element for element in Message.listMessage if element["session_id"] != sessionId]
    if messageId != None:
        Message.listMessage = [element for element in Message.listMessage if element["message_id"] != messageId]
    return "{} messages deleted".format(count-Message.listMessage.__len__())


if __name__ == "__main__":
    app.run()

