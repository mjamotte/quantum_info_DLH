## Admin: Create Azure VM

## Admin: Connect to the VM and setup jupyterhub

Log on the VM using:

ssh -i <your-key>.pem <your-vm-username>@<your-vm-ip>

Optionally, edit the ssh config file to add this connection.

Install jupyterhub using:

```
curl -L https://tljh.jupyter.org/bootstrap.py
sudo -E python3 - --admin <admin-user>
```

Add users in the admin dashboard at

```
http://4.231.59.231/hub/admin
```

You will be prompted for your username (what you chose for <admin-user>) and a password.
Your password will be created at this first login (remember it!)

## User: Connect to the jupyterhub

Open web browser and connect to the jupyterhub server at

```
http://4.231.59.231
```

Then enter your username and the password you want to use. Note that:

- The user (username) must have been created beforehand
- The password is created at the first login (remember it!)

You will arrive in your jupyterlab environment.

## User: Local python venv after git clone

In the jupyterlab home page, select terminal and setup your python environment using the following commands:

```
git clone https://github.com/mjamotte/quantum_info_DLH
cd quantum_info_DLH
python3 -m venv .venv
./.venv/bin/pip install -r requirements.txt
./.venv/bin/python -m ipykernel install --user --name="kernel-dlh"
```

Congrats, all is now setup properly!
