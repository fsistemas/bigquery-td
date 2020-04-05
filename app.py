from google.cloud import bigquery

import datetime
from datetime import timedelta

from dotenv import load_dotenv

import os

from generate_data import generate_data
from extract_data import extract_data

client = bigquery.Client()

def save_data():
    filename = 'file.csv'
    dataset_id = 'MyDataset'
    table_id = 'table_test01_tmp'

    dataset_ref = client.dataset(dataset_id)
    table_ref = dataset_ref.table(table_id)

    job_config = bigquery.LoadJobConfig()
    job_config.source_format = bigquery.SourceFormat.CSV
    job_config.skip_leading_rows = 1
    job_config.autodetect = True

    #https://cloud.google.com/bigquery/docs/reference/rest/v2/Job#JobConfigurationLoad.FIELDS.write_disposition
    #Truncate before insert
    job_config.write_disposition = 'WRITE_TRUNCATE'

    with open(filename, "rb") as source_file:
        job = client.load_table_from_file(source_file, table_ref, job_config=job_config)

    job.result()  # Waits for table load to complete.

    print("Loaded {} rows into {}:{}.".format(job.output_rows, dataset_id, table_id))

def delete_old_data(date_from):
    # Perform a delete query.
    QUERY = """
    DELETE FROM `bigquerytest-273202.MyDataset.table_test01`
    WHERE CREATION_DATE >= @date_from
    """

    job_config = bigquery.QueryJobConfig(
        query_parameters=[
            bigquery.ScalarQueryParameter("date_from", "TIMESTAMP", date_from),
        ]
    )

    query_job = client.query(QUERY, job_config=job_config)  # API request
    rows = query_job.result()  # Waits for query to finish

    print("end delete rows")

def merge_data():
    # Perform a merge query.
    QUERY = """
    MERGE MyDataset.table_test01 test
    USING MyDataset.table_test01_tmp tmp
    ON test.ID = tmp.ID
    WHEN MATCHED THEN
        UPDATE SET NAME = tmp.name, CREATION_DATE = tmp.CREATION_DATE
    WHEN NOT MATCHED THEN
        INSERT ROW
    """

    query_job = client.query(QUERY)  # API request
    rows = query_job.result()  # Waits for query to finish

    print("end merged rows")

if __name__ == '__main__':
    load_dotenv()

    date_format = '%Y-%m-%d %H:%M:%S'

    current_date = datetime.datetime.today()

    date_from = (current_date + timedelta(minutes=-40)).strftime(date_format)

    conection_string = SECRET_KEY = os.getenv("CONECTION_STRING")

    generate_data(conection_string)
    quantity = extract_data(conection_string, date_from)
    if quantity > 0:
        delete_old_data(date_from)
        save_data()
        merge_data()
    else:
        print("No data to send")
