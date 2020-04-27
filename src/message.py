# Class for Message
class Message:
    #__listMessage=[]
    #listMessage = []

    def __init__(self, application_id,session_id, message_id, participants, content):
      self.application_id = application_id
      self.session_id = session_id
      self.message_id = message_id
      self.participants = participants
      self.content = content

    @property
    def application_id(self):
        return self._application_id

    @application_id.setter
    def application_id(self, application_id):
        if not application_id: raise Exception("application_id cannot be empty")
        if not isinstance(application_id,int): raise Exception("application_id must be number")
        self._application_id = application_id

    @property
    def session_id(self):
        return self._session_id

    @session_id.setter
    def session_id(self, session_id):
        if not session_id: raise Exception("session_id cannot be empty")
        if not isinstance(session_id, str): raise Exception("session_id must be string")
        self._session_id = session_id

    @property
    def message_id(self):
        return self._message_id

    @message_id.setter
    def message_id(self, message_id):
        if not message_id: raise Exception("message_id cannot be empty")
        if not isinstance(message_id, str): raise Exception("message_id must be string")
        self._message_id = message_id

    @property
    def participants(self):
        return self._participants

    @participants.setter
    def participants(self, participants):
        if not participants: raise Exception("participants cannot be empty")
        if not isinstance(participants, list): raise Exception("participants must be list")
        self._participants = participants

    @property
    def content(self):
        return self._content

    @content.setter
    def content(self, content):
        if not content: raise Exception("content cannot be empty")
        if not isinstance(content, str): raise Exception("participants must be string")
        self._content = content

# if __name__ == '__main__':
#     message = Message(1, "aaa", "bbb", ['avi aviv', 'moshe cohen'], "whats up?")
#     Message.listMessage.append(message)
#     print(Message.listMessage[0].application_id)
