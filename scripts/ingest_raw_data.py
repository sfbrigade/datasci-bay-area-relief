import pandas as pd
from pathlib import Path
from sqlalchemy import create_engine

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
    "Women": "women",
    "Who Applies": "who_applies",
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
    "Other Details": "description"
}


def main():
    connection = create_engine('postgresql://postgres:postgres@localhost:5000/bar')
    scripts_file = Path(Path(__file__).absolute().parent, "raw_data.csv")
    df = pd.read_csv(scripts_file)
    df = df.iloc[:, :-5]
    df = df.rename(columns=csv_to_db_mapper)
    df.drop(df[df["name"].isna()].index, inplace=True)
    df.to_sql('relief', connection, if_exists="replace")


if __name__ == '__main__':
    main()
