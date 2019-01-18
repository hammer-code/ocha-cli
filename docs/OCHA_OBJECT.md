# OCHA OBJECT
Ocha Object is a configuration and (int)egration file in creating a REST project

## AUTH OBJECT
Auth Object is a configuration file for the security system that will be installed on your project, all about the credentials of the project will be created listed here, example:
``` 
auth:
  user: (str)
  password: (str)
  email: (str) | admin@admin.com
  admin: (str)
```
To activate the auth credentials, on each endpoint object in the endpoint configuration you are required to assign the True value to the auth object

## CONFIG OBJECT
This is the setup configuration of your project, example:

```
config:
  database:
    host: localhost
    port: 26257
    username: root
    name: bless_test01
    ssl: disable
    driver: cockroachdb
  app:
    host: 0.0.0.0
    name : bless_test01
    framework: flask
    port: 6969
    worker: 2
    environment: production
  redis:
    host: 127.0.0.1
    password: pass
    port: 6379
```
### Database
Default database configuration uses cockroachdb as the basis for using other databases, please replace the driver object
```
database:
    host: (str) | db_host
    port: (str) | db_port
    username: (str) | db_username
    name: (str) | db_name
    ssl: (boolean)
    driver: (str) | cockroachdb | mysql | postgreesql
```

### Application
```
app:
    host: (str)
    name : (str)
    framework: (str) | flask | django | nodejs | laravel
    port: (str)
    worker: (int)
    environment: (str) | production | development
```

### Redis
```
redis:
    host: (str)
    password: (str)
    port: (int)
```


