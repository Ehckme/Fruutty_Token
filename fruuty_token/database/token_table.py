"""
The following below code is for connecting  to an existing
database and creating new table using SQLAlchemy 2.22 version
It inherits from sqlalchemy.orm DeclarativeBase

Please check for latest version updates and update when necessary!

"""

# import SQLAlchemy
from __future__ import annotations
import datetime
from sqlalchemy import DateTime
from sqlalchemy.sql import func
from typing import List
from sqlalchemy import ForeignKey, String, Integer, CHAR, Boolean, Column
from sqlalchemy.orm import DeclarativeBase
from sqlalchemy.orm import Mapped
from sqlalchemy.orm import relationship, mapped_column
from sqlalchemy import Table, create_engine
from sqlalchemy.orm import Session

# create an inheritance class from declarativeBase
class Base(DeclarativeBase):
    pass


# Create an association tabele for both tables to merge
# note for a Core table, we use the sqlalchemy.column construct
# not sqlalchemy.orm.mapped_column


class Token_vault(Base):
    __tablename__ = 'token_vault'

    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)

    token_id: Mapped[str] = mapped_column(String(30))
    initial_base_token: Mapped[str] = mapped_column((String(1000)))
    available_tokens: Mapped[str] = mapped_column((String(1000)))
    sold_tokens: Mapped[str] = mapped_column(String(30))
    opening_trade: Mapped[str] = mapped_column(String(30))
    closing_trade: Mapped[str] = mapped_column(String(30))
    date: Mapped[datetime.datetime] = mapped_column(DateTime(
        timezone=True), nullable=False, server_default=func.now())

    def __repr__(self) -> str:
        return f'Token_vault(id={self.id!r}, token_id={self.token_id!r}, ' \
               f'initial_base_token={self.initial_base_token}, available_tokens={self.available_tokens}, ' \
               f'sold_tokens={self.sold_tokens!r}, opening_trade={self.opening_trade!r}, ' \
               f'closing_trade={self.closing_trade!r}, date={self.date!r},'




# Create User a Table class
class Users(Base):
    __tablename__ = 'users'

    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    user_id: Mapped[str] = mapped_column(String(30))
    username: Mapped[str] = mapped_column(String(30))
    email: Mapped[str] = mapped_column(String(30))
    password: Mapped[str] = mapped_column(CHAR(200))
    confirmed: Mapped[bool] = mapped_column(nullable=False, default=False)
    otp: Mapped[int] = mapped_column(nullable=True)
    confirmed_at: Mapped[datetime.datetime] = mapped_column(DateTime(
        timezone=True), nullable=True, )
    signup_at: Mapped[datetime.datetime] = mapped_column(DateTime(
        timezone=True), nullable=False, server_default=func.now())
    lastLogin_at: Mapped[datetime.datetime] = mapped_column(DateTime(
        timezone=True), nullable=True, )
    lastLout_at: Mapped[datetime.datetime] = mapped_column(DateTime(
        timezone=True), nullable=True, )
    fruutty_token: Mapped[str] = mapped_column(nullable=True)

    def __repr__(self) -> str:
        return f'Users(id={self.id!r}, user_id={self.user_id!r}, username={self.username!r}, ' \
               f'email={self.email!r}, password={self.password!r}, ' \
               f'confirmed={self.confirmed!r}, otp={self.otp!r}, confirmed_at={self.confirmed_at!r},' \
               f'signup_at={self.signup_at!r}, lastlogin_at={self.lastLogin_at!r},' \
               f'lastLogout_at={self.lastLout_at!r}, fruutty_token={self.fruutty_token!r} '




class Fruutty_token(Base):
    __tablename__ = 'fruutty_token'
    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    user_id: Mapped[str] = mapped_column(String(30))
    token_id: Mapped[str] = mapped_column(String(30))
    token_type: Mapped[str] = mapped_column(String(30))

    store_name : Mapped[str] = mapped_column(String(100))
    token_amount: Mapped[str] = mapped_column(String(30))
    country : Mapped[str] = mapped_column(String(30))
    trade_location : Mapped[str] = mapped_column(String(30))
    city : Mapped[str] = mapped_column(String(30))
    date : Mapped[datetime.datetime] = mapped_column(DateTime(
        timezone=True), nullable=False, server_default=func.now())
    processor : Mapped[str] = mapped_column(String(60))


    def __repr__(self) -> str:
        return f'Fruutty_token(id={self.id!r}, user_id={self.user_id!r}' \
               f'token_id={self.token_id!r}, store_name={self.store_name!r},' \
               f' token_amount={self.token_amount!r}' \
               f'country={self.country!r}, trade_location ={self.trade_location !r}),' \
               f'city={self.city!r}, date={self.date!r}, processor={self.processor!r}'






class Fruutty_product(Base):
    __tableName__ = 'fruutty_product'
    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    user_id: Mapped[str] = mapped_column(String(30))
    token_id: Mapped[str] = mapped_column(String(30))
    token_type: Mapped[str] = mapped_column(String(30))


    product_name: Mapped[str] = mapped_column(String(30))
    product_price: Mapped[str] = mapped_column(String(30))

    def __repr__(self) -> str:
        return f'Fruutty_product(id={self.id!r}, user_id={self.user_id!r}' \
               f'token_id={self.token_id!r}, token_type={self.token_type!r}' \
               f'product_name={self.product_name!r}, product_price={self.product_price!r},'


class Fruutty_transactions(Base):
    __tablename__ = 'fruutty_transactions'

    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)

    token_id: Mapped[str] = mapped_column(String(30))
    initial_base_token: Mapped[str] = mapped_column((String(1000)))
    available_tokens: Mapped[str] = mapped_column((String(1000)))
    sold_tokens: Mapped[str] = mapped_column(String(30))
    opening_trade: Mapped[str] = mapped_column(String(30))
    closing_trade: Mapped[str] = mapped_column(String(30))
    date: Mapped[datetime.datetime] = mapped_column(DateTime(
        timezone=True), nullable=False, server_default=func.now())

    def __repr__(self) -> str:
        return f'Fruutty_transactions(id={self.id!r}, token_id={self.token_id!r}, ' \
               f'initial_base_token={self.initial_base_token}, available_tokens={self.available_tokens}, ' \
               f'sold_tokens={self.sold_tokens!r}, opening_trade={self.opening_trade!r}, ' \
               f'closing_trade={self.closing_trade!r}, date={self.date!r},'




connection_string = 'mysql+pymysql://root:root@localhost/Fruutty'
engine = create_engine(connection_string, echo=True)

Base.metadata.create_all(engine)

with Session(engine) as session:
    user_token = Fruutty_token(
        id='1',
        user_id='motchello@gmail.com',
        token_id='1234',
        store_name='Fruutty Store',
        token_amount='100000000',
        country='South Africa',
        trade_location='United States',
        city='New York',
        processor='fruutty',

    )

    user = Users(
        username='motchello',
        email='motchello@gmail.com',
        password='1234',
        confirmed=True,

    )
    # Add
    session.add_all([user_token, user])
    session.commit()






