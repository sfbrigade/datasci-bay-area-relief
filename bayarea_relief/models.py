from enum import Enum

from bayarea_relief import db


class UniqueCountyEnum(Enum):
    yes = 'Yes'
    no = 'No'
    unknown = 'Unknown'


class CountyEnum(Enum):
    all = 'All'
    some = 'Some'
    unknown = 'Unknown'


class CategoryEnum(Enum):
    agriculture = 'Agriculture'
    all = 'All'
    unknown = 'Unknown'
    multiple = 'Multiple'
    healthcare = 'Healthcare'
    entertainment = 'Entertainment'
    hospitality = 'Hospitality'
    manufacturing = 'Manufacturing'
    education = 'Education'
    mass_media = 'Mass Media'
    software = 'Software'
    real_estate = 'Real Estate'
    sport = 'Sport'
    transport = 'Transport'
    financial = 'Financial Services'


class ReliefModel(db.Model):
    __tablename__ = 'relief'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String())
    sf_county = db.Column(db.Enum(UniqueCountyEnum))
    alameda_county = db.Column(db.Enum(UniqueCountyEnum))
    san_mateo_county = db.Column(db.Enum(UniqueCountyEnum))
    contra_costa_county = db.Column(db.Enum(UniqueCountyEnum))
    santa_clara_county = db.Column(db.Enum(UniqueCountyEnum))
    county = db.Column(db.Enum(CountyEnum))
    category = db.Column(db.Enum(CategoryEnum))

    def __init__(self, name, sf_county, alameda_county, san_mateo_county,
                 contra_costa_county, santa_clara_county,
                 county, category):
        self.name = name
        self.sf_county = sf_county
        self.alameda_county = alameda_county
        self.san_mateo_county = san_mateo_county
        self.contra_costa_county = contra_costa_county
        self.santa_clara_county = santa_clara_county
        self.county = county
        self.category = category

    def __repr__(self):
        return "f<Relief {self.name}>"
