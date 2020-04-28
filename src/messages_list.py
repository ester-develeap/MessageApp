from src.message import Message


class MessageList:
    __listMessage=[]

    @staticmethod
    def add_new_message(message):
        try:
            app_id=message['application_id']
            session_id = message['session_id']
            message_id = message['message_id']
            participants=message['participants']
            content=message['content']
        except:
            raise Exception("data not correct")
        new_message=Message(app_id,session_id,message_id,participants,content)

        if any(elem.message_id == new_message.message_id for elem in MessageList.__listMessage):
            raise Exception("message_id is alredy exist")
        MessageList.__listMessage.append(new_message)

    @staticmethod
    def get_messages():
        return MessageList.__listMessage

    @staticmethod
    def delete_messages(applicationId,sessionId,messageId):
        if applicationId != None:
            MessageList.__listMessage = [element for element in MessageList.__listMessage if element.application_id != applicationId]
        if sessionId != None:
            MessageList.__listMessage = [element for element in MessageList.__listMessage if element.session_id != sessionId]
        if messageId != None:
            MessageList.__listMessage = [element for element in MessageList.__listMessage if element.message_id != messageId]

