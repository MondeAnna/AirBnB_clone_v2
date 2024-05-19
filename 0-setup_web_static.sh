#!/usr/bin/env bash
# prep web server

# directories
current="/data/web_static/current"
shared="/data/web_static/shared"
test="/data/web_static/releases/test"

# operational directories
mkdir -p "$shared"
mkdir -p "$test"

# operational symbolic link
ln -s "$test" "$current"

# template landing page
web_page="<h1 align=\"center\">Best School</h1>"
echo "$web_page" > "$test"/index.html

# change owner
chown -R ubuntu:ubuntu /data

# install and config nginx
apt update
apt -y install nginx

sed_pattern="server_name _;"
sed -i "/$sed_pattern/a \
location = /hbnb_static {\
\n\t\talias $current;\
\n\t}" /etc/nginx/sites-enabled/default

service nginx restart
