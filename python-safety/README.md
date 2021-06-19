## Installation

See https://medium.com/swlh/mini-project-deploying-python-application-with-nginx-30f9b25b195

```bash
apt install nginx
vi /etc/nginx/sites-enabled/default
# Change the default port

apt install python3-pip
pip3 install tensorflow pyyaml h5py virtualenv gunicorn flask
virtualenv iherb
source iherb/bin/activate
```

POST http://84.252.141.221:5000
{"features":[1, 0],"substances":[1, 1, 0]}
