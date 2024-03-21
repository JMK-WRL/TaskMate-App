import os

class Config:
    # SQLite database URI
    SQLALCHEMY_DATABASE_URI = 'sqlite:///{}'.format(os.path.join(os.getcwd(), 'my_database_name.db'))
