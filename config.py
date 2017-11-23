import os


basedir = os.path.abspath(os.path.dirname(__file__))
SQLALCHEMY_DATABASE_URI = 'sqlite:///' + os.path.join(basedir, 'realty.db')
SQLALCHEMY_MIGRATE_REPO = os.path.join(basedir, 'db_repository')
ads_per_page = 15
site_ip_address = '0.0.0.0'
site_port = 8080
count_years_new_settlement = 3
