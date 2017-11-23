# Real Estate Site

Real estate site is develop-verison site. Is's just include technological lauout for run on localhost

# How to install local

Python 3 should be already installed. Then use pip (or pip3 if there is a conflict with old Python 2 setup) to install dependencies:

```bash
$ pip install -r requirements.txt # alternatively try pip3
```
Remember, it is recommended to use [virtualenv/venv](https://devman.org/encyclopedia/pip/pip_virtualenv/) for better isolation.

Than you must create db and load data:

```bash
$ python db_create.py
$ python db_migrate.py
$ python db_load_ads.py [path_to_your_file_with_advertisement]
```

Next, run app:

```bash
$ python server.py
```

# Project Goals

The code is written for educational purposes. Training course for web-developers - [DEVMAN.org](https://devman.org)
