#   List of gnomes

### Requirements for run:
*   Python interpreter
*   Django package
*   Django Rest Framework package
*   Django Filter


### Runserver

Go to project directory and type:

```
manage.py runserver 8000
```

### Admin user:

If you want to log in to administration panel go to:
```
http://localhost:8000/admin
```

#### Username: admin

#### Password: TA3u41pe

### CRUD

Authentication not required

#### Read

```
http://localhost:8000
```

Authentication required

#### Create

```
http://localhost:8000/create
```

#### Update

```
http://localhost:8000/<int:id>
```

#### Delete

```
http://localhost:8000/delete/<int:id>
```