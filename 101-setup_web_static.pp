# Puppet script that sets up your web servers for the deployment of web_static

# Step 1: update installed packages
exec {'update':
  provider => shell,
  command  => 'sudo apt update',
  before   => Exec['upgrade'],
}

# Step 2: upgrade packages
exec {'upgrade':
  provider => shell,
  command  => 'sudo apt upgrade -y',
  before   => Exec['install Nginx'],
}

Step 3: install nginx
exec {'install Nginx':
  provider => shell,
  command  => 'sudo apt install nginx -y',
}

Step 4: create the web_static directories
exec {'create directories':
  provider => shell,
  command  => 'sudo mkdir -p /data/web_static/releases/test /data/web_static/shared',
  before   => Exec['info'],
}

# Step 5: create content of dummy index.html
exec {'info':
  provider => shell,
  command  => 'echo "Test World" | sudo tee /data/web_static/releases/test/index.html',
  before   => Exec['link'],
}

# Step 6: creating symbolic link
exec {'link':
  provider => shell,
  command  => 'sudo ln -sf /data/web_static/releases/test/ /data/web_static/current',
  before   => Exec['change ownership'],
}

Step 7: Change ownership "chown"
exec {'change ownership':
  provider => shell,
  command  => 'sudo chown -R ubuntu:ubuntu /data/',
  before   => Exec['put location'],
}

Step 8: put location and restart the nginx
exec {'put location':
  provider => shell,
  command  => "sudo sed -i '38i\\tlocation /hbnb_static/ {\n\t\talias /data/web_static/current/;\n\t}\n' /etc/nginx/sites-available/default",
  before   => Exec['restart Nginx'],
}

exec {'restart Nginx':
  provider => shell,
  command  => 'sudo service nginx restart',
  before   => File['/data/']
}

# check for file
file {'/data/':
  ensure  => directory,
  owner   => 'ubuntu',
  group   => 'ubuntu',
  recurse => true,
}
