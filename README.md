# Purpose
This repo allows tutors to send exercises compiled through LaTeX to students via WhatsApp.
The connection to Whatsapp is operated through [Twilio API](https://www.twilio.com/docs/iam/test-credentials#maincontent), hence the need for a Twilio account and credentials.
Also, to hand the compiled images over to Twilio, they need to be uploaded to the web.
Currently, that is being done through AWS S3 storage, hence, AWS credentials are needed. They are retrieved through the environment variables `AWS_ACCESS_KEY_ID` and `AWS_SECRET_ACCESS_KEY`.

# How to Operate
1. Set up Twilio Account, Twilio Number to send via WhatsApp.
2. Set up AWS S3 credentials
3. Configure config in `/configs/` based on the template (`configs/template.yaml`). In part that means setting up exercises in `exercises/exercises_general.yaml`.
4. To then execute the pipeline call `main.py` using your .venv as the python source and passing the config as an argument. For example `.venv/bin/python main.py configs/valid/testing.yaml`.

<img width="559" alt="grafik" src="https://github.com/SebastianBehrens/mathchatbot/assets/51058351/c7d9c704-4c44-4dd3-92eb-ebc875bee135">

