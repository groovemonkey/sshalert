# The tutorialinux SSHAlert script

A simple script that sends a text message when someone logs in or becomes root.

## To run
```
virtualenv -p python3 venv
source venv/bin/activate
pip install -r requirements.txt
```

## To install

Use rsync to copy this project directory to your target server. Adjust file paths as necessary in sshalert.service.

Pass your secrets in as env vars, or use the secrets.env file in this repo (and referenced in the sshalert.service systemd unit file):

```
NEXMO_KEY=yourkey
NEXMO_SECRET=yoursecret
TARGET_PHONE_NUMBER=yourphonenumber
TARGET_PHONE_NUMBER=yournexmosourcenumber
```


## Naked Ubuntu 18.04 Server Setup
```
sudo apt-get update
sudo apt-get upgrade
sudo apt-get install virtualenv python3-virtualenv

# copy this repo over, adjust paths in sshalert.service
# copy sshalert.service to /etc/systemd/system/ into whichever target directory you want (probably multi-user)
systemctl daemon-reload
systemctl start sshalert
systemctl enable sshalert
```

TODO: add more instructions ;-)

