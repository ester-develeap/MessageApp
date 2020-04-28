import json
import sys

from flask import Flask,jsonify,request
from src.messages_list import MessageList

app = Flask(__name__)

#POST
@app.route("/AddMessage", methods=['POST'])
def add_message():
    new_message = request.get_json()
    try:
        MessageList.add_new_message(new_message)
    except:
        return str(sys.exc_info()[1])
    return "the message was added succesfully"

#GET
@app.route("/GetMessage", methods=['GET'])
def get_message():
    applicationId=request.args.get('applicationId', default = None ,type = int)
    sessionId=request.args.get('sessionId', default = None , type = str)
    messageId = request.args.get('messageId', default=None, type=str)
    list_messages = [element for element in MessageList.get_messages() if element.application_id==applicationId or element.session_id==sessionId or element.message_id==messageId ]
    if messageId != None and list_messages.__len__()==1:
        return list_messages[0].dump()
    return json.dumps([element.dump() for element in list_messages])



#Delete
@app.route("/DeleteMessage", methods=['DELETE'])
def delete_message():
    applicationId=request.args.get('applicationId', default = None ,type = int)
    sessionId=request.args.get('sessionId', default = None , type = str)
    messageId = request.args.get('messageId', default=None, type=str)
    count=MessageList.get_messages().__len__()
    MessageList.delete_messages(applicationId,sessionId,messageId)
    return "{} messages deleted".format(count - MessageList.get_messages().__len__())


if __name__ == "__main__":
    app.run()

