# Poor Man's Twitter using VUE and Django

### Technical Stacks
* **`Django 3.2`**
* **`DRF 3.10`**
* **`Vue2`**

### Configuring and Running Site on Local Machine

## Setting up for the backend in the backend directory 

#### Clone this repository
```
git clone https://github.com/Kolaposki/poor_mans_twitter.git
```


#### Create the virtual environment
```
python -m venv venv
```


#### Activate the virtual environment

*Windows:*
```
venv\Scripts\activate
```

*POSIX(macOS/Linux):*
```
source venv\bin\activate
```


#### Use the package manager [pip](https://pip.pypa.io/en/stable/) to install requirements.

```
pip install -r requirements.txt
```


#### Migrate the database
```
python manage.py makemigrations
python manage.py migrate
```

#### Run server
```
python manage.py runserver
```


The server will default on local environments to be running at [127.0.0.1:8000](127.0.0.1:8000)


## Setting up for the frontend

```
Open the index.html file in the frontend directory using your browser. 
```

