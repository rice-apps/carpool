from sqlalchemy import *
from migrate import *


from migrate.changeset import schema
pre_meta = MetaData()
post_meta = MetaData()
post = Table('post', pre_meta,
    Column('id', INTEGER, primary_key=True, nullable=False),
    Column('body', VARCHAR(length=140)),
    Column('timestamp', DATETIME),
    Column('user_id', INTEGER),
)

user = Table('user', pre_meta,
    Column('id', INTEGER, primary_key=True, nullable=False),
    Column('nickname', VARCHAR(length=64)),
    Column('email', VARCHAR(length=120)),
)

trip = Table('trip', post_meta,
    Column('id', Integer, primary_key=True, nullable=False),
    Column('origin', String(length=64)),
    Column('destination', String(length=64)),
    Column('contact_info', String(length=64)),
    Column('date', String(length=6)),
    Column('TOD', String(length=4)),
    Column('TOA', String(length=4)),
)


def upgrade(migrate_engine):
    # Upgrade operations go here. Don't create your own engine; bind
    # migrate_engine to your metadata
    pre_meta.bind = migrate_engine
    post_meta.bind = migrate_engine
    pre_meta.tables['post'].drop()
    pre_meta.tables['user'].drop()
    post_meta.tables['trip'].create()


def downgrade(migrate_engine):
    # Operations to reverse the above upgrade go here.
    pre_meta.bind = migrate_engine
    post_meta.bind = migrate_engine
    pre_meta.tables['post'].create()
    pre_meta.tables['user'].create()
    post_meta.tables['trip'].drop()
