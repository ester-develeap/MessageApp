# README

Flask message application

where you can send, get,  delete your messages and save into db

**Setup and run instructions:**

**1.** Download the project

        git clone https://github.com/EsterBenedikt/MessageApp.git 

**2.** Install the requirements

         pip install -r requirements.txt

**3.** Set database url in config file

      
        DATABASE ="put your path of the project here/MessageApp/data/message.db"
        
        example: "C:/Users/HP/Documents/esty/test/MessageApp/data/message.db"

**4**. Run the pytest command to run all the application's tests

        pytest

**5.** Run the application by

        python app.py

**REST API:**

**POST** Add new Message to your DB

       POST http://{host_ip}:{port}/AddMessage
        data = {
            "application_id": 1,
            "session_id": "aaaa",
            "message_id": "bbbb",
            "participants": ["avi aviv", "moshe cohen"],
            "content": "Hi, how are you today?"
        }

**GET** Get list messages, filter by applicationId/sessionId/messageId

      GET http://{host_ip}:{port}/GetMessage?applicationId=1
      GET http://{host_ip}:{port}/GetMessage?sessionId=aaaa
      GET http://{host_ip}:{port}/GetMessage?messageId=bbbb&applicationId=1

**DELETE** Delete messages by applicationId/sessionId/messageId
      
      DELETE http://{host_ip}:{port}/DeleteMessage?applicationId=1
      DELETE http://{host_ip}:{port}/DelteMessage?sessionId=aaaa
      DELETE http://{host_ip}:{port}/DeleteMessage?messageId=bbbb

