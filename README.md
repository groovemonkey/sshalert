# The tutorialinux SSHAlert script

A simple script that sends a text message when someone logs in or becomes root.

## To install

virtualenv -p python3 venv
source venv/bin/activate
pip install -r requirements.txt


## To run

Pass your secrets in as env vars):

```
export NEXMO_KEY=yourkey
export NEXMO_SECRET=yoursecret
export TARGET_PHONE_NUMBER=yourphonenumber
export TARGET_PHONE_NUMBER=yournexmosourcenumber
```

