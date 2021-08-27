from sqlalchemy import create_engine, Column, String, Integer
import sqlalchemy as sql
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base

engine = create_engine('sqlite:///vendors.sqlite', echo=False)
Session = sessionmaker(bind=engine)
Base = declarative_base()


class Vendor(Base):
    __tablename__ = 'vendors'
    GST_HST_Number = Column(Integer(), primary_key=True)
    Vendor_Name = Column(String(60), nullable=False)
    Receipt_Format_1 = Column(String(20))
    Receipt_Format_2 = Column(String(20))
    Receipt_Format_3 = Column(String(20))
    Invoice_Format_1 = Column(String(20))
    Invoice_Format_2 = Column(String(20))
    Invoice_Format_3 = Column(String(20))


Base.metadata.create_all(engine)


def insert_entry(new_vendor):
    """
    In: class Vendor(Base) instance
    Adds vendor to database.
    """
    session = Session()

    session.add(new_vendor)
    session.commit()

    session.close()


def delete_entry(vendor_tax):
    """
    In: tax num
    Deletes vendor with given tax num from database.
    """
    session = Session()

    record = session.query(Vendor).filter(Vendor.GST_HST_Number == int(vendor_tax)).one()

    session.delete(record)
    session.commit()

    session.close()


def get_vendors():
    """
    Out: all str(Vendor.Vendor_Name).lower()
    """

    all_vendors = []

    connection = engine.connect()

    query = sql.select([Vendor])
    ResultProxy = connection.execute(query)
    ResultSet = ResultProxy.fetchall()

    for vendor in range(len(ResultSet)):
        all_vendors.append(ResultSet[vendor][1].lower())

    connection.close()

    return all_vendors


def vendor_exists(vendor_name):
    """
    In: str(vendor_name)
    Out: True (vendor_name IN database) or False (vendor_name NOT IN database)
    """

    connection = engine.connect()
    query = sql.select([Vendor]).where(Vendor.Vendor_Name == vendor_name)

    ResultProxy = connection.execute(query)
    ResultSet = ResultProxy.fetchall()

    connection.close()

    if ResultSet:
        return True
    else:
        return False


def search_vendors(vendor_name):
    """
    In: str: vendor_name
    Out: [(tax_num_1, vendor_name),(tax_num_2, vendor_name) ... ]
    """
    connection = engine.connect()

    query = sql.select([Vendor]).where(Vendor.Vendor_Name == vendor_name)

    ResultProxy = connection.execute(query)
    ResultSet = ResultProxy.fetchall()

    connection.close()

    return ResultSet


def search_vendors_by_tax(num):
    """
    In: int(9)
    Out: [(tax_num, vendor_name)]
    """
    connection = engine.connect()
    query = sql.select([Vendor]).where(Vendor.GST_HST_Number == num)
    ResultProxy = connection.execute(query)
    ResultSet = ResultProxy.fetchall()

    connection.close()

    return ResultSet
