#!/usr/bin/env bash
# script that sets up your web servers for the deployment of web_static

# 1: install nginx if not installed
sudo apt-get update
sudo apt-get -y install nginx
sudo ufw allow 'Nginx HTTP'

# 2: create folder "shared" if it doesnt exist
sudo mkdir -p /data/web_static/shared/

# 3: create folder "test" if it doesnt exit
sudo mkdir -p /data/web_static/releases/test/

# 4: create fake html "index.html" with simple content
sudo touch /data/web_static/releases/test/index.html
sudo echo "<html>
  <head>
  </head>
  <body>
    Holberton School
  </body>
</html>" | sudo tee /data/web_static/releases/test/index.html

# 5: Create a symbolic link /data/web_static/current linked to the /data/web_static/releases/test/
sudo ln -sf /data/web_static/releases/test/ /data/web_static/current

# 6: Give ownership of the /data/ folder to the ubuntu user AND group
sudo chown -R ubuntu:ubuntu /data/

# 7: Update the Nginx configuration to serve the content of /data/web_static/current/ to hbnb_static
sudo sed -i '/listen 80 default_server/a location /hbnb_static { alias /data/web_static/current/;}' /etc/nginx/sites-enabled/default

sudo service nginx restart
