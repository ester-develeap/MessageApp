# Class for Message
class Message:
  listMessage=[]

  def __init__(self, application_id,session_id, message_id, participants, content):
      self.application_id=application_id
      self.session_id=session_id
      self.message_id=message_id
      self.participants=participants
      self.content=content


if __name__ == '__main__':
    message = Message(1, "aaa", "bbb", ['avi aviv', 'moshe cohen'], "whats up?")
    Message.listMessage.append(message)
    print(Message.listMessage[0].application_id)
