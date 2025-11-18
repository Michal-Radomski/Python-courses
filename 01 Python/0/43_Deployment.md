Deploying a Python app on an Ubuntu server is a common workflow that typically involves setting up the server, configuring a
Python environment, and choosing a production web server or gateway to serve your app. Here’s a concise, practical guide you
can follow.

Core approach

- Use a dedicated user for the app and keep code under a specific directory.
- Prefer a real web server gateway (like Gunicorn with Nginx or Apache with mod_wsgi) over running the app directly with
  Python in production.
- Use a virtual environment to isolate dependencies.
- Implement process management and automatic startup (systemd) and ensure firewall rules allow traffic on the chosen port
  (usually 80/443 for HTTP/HTTPS).
- Keep the system updated and monitor logs for issues.

Step-by-step setup (recommended pattern: Gunicorn + Nginx)

1. Prepare the server

- Update and upgrade:
  - sudo apt update
  - sudo apt upgrade -y
- Install essential packages:
  - sudo apt install -y software-properties-common curl

2. Create a dedicated app user and directory

- sudo useradd -m -d /home/myapp -s /bin/bash myapp
- sudo mkdir -p /home/myapp/app
- sudo chown -R myapp:myapp /home/myapp

3. Deploy your code

- Clone your repo or upload your code to /home/myapp/app
- Ensure a clean Python environment (Python 3.x is standard on recent Ubuntu releases)

4. Set up a Python virtual environment

- sudo apt install -y python3-venv python3-pip
- sudo -u myapp bash -c 'cd /home/myapp/app && python3 -m venv venv'
- sudo -u myapp bash -c 'source /home/myapp/app/venv/bin/activate && pip install -r requirements.txt'
  - If you have a Gunicorn requirement, it will be installed here.

5. Create a Gunicorn entry point

- In your app, ensure a WSGI callable exists, e.g., myapp.wsgi:app or yourapp:create_app()
- Start Gunicorn as a service (systemd) for reliability:

  - Create a systemd service file, e.g., /etc/systemd/system/myapp.service with content:

    - [Unit] Description=Gunicorn instance to serve myapp After=network.target

      [Service] User=myapp Group=www-data WorkingDirectory=/home/myapp/app Environment="PATH=/home/myapp/app/venv/bin"
      ExecStart=/home/myapp/app/venv/bin/gunicorn --workers 3 --bind unix:/home/myapp/app/myapp.sock myapp.wsgi:app

      [Install] WantedBy=multi-user.target

- Enable and start:
  - sudo systemctl daemon-reload
  - sudo systemctl enable --now myapp

6. Install and configure Nginx as a reverse proxy

- sudo apt install -y nginx
- Create an Nginx server block (e.g., /etc/nginx/sites-available/myapp):

  - server { listen 80; server_name your_server_domain_or_IP;

    location / { proxy_pass http://unix:/home/myapp/app/myapp.sock; proxy_set_header Host
    $host; proxy_set_header X-Real-IP
    $remote_addr; proxy_set_header X-Forwarded-For $proxy_add_x_forwarded_for;
    proxy_set_header X-Forwarded-Proto $scheme; } }

- Enable the site and test:
  - sudo ln -s /etc/nginx/sites-available/myapp /etc/nginx/sites-enabled/
  - sudo nginx -t
  - sudo systemctl reload nginx

7. Security and maintenance

- Configure a firewall (ufw):
  - sudo ufw allow 'Nginx Full'
  - sudo ufw enable
- Obtain TLS certificates (Let’s Encrypt) with Certbot:
  - sudo apt install -y certbot python3-certbot-nginx
  - sudo certbot --nginx -d your_domain
- Set up automatic renewal:
  - certbot renew --dry-run
- Regularly update the server and monitor logs:
  - sudo apt update && sudo apt upgrade -y
  - journalctl -u myapp -f
  - tail -f /var/log/nginx/access.log /var/log/nginx/error.log

Alternative patterns

- Flask/Django with Gunicorn + Nginx (similar steps; adjust Gunicorn command to your app entry point).
- Apache with mod_wsgi:
  - Install: sudo apt install apache2 libapache2-mod-wsgi-python3
  - Configure a VirtualHost with WSGIScriptAlias pointing to your app, and ensure the project is in a proper directory with a
    virtual environment.

Common pitfalls

- Not using a virtual environment can lead to dependency conflicts and system-wide changes.
- Running the app directly with python your_script.py in production is discouraged; use a WSGI server like Gunicorn.
- Misconfiguring file permissions can prevent the app from starting or reading resources.
- Failing to route TLS/HTTPS traffic properly can expose data; prefer automated TLS with Let’s Encrypt.

What you may need to customize

- Your app’s entry point (module and callable): e.g., myapp.wsgi:application or myapp:create_app()
- The number of Gunicorn workers (depends on CPU cores and concurrency needs)
- Domain name and TLS setup
- Paths to your project and virtual environment

If you share details like your Python framework (Flask, Django, FastAPI, etc.), your deployment method (Git, Docker, or
direct), and whether you want HTTP or HTTPS, a more tailored, step-by-step guide can be provided.

[1](https://www.phusionpassenger.com/library/walkthroughs/deploy/python/ownserver/apache/oss/bionic/deploy_app.html)
[2](https://www.phusionpassenger.com/library/walkthroughs/deploy/python/ownserver/apache/enterprise/xenial/deploy_app.html)
[3](https://truehost.com/support/knowledge-base/python-app-hosting-on-ubuntu-20-04/)
[4](https://blog.racknerd.com/how-to-deploy-a-python-app-on-an-ubuntu-server-vps-or-dedicated/)
[5](https://stackoverflow.com/questions/5281336/how-to-deploy-a-simple-python-application-in-linux-for-shared-company-environme)
[6](https://www.reddit.com/r/flask/comments/1iy6179/most_efficient_way_to_deploy_flask_app_on_ubuntu/)
[7](https://www.youtube.com/watch?v=KVFF-HTYbXM)
[8](https://docs.forestadmin.com/developer-guide-agents-python/deploying-to-production/environments/deploy-on-ubuntu)
[9](https://vexxhost.com/resources/tutorials/how-to-deploy-python-web-applications-with-the-bottle-micro-framework-on-ubuntu-16-04/)
[10](https://www.digitalocean.com/community/tutorials/how-to-set-up-ubuntu-cloud-servers-for-python-web-applications)
