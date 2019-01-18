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
    host: (str) | redis_host
    password: (str) | redis_password
    port: (int) redis_port
```
To change the password for Redis
``` bash
$ redis-cli
127.0.0.1:6379> CONFIG SET requirepass "password"
...
127.0.0.1:6379> AUTH password

```
ctrl+d | exit command to quit redis


## DATABASE INTEGRATION
In the database object you will be presented with the database model or schema that you will create, for now there are two default tables, namely the table tb_userdata and tb_user, do not delete these two objects, then you can see how the database schema is created.  minimal example config database:
```
database:
  tables :
    table_name:
        field_name:
            type: (str) | see your data type database driver
            notNull: (boolean)
            primary: (boolean)
            unique: (boolean)
            foreignKey:
                reference: (table_name)
                field: (field_name)
                on_delete: (str) | see your database driver action
                on_update: (str) | see your database action
        config:
            returning:
                - field_name
                - field_name
```

if using cockroachdb driver example create your table:
```
database:
  tables :
    tb_userdata:
      id_userdata:
        type: serial
        notNull: True
        primaryKey: True
      first_name:
        type: varchar
        notNull: True
      last_name:
        type: varchar
        notNull: True
      location:
        type: varchar
      email:
        type: varchar
        unique: True

```

The database object will be processed sequentially, for example if the table to be created has a foreign key then you must create a reference table above that table, example:

```
database:
  tables :
    tb_userdata:
      id_userdata:
        type: serial
        notNull: True
        primaryKey: True
      first_name:
        type: varchar
        notNull: True
      last_name:
        type: varchar
        notNull: True
      location:
        type: varchar
      email:
        type: varchar
        unique: True

    tb_user:
      id_user:
        type: serial
        notNull: True
        primaryKey: True
      id_userdata:
        type: int
        notNull: True
        foreignKey:
          reference: tb_userdata
          field: id_userdata
          on_delete: cascade
          on_update: cascade
      username:
        type: varchar
        unique: True
      password:
        type: varchar
```

## ENDPOINT INTEGRATION
This object you will be presented by integrating all endpoint models or Application Programing Interfaces from your project, you also create models from your endpoint, endpoints consist of one main sub-function and several functions inside it.
rules for creating endpoints:

1. Create 1 main endpoint in one module file in which there are several functions.
2. Connect the main endpoint to 1 table in a database.
3. Specify the endpoint is connected with the credentials that have been made.
4. Some modules with the name insert, get, remove, and where will automatically generate the code

Following is the main example of making endpoints

```
endpoint:
  endpoint_name:
    auth: (boolean)
    function_name:
      fields:
        fields_function_name:
          name: (str)
          desc: (str)
          type: fields | tags
        fields_function_name_2:
          name: (str)
          desc: (str)
          type: fields | tags
      others:
        method_name:
          name: (str)
          desc: (str)
      moduls:
        moduls_name:
          action: (str)
          parameters:
            table : (table_name)
            fields: $fields

    function_name_2:
      fields:
        fields_function_name:
          name: (str)
          desc: (str)
          type: fields | tags
        fields_function_name_2:
          name: (str)
          desc: (str)
          type: fields | tags
      others:
        method_name:
          name: (str)
          desc: (str)
      moduls:
        moduls_name:
          action: (str)
          parameters:
            table : (table_name)
            fields: $fields
```

### Function
The function is an action that will be displayed in a raw REST that will be made each function will be connected to the module where these modules where you can place code that can be modified later

```
endpoint:
  endpoint_name:
    auth: (boolean)
    function_name:

      fields:
        fields_function_name:
          name: (str)
          desc: (str)
          type: fields | tags
        fields_function_name_2:
          name: (str)
          desc: (str)
          type: fields | tags
      
      others:
        method_name:
          name: (str)
          desc: (str)

      ## ATTENTION ##
      moduls:
        moduls_name:
          action: (str)
          parameters:
            table : (table_name)
            fields: $fields
      ## ATTENTION ##
```
- paramaters in each module consisting of actions and fields the action is the name of the function that will be generated in the python code later
- fields are parameters to get the data sent by REST

### Others
This is in develop see next time

### Moduls
Moduls is the interface to the action that will occur from the function

```
moduls:
  moduls_name:
    action: (str)
    parameters:
      table : (table_name)
      fields: $fields
```
- Use the same Moduls name at each endpoint, you can use different names of modules but do not use the same module name at the next endpoint
- fields are parameters to get the data sent by REST, if you need all fields in the function then write $ fields but if you only need fields specifically then write according to the name of the fields in the function, besides fields can be left blank include it

Endpoint Full Example And Full Case:
```
endpoint:
  point_test:
    auth: False
    insert:
      fields:
        nm_pointest:
          name: name search for domain
          desc: Domain Variabel To Search
          type: fields
        value_pointest:
          name: name search for domain
          desc: Domain Variabel To Search
          type: fields
      others:
        method:
          name: name search for domain
          desc: Domain Variabel To Search
      moduls:
        test:
          action: insert
          parameters:
            table : point_test
            fields: $fields
    remove:
      fields:
        id_pointest:
          name: ID search
          desc: Domain Variabel To Search
          type: tags
      others:
        method:
          name: methode name
          desc: Domain Variabel To Search
      moduls:
        test:
          action: remove
          parameters:
            table : point_test
            fields: $fields

    get:
      fields:
        id_pointest:
          name: ID search
          desc: Domain Variabel To Search
          type: tags
          default:
      others:
        method:
          name: methode name
          desc: Domain Variabel To Search
      moduls:
        test:
          action: get
          parameters:
            table : point_test

    where:
      fields:
        id_pointest:
          name: ID search
          desc: Domain Variabel To Search
          type: tags
          default:
      others:
        method:
          name: methode name
          desc: Domain Variabel To Search
      moduls:
        test:
          action: where
          parameters:
            table : point_test
            fields: $fields

  ocha:
    auth: True
    insert:
      fields:
        nm_pointest:
          name: name search for domain
          desc: Domain Variabel To Search
          type: fields
        value_pointest:
          name: name search for domain
          desc: Domain Variabel To Search
          type: fields
      others:
        method:
          name: name search for domain
          desc: Domain Variabel To Search
      moduls:
        ocha:
          action: insert
          parameters:
            table : tb_ocha
            fields: $fields
    remove:
      fields:
        id_pointest:
          name: ID search
          desc: Domain Variabel To Search
          type: tags
      others:
        method:
          name: methode name
          desc: Domain Variabel To Search
      moduls:
        ocha:
          action: remove
          parameters:
            table : tb_ocha
            fields: id_pointest
```


