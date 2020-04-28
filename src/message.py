# Class for Message
class Message:
    listMessage=[]
    #listMessage = []

    def __init__(self, application_id,session_id, message_id, participants, content):
      self.application_id = application_id
      self.session_id = session_id
      self.message_id = message_id
      self.participants = participants
      self.content = content

    @property
    def application_id(self):
        return self.__application_id

    @application_id.setter
    def application_id(self, application_id):
        if not application_id: raise Exception("application_id cannot be empty")
        if not isinstance(application_id,int): raise Exception("application_id must be number")
        self.__application_id = application_id

    @property
    def session_id(self):
        return self.__session_id

    @session_id.setter
    def session_id(self, session_id):
        if not session_id: raise Exception("session_id cannot be empty")
        if not isinstance(session_id, str): raise Exception("session_id must be string")
        self.__session_id = session_id

    @property
    def message_id(self):
        return self.__message_id

    @message_id.setter
    def message_id(self, message_id):
        if not message_id: raise Exception("message_id cannot be empty")
        if not isinstance(message_id, str): raise Exception("message_id must be string")
        self.__message_id = message_id

    @property
    def participants(self):
        return self.__participants

    @participants.setter
    def participants(self, participants):
        if not participants: raise Exception("participants cannot be empty")
        if not isinstance(participants, list): raise Exception("participants must be list")
        self.__participants = participants

    @property
    def content(self):
        return self.__content

    @content.setter
    def content(self, content):
        if not content: raise Exception("content cannot be empty")
        if not isinstance(content, str): raise Exception("participants must be string")
        self.__content = content

    def dump(self):
        return {   'application_id': self.__application_id,
                   'session_id': self.__session_id,
                   'message_id': self.__message_id,
                   'participants': self.__participants,
                   'content': self.__content }

