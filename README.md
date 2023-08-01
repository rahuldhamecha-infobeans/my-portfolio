# My Portfolio Site

#### Prerequisite & Installation Command:
```python
  Python : 3.10
  Django : 4.1
  Mysql  : 8.0
  bcrypt : 4.0.1
``` 
```bash
  sudo apt-get install python3.10
  pip install Django==4.1
  sudo apt-get install mysql-server
  pip install bcrypt
  pip install django[argon2]
```

#### Setup :
- Clone the project from the github by using this command
  ```bash
  git clone https://github.com/rahuldhamecha-infobeans/python-traning.git  
  ``` 
- Configure database with the project by creating `env.py` from `local.env.py` copying using below command 
  ```bash
  cp local.env.py env.py 
  ```
- Update below details in `env.py`
  ```python
  config = {
          'database': "MYSQL_DATABASE_NAME",
          'user': "MYSQL_USER_NAME",
          'password': "MYSQL_USER_PASSWORD",
          'host': "MY_SQL_HOST",
          'port': "MY_SQL_PORT",
          'allowed_host': ['DOMAIN_NAME1','DOMAIN_NAME2'] # Add Multiple Domain if required in array
      }
  ```