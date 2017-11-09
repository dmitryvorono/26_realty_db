import os


basedir = os.path.abspath(os.path.dirname(__file__))
sqlalchemy_database_url = 'sqlite:///' + os.path.join(basedir, 'realty.db')
ads_per_page = 15
