import json
import sys

from flask import Flask,request
from src.messages_list import MessageList

app = Flask(__name__)

##Health
#@app.route("/")
#def helth():
#    return "hello"

#POST
@app.route("/AddMessage", methods=['POST'])
def add_message():
    new_message = request.get_json(force=True)
    try:
        MessageList.add_new_message(new_message)
    except:
        return str(sys.exc_info()[1]),400
    return "the message was added succesfully"

#GET
@app.route("/GetMessage", methods=['GET'])
def get_message():
    applicationId=request.args.get('applicationId', default = None ,type = int)
    sessionId=request.args.get('sessionId', default = None , type = str)
    messageId = request.args.get('messageId', default=None, type=str)
    if applicationId != None:
        r=json.dumps(MessageList.get_messages("applicationId",applicationId))
        return (r if r!='null' else "[]")
    elif sessionId != None:
        r= json.dumps(MessageList.get_messages("sessionId", sessionId))
        return (r if r!='null' else "[]")
    elif messageId != None:
        r=MessageList.get_messages("messageId", messageId)
        return (r[0] if r else {})
    else:
        return "arguments not correct",400

#Delete
@app.route("/DeleteMessage", methods=['DELETE'])
def delete_message():
    applicationId=request.args.get('applicationId', default = None ,type = int)
    sessionId=request.args.get('sessionId', default = None , type = str)
    messageId = request.args.get('messageId', default=None, type=str)

    if applicationId != None:
        rowcount=MessageList.delete_messages("applicationId",applicationId)
        return "{} messages deleted".format(rowcount)
    elif sessionId != None:
        rowcount= MessageList.delete_messages("sessionId", sessionId)
        return "{} messages deleted".format(rowcount)
    elif messageId != None:
        rowcount=MessageList.delete_messages("messageId", messageId)
        return "{} messages deleted".format(rowcount)
    else:
        return "arguments not correct",400

