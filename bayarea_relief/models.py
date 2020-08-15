from enum import Enum

from bayarea_relief import db


class BinaryWithUnknown(Enum):
    Yes = 'Yes'
    No = 'No'
    Unknown = 'Unknown'

    @classmethod
    def is_available(cls, response):
        return BinaryWithUnknown.yes.value == response

    def __str__(self):
        return self.value

class BinaryWithUnknownNA(Enum):
    Yes = 'Yes'
    No = 'No'
    Unknown = 'Unknown'
    NotApplicable = 'Not Applicable'

    @classmethod
    def is_available(cls, response):
        return BinaryWithUnknownNA.yes.value == response

    def __str__(self):
        return self.value


class Binary(Enum):
    Yes = 'Yes'
    No = 'No'

    def __str__(self):
        return self.value


class CountyEnum(Enum):
    all = 'All'
    some = 'Some'
    unknown = 'Unknown'

    def __str__(self):
        return self.value


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
    financial_services = 'Financial Services'

    def __str__(self):
        return self.value


class NonProfitEnum(Enum):
    all = 'All'
    unknown = 'Unknown'
    non_profits_only = "Non-Profits Only"
    businesses_only = "Businesses Only"
    individuals_only = "Individuals Only"

    def __str__(self):
        return self.value


class ReliefTypeEnum(Enum):
    covid = 'COVID'
    protest_damage = 'Protest Damage'
    both = "Both"

    def __str__(self):
        return self.value


class AwardTypeEnum(Enum):
    recurring = 'Recurring'
    one_time = 'Onetime'

    def __str__(self):
        return self.value


class InterestRateApplicableEnum(Enum):
    yes_and_reported = 'Yes and Reported'
    yes_but_not_reported = 'Yes but not Reported '
    no = 'No'
    unknown = "Unknown"

    def __str__(self):
        return self.value


class SupportTypeEnum(Enum):
    insurance = "Insurance"
    loan = "Loan"
    grant = "Grant"

    def __str__(self):
        return self.value


class SectorType(Enum):
    public = "Public"
    private = "Private"

    def __str__(self):
        return self.value


class SupportedEntity(Enum):
    government = "Government"
    non_profit = "Non Profit"
    gofund_me = "GoFund Me"
    private = "Private"

    def __str__(self):
        return self.value


# class Serializer(object):
#
#     def serialize(self):
#         return {c: getattr(self, c) for c in inspect(self).attrs.keys()}
#
#     @staticmethod
#     def serialize_list(l):
#         return [m.serialize() for m in l]


class ReliefModel(db.Model):
    __tablename__ = 'relief'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String())
    sf_county = db.Column(db.Enum(BinaryWithUnknown))
    alameda_county = db.Column(db.Enum(BinaryWithUnknown))
    san_mateo_county = db.Column(db.Enum(BinaryWithUnknown))
    contra_costa_county = db.Column(db.Enum(BinaryWithUnknown))
    santa_clara_county = db.Column(db.Enum(BinaryWithUnknown))
    county = db.Column(db.Enum(CountyEnum))
    category = db.Column(db.Enum(CategoryEnum))

    black_owned = db.Column(db.Enum(Binary))
    lgbtq = db.Column(db.Enum(Binary))
    women_owned = db.Column(db.Enum(Binary))
    non_profit = db.Column(db.Enum(NonProfitEnum))
    _100_or_fewer = db.Column(db.Enum(BinaryWithUnknownNA))
    _500_or_fewer = db.Column(db.Enum(BinaryWithUnknownNA))
    _750_or_fewer = db.Column(db.Enum(BinaryWithUnknownNA))
    _750_more = db.Column(db.Enum(BinaryWithUnknownNA))
    relief_type = db.Column(db.Enum(ReliefTypeEnum))
    award_type = db.Column(db.Enum(AwardTypeEnum))
    award_amount_specified = db.Column(db.Enum(Binary))
    max_award_amount = db.Column(db.Integer)
    interest_rate_applicable = db.Column(db.Enum(InterestRateApplicableEnum))
    interest_rate = db.Column(db.Float)

    support_type = db.Column(db.Enum(SupportTypeEnum))
    sector_type = db.Column(db.Enum(SectorType))
    supported_entity = db.Column(db.Enum(SupportedEntity))
    entity_name = db.Column(db.Text)
    deadline_applicable = db.Column(db.Enum(BinaryWithUnknown))
    deadline = db.Column(db.DateTime)
    website_url = db.Column(db.Text)
    description = db.Column(db.Text)
    date_added = db.Column(db.DateTime)

    english = db.Column(db.Enum(BinaryWithUnknown))
    chinese = db.Column(db.Enum(BinaryWithUnknown))
    spanish = db.Column(db.Enum(BinaryWithUnknown))

    def __init__(self, _id, name, sf_county, alameda_county, san_mateo_county,
                 contra_costa_county, santa_clara_county,
                 county, category, black_owned,
                 lgbtq, women_owned, non_profit, _100_or_fewer, _500_or_fewer,
                 _750_or_fewer, _750_more, relief_type,
                 award_type, award_amount_specified,
                 max_award_amount, interest_rate_applicable, interest_rate,
                 support_type, sector_type, supported_entity, entity_name,
                 deadline_applicable, deadline,
                 website_url, description,
                 date_added, english,
                 chinese, spanish, *args, **kwargs):
        self.id = _id
        self.name = name
        self.sf_county = sf_county
        self.alameda_county = alameda_county
        self.san_mateo_county = san_mateo_county
        self.contra_costa_county = contra_costa_county
        self.santa_clara_county = santa_clara_county
        self.county = county
        self.category = category
        self.black_owned = black_owned
        self.lgbtq = lgbtq
        self.women_owned = women_owned
        self.non_profit = non_profit
        self._100_or_fewer = _100_or_fewer
        self._500_or_fewer = _500_or_fewer
        self._750_or_fewer = _750_or_fewer
        self._750_more = _750_more
        self.relief_type = relief_type
        self.award_type = award_type
        self.award_amount_specified = award_amount_specified
        self.max_award_amount = max_award_amount
        self.interest_rate_applicable = interest_rate_applicable
        self.interest_rate = interest_rate
        self.support_type = support_type
        self.sector_type = sector_type
        self.supported_entity = supported_entity
        self.entity_name = entity_name
        self.deadline_applicable = deadline_applicable
        self.deadline = deadline
        self.website_url = website_url
        self.description = description
        self.date_added = date_added
        self.english = english
        self.chinese = chinese
        self.spanish = spanish

    def __getitem__(self, item):
        return getattr(self, item)

    @property
    def serialize(self):
        """Return object data in easily serializeable format"""
        serialized_obj = {}
        for column in self.__table__.columns:
            value = self[column.key]
            if isinstance(value, Enum):
                value = str(value)
            serialized_obj[column.key] = value
        return serialized_obj
