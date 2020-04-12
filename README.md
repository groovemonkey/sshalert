# The tutorialinux SSHAlert script

A simple script that sends a text message when someone logs in or becomes root.

## To install

virtualenv -p python3 venv
source venv/bin/activate
pip install -r requirements.txt


## To run

Pass your secrets in as env vars):

```
NEXMO_KEY=yourkey
NEXMO_SECRET=yoursecret
TARGET_PHONE_NUMBER=yourphonenumber
TARGET_PHONE_NUMBER=yournexmosourcenumber
```



## Naked Ubuntu 18.04 Server Setup
sudo apt-get update
sudo apt-get upgrade
sudo apt-get install virtualenv python3-virtualenv
