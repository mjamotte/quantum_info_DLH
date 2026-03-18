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
python3 -m pip install qiskit[visualization] qiskit-ibm-runtime qiskit-aer numpy matplotlib ipykernel
python3 -m ipykernel install --user --name="kernel-dlh" --display-name="kernel-dlh"
```

Congrats, all is now setup properly!
