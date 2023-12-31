# Config function for mysql database.
def get_config():
    '''
    Return Database Credential Config.
    '''
    config = {
        'database': "MYSQL_DATABASE_NAME",
        'user': "MYSQL_USER_NAME",
        'password': "MYSQL_USER_PASSWORD",
        'host': "MY_SQL_HOST",
        'port': "MY_SQL_PORT",
        'allowed_host': ['DOMAIN_NAME1','DOMAIN_NAME2'], # Add Multiple Domain if required in array
        'debug': False,
        'email_host': 'SMTP_HOST',
        'email_ssl': 'SMTP_SSL_OR_TLS',
        'email_port': 'SMTP_SSL_TLS_PORT',
        'email_user': 'USER_EMAIL',
        'email_password': 'USER_PASSWORD'
    }
    return config