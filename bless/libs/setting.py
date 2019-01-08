database_setting = {
    "driver": {
        "mysql": {
            "constructor": "__init__.py.mysql",
            "package": {
                "name": "pymysql",
                "tools": "pip"
            }
        },
        "cockroachdb": {
            "constructor": "__init__.py.cockroachdb",
            "package": {
                "name": "psycopg2",
                "tools": "pip"
            }
        },
        "mariadb": {
            "constructor": "__init__.py.mysql",
            "package": {
                "name": "pymysql",
                "tools": "pip"
            }
        },
        "postgresql": {
            "constructor": "__init__.py.mysql",
            "package": {
                "name": "psycopg2",
                "tools": "pip"
            }
        },
        "mongodb": {
            "constructor": "__init__.py.mongo",
            "package": {
                "name": "flaskmongoengine",
                "tools": "pip"
            }
        }
    }
}

framework_setting = {
    "flask": {
      "default": {
        "url": "https://",
        "package": {
          "name": "psycopg2",
          "tools": "pip"
        }
      },
      "mysql": {
        "url": "https://",
        "package": {
          "name": "pymysql",
          "tools": "pip"
        }
      },
      "mongodb": {
        "url": "https://",
        "package": {
          "name": "mongoengine",
          "tools": "pip"
        }
      }
    }
  }
