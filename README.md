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
