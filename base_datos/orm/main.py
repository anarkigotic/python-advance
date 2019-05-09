import peewee
import datetime
import config

database = peewee.MySQLDatabase(config.DATABASE['db'], host=config.DATABASE['host'], port=config.DATABASE['port'], user=config.DATABASE['user'], passwd=config.DATABASE['passwd'])

class User(peewee.Model):
    username = peewee.CharField(unique=True, max_length=50, index=True)
    password = peewee.CharField(max_length=50, null=True)
    email = peewee.CharField(max_length=50)
    active = peewee.BooleanField(default=True)
    created_date = peewee.DateTimeField(default=datetime.datetime.now)

    class Meta:
        database = database
        db_table = 'users'

if __name__ == '__main__':
    if(User.table_exists()):
        User.drop_table()
    User.create_table()
    

