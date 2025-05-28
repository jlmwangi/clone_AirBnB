#!/usr/bin/env bash
# sets up web servers for deployment of web static

sudo apt update -y
sudo apt install -y nginx

sudo mkdir -p /data/web_static/releases/test/
sudo mkdir -p /data/web_static/shared/

echo "<html>
  <head>
  </head>
  <body>
    Hello HBNB!
  </body>
  </html>" | sudo tee /data/web_static/releases/test/index.html >/dev/null

sudo ln -sf /data/web_static/releases/test/ /data/web_static/current

sudo chown -R ubuntu:ubuntu /data/

sudo sed -i '/listen 80 default_server;/a \
	location /hbnb_static/ {\n\
	    alias /data/web_static/current/;\n\
	    index index.html;\n\
	}' /etc/nginx/sites-available/default

# sudo ln -s /etc/nginx/sites-available/default /etc/nginx/sites-enabled

sudo nginx -t

sudo service nginx reload
