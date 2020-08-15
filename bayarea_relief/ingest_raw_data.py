import pandas as pd
from bayarea_relief import db
from sqlalchemy import null
from argparse import ArgumentParser
from datetime import datetime

from bayarea_relief.models import ReliefModel
from collections import namedtuple

Date = namedtuple("Date", "month, day, year")

csv_to_db_mapper = {
    "Name": "name",
    "San Francisco County": "sf_county",
    "Alameda County": "alameda_county",
    "San Mateo County": "san_mateo_county",
    "Contra Costa County": "contra_costa_county",
    "Santa Clara County": "santa_clara_county",
    "County": "county",
    "Category": "category",
    "Black Owned": "black_owned",
    "LGBTQ": "lgbtq",
    "Women": "women_owned",
    "Who Applies": "non_profit",
    "100 or fewer employees": "_100_or_fewer",
    "500 or fewer employees": "_500_or_fewer",
    "750 or fewer employees": "_750_or_fewer",
    "750 or more": "_750_more",
    "Type of Relief": "relief_type",
    "Award Type": "award_type",
    "Award Amount Specified": "award_amount_specified",
    "Max Award Amount": "max_award_amount",
    "Interest Rate Applicable": "interest_rate_applicable",
    "Interest rate": "interest_rate",
    "Type of Support": "support_type",
    "Public or Private": "sector_type",
    "Type Entity Offering Support": "supported_entity",
    "Name of Entity": "entity_name",
    "Is there a Deadline": "deadline_applicable",
    "Deadline": "deadline",
    "English": "english",
    "Spanish": "spanish",
    "Chinese": "chinese",
    "Website": "website_url",
    "Other Details": "description",
    "Date Added": "date_added"
}


def main():
    parser = ArgumentParser(description='Tool for uploading data to PostgreSQL')
    parser.add_argument('-c', '--csv', type=str, help='CSV path to data for ingestion',
                        required=True)
    args = parser.parse_args()
    csv_file = args.csv

    # connection = create_engine('postgresql://postgres:postgres@localhost:5000/bar')
    df = pd.read_csv(csv_file)
    df = df.iloc[:, :-4]
    df = df.rename(columns=csv_to_db_mapper)
    df.drop(df[df["name"].isna()].index, inplace=True)
    df["_id"] = df.index
    df["county"] = df["county"].apply(transform_entry)
    df["category"] = df["category"].apply(transform_entry)
    df["non_profit"] = df["non_profit"].apply(transform_entry)
    df["relief_type"] = df["relief_type"].apply(transform_entry)
    df["award_type"] = df["award_type"].apply(transform_entry)
    df["max_award_amount"] = df["max_award_amount"].astype(str).apply(transform_entry)
    df["interest_rate_applicable"] = df["interest_rate_applicable"].astype(str).apply(
        transform_entry)
    df["support_type"] = df["support_type"].apply(transform_entry)
    df["sector_type"] = df["sector_type"].apply(transform_entry)
    df["supported_entity"] = df["supported_entity"].apply(transform_entry)
    df["non_profit"] = df["non_profit"].replace('non_profit_only', 'non_profits_only')
    df['max_award_amount'] = df['max_award_amount'].replace('nan', null())
    df['deadline'] = df['deadline'].replace('nan', null())
    df = df.replace('nan', null())
    df = df.fillna(null())
    queries = ReliefModel.query.all()
    if queries:
        for q in queries:
            db.session.delete(q)
        db.session.commit()
    df.apply(upload, axis=1)


def transform_entry(entry):
    entry = entry.strip()
    for character in [" ", "-"]:
        entry = entry.replace(character, '_')
    for character in ["$", ","]:
        entry = entry.replace(character, '')
    return entry.lower()


def upload(row):
    row = populate_datetime(row, "deadline")
    row = populate_datetime(row, "date_added")
    relief = ReliefModel(**row.to_dict())
    db.session.add(relief)
    db.session.commit()


def populate_datetime(row, column):
    try:
        row[column] = row[column].replace('June', '6').replace(' ', '/')
        values = [int(i) for i in row[column].split('/')]
        if len(values) < 3:
            values.append(datetime.now().year)
        if values[-1] < 2000:
            values[-1] = values[-1] + 2000
        d = Date(*values)
    except Exception:
        return row
    else:
        row[column] = datetime(d.year, d.month, d.day)
    return row


if __name__ == '__main__':
    main()
