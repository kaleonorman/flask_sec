### Start virtual environment
```source .env/bin/activate```

### Freeze iinstalled modules
- Run everytime you install a new module to keep up to date
```pip freeze > requirements.txt```

### Create flask run environment variable
``` export FLASK_APP=server.py```

### Turn flask debugger on
```export FLASK_DEBUG=1```

### Start flask server
```flask run```

### Init manage.py
```python manage.py db init```

### Migrate manage.py
```python manage.py db migrate```

### Upgrade manage.py
```python manage.py db upgrade```

##Python ripl
``` from app import db```
```>>> from app.models import User```
```>>> user = User(username='kaleo', email='k@gmail.com')```
```>>> user.set_password('pass')```
```>>> db.session.add(user)```
```>>> db.session.commit()```

```from app import db```
```from app.models import User```
```users = User.query.all()```
```for user in users: print(user.username)```
```for user in users: print(user.password_hash)```

```pip install flask-login```
``` pip freeze > requirements.txt```





##psql

```\c flask_sec```

### List Database
```\dt```

### Open Table
```\d user```