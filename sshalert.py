#!/usr/bin/env python

import logging
import os
from datetime import datetime
import nexmo

try:
    source_phone_number = os.getenv("SOURCE_PHONE_NUMBER")
    target_phone_number = os.getenv("TARGET_PHONE_NUMBER")
    nexmo_key = os.getenv("NEXMO_KEY")
    nexmo_secret = os.getenv("NEXMO_SECRET")
except:
    logging.critical("ERROR: Have you exported all required environment variables? (TARGET_PHONE_NUMBER, NEXMO_KEY, NEXMO_SECRET)")

# Initialize the nexmo client
client = nexmo.Client(key=nexmo_key, secret=nexmo_secret)

# Send a message
response = client.send_message({
    'from': source_phone_number,
    'to': target_phone_number,
    'text': 'Hello from sshalert',
})

if response['messages'][0]['status'] != '0':
    logging.error("ERROR: failed to send message: {0}".format(response['messages'][0]['error-text']))
else:
    logging.info("Successfully sent text message at {0}".format(datetime.utcnow()))
