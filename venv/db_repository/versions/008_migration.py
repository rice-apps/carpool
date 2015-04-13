from sqlalchemy import *
from migrate import *


from migrate.changeset import schema
pre_meta = MetaData()
post_meta = MetaData()
trip = Table('trip', post_meta,
    Column('id', Integer, primary_key=True, nullable=False),
    Column('origin', String(length=64)),
    Column('destination', String(length=64)),
    Column('contact_info', String(length=64)),
    Column('date', String(length=8)),
    Column('TOD', String(length=8)),
    Column('TOA', String(length=8)),
    Column('seats', String(length=8)),
)


def upgrade(migrate_engine):
    # Upgrade operations go here. Don't create your own engine; bind
    # migrate_engine to your metadata
    pre_meta.bind = migrate_engine
    post_meta.bind = migrate_engine
    post_meta.tables['trip'].columns['seats'].create()


def downgrade(migrate_engine):
    # Operations to reverse the above upgrade go here.
    pre_meta.bind = migrate_engine
    post_meta.bind = migrate_engine
    post_meta.tables['trip'].columns['seats'].drop()
