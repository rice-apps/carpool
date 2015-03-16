from sqlalchemy import *
from migrate import *


from migrate.changeset import schema
pre_meta = MetaData()
post_meta = MetaData()
trip = Table('trip', pre_meta,
    Column('id', INTEGER, primary_key=True, nullable=False),
    Column('origin', VARCHAR(length=64)),
    Column('destination', VARCHAR(length=64)),
    Column('contact_info', VARCHAR(length=64)),
    Column('date', VARCHAR(length=6)),
    Column('TOD', VARCHAR(length=4)),
    Column('TOA', VARCHAR(length=4)),
)

post = Table('post', post_meta,
    Column('id', Integer, primary_key=True, nullable=False),
    Column('body', String(length=140)),
    Column('timestamp', DateTime),
    Column('user_id', Integer),
)

user = Table('user', post_meta,
    Column('id', Integer, primary_key=True, nullable=False),
    Column('nickname', String(length=64)),
    Column('email', String(length=120)),
)


def upgrade(migrate_engine):
    # Upgrade operations go here. Don't create your own engine; bind
    # migrate_engine to your metadata
    pre_meta.bind = migrate_engine
    post_meta.bind = migrate_engine
    pre_meta.tables['trip'].drop()
    post_meta.tables['post'].create()
    post_meta.tables['user'].create()


def downgrade(migrate_engine):
    # Operations to reverse the above upgrade go here.
    pre_meta.bind = migrate_engine
    post_meta.bind = migrate_engine
    pre_meta.tables['trip'].create()
    post_meta.tables['post'].drop()
    post_meta.tables['user'].drop()
