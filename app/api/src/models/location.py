from api.src.db import db
import api.src.models as models
class Location:
    __table__='locations'
    columns = ['id','borough','latitude','longitude','setting','precinct']

    def __init__(self, **kwargs):
        for key in kwargs.keys():
            if key not in self.columns:
                raise ValueError(f'{key} not in columns: {self.columns}')
        for k, v in kwargs.items():
            setattr(self, k, v)

    @classmethod
    def find_by_id(self, id, cursor): 
        location_query = """SELECT * FROM locations WHERE id = %s"""
        cursor.execute(location_query, (id,))
        record =  cursor.fetchone()
        return db.build_from_record(Location, record)
# >>> location = Location.find_by_id('5',cursor)
# >>> location.__dict__
# {'id': 5, 'borough': 'MANHATTAN', 'latitude': Decimal('40.75469651000003'), 'longitude': Decimal('-73.99535613299997'), 'setting': 'STREET', 'precinct': 14}

    @classmethod
    def lat_long(self, latitude, longitude, cursor):
        query_str = f"SELECT * FROM locations WHERE (latitude, longitude) = ({latitude},{longitude})"
        cursor.execute(query_str)
        records = cursor.fetchall()
        return db.build_from_records(Location, records)
       