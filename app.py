import pandas as pd
from sqlalchemy import create_engine
from os import getenv


ac_year_data = "academic_years.ods"
engine = create_engine(getenv("DATABASE_URL"), echo=False)
schema = ""

# with open('schema.sql') as file:
#     schema = file.read()


df = pd.read_excel(ac_year_data)
df.to_sql(name='academic_years', con=engine)

dt = df.dtypes

print(dt)
print(df)