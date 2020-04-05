from sqlalchemy import create_engine
import pandas as pd
import sql2json

def extract_data(conection_string, date_from):
    print('date_from:', date_from)

    parameters = {
        'date_from': date_from
    }

    engine = create_engine(conection_string)
    raw_query_string = """
    SELECT
    t.ID,
    t.NAME,
    t.CREATION_DATE
    FROM test_table t
    WHERE t.CREATION_DATE >= :date_from
    """

    data = sql2json.sql2json.run_query(engine, raw_query_string, **parameters)

    df = pd.DataFrame(data)

    df.to_csv('file.csv', index=False)

    return len(data)

