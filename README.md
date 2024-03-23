# Purpose
This repo allows tutors to send exercises compiled through LaTeX to students via WhatsApp.
The connection to Whatsapp is operated through [Twilio API](https://www.twilio.com/docs/iam/test-credentials#maincontent), hence the need for a Twilio account and credentials.
Also, to hand the compiled images over to Twilio, they need to be uploaded to the web.
Currently, that is being done through AWS S3 storage, hence, AWS credentials are needed. They are retrieved through the aws credentials file (`AWS_SHARED_CREDENTIALS_FILE`).

# How to Operate
1. Set up Twilio Account, Twilio Number to send via WhatsApp.
2. Set up AWS S3 credentials
3. Configure config in `/configs/` based on the template (`configs/template.yaml`). In part that means setting up exercises in `exercises/exercises_general.yaml`.
## Configure Exercises
