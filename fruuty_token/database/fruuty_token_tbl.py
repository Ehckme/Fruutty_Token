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

class Fruutty(Base):
    __tableName__ = 'fruuty_token'
    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    user_id: Mapped[str] = mapped_column(String(30))
    token_id: Mapped[str] = mapped_column(String(30))

    store_name : Mapped[str] = mapped_column(String(100))
    token_amount: Mapped[str] = mapped_column(String(30))
    country : Mapped[str] = mapped_column(String(30))
    trade_location : Mapped[str] = mapped_column(String(30))
    city : Mapped[str] = mapped_column(String(30))
    date : Mapped[datetime.datetime] = mapped_column(DateTime(
        timezone=True), nullable=False, server_default=func.now())
    processor : Mapped[str] = mapped_column(String(60))


    def __repr__(self) -> str:
        return f'Fruutty(id={self.id!r}, user_id={self.user_id!r}' \
               f'token_id={self.token_id!r}, token_amount={self.token_amount!r}' \
               f'country={self.country!r}, trade_location ={self.trade_location !r}),' \
               f'city={self.city!r}, date={self.date!r}'


class Fruutty(Base):
    __tableName__ = 'bank'
    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    user_id: Mapped[str] = mapped_column(String(30))
    bank_id: Mapped[str] = mapped_column(String(30))

    bank_name: Mapped[str] = mapped_column(String(30))
    branch: Mapped[str] = mapped_column(String(30))
    branch_code: Mapped[str] = mapped_column(String(30))

    def __repr__(self) -> str:
        return f'Fruutty(id={self.id!r}, user_id={self.user_id!r}' \
               f'bank_id={self.bank_id!r}, bank_name={self.bank_name!r}' \
               f'branch={self.branch!r}, branch_code={self.branch_code!r}),'




class Fruutty(Base):
    __tableName__ = 'orders'
    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    order_id: Mapped[str] = mapped_column(String(30))
    user_id: Mapped[str] = mapped_column(String(30))
    service_id: Mapped[str] = mapped_column(String(30))
    card_id: Mapped[str] = mapped_column(String(30))

    order: Mapped[str] = mapped_column(String(30))
    order_price: Mapped[str] = mapped_column(String(30))
    order_discount: Mapped[str] = mapped_column(String(30))
    order_vat: Mapped[str] = mapped_column(String(30))

    def __repr__(self) -> str:
        return f'Fruuttyt(id={self.id!r}, order_id={self.order_id!r}' \
               f'user_id={self.user_id!r}, order={self.order!r}' \
               f'order_price={self.order_price!r}, order_discount={self.order_discount!r},' \
               f'order_vat={self.order_vat!r},)'



connection_string = 'mysql+pymysql://root:root@localhost/Transact'
engine = create_engine(connection_string, echo=True)

Base.metadata.create_all(engine)

with Session(engine) as session:
    motchello  = Transact(
        username='motchello',
        email='motchello@gmail.com',
        password='1234',
        confirmed=True,


    )
    # Add
    session.add_all([motchello, lerato])
    session.commit()

    user = Token(
        id='motchello',
        user_id='motchello@gmail.com',
        token_id='1234',

    )
    # Add
    session.add_all([motchello, lerato])
    session.commit()






