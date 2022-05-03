# Testing Bigquery API - ETL to extract data from mysql using sql2json and load that information to BigQuery

## Necessary dependencies
```
pip install --upgrade google-cloud-bigquery
pip install python-dotenv
pip install pandas
```

## Useful links
https://googleapis.dev/python/bigquery/latest/index.html
https://cloud.google.com/bigquery/docs/quickstarts/quickstart-client-libraries#client-libraries-install-python
https://cloud.google.com/bigquery/docs/loading-data-local
https://cloud.google.com/bigquery/docs/reference/standard-sql/dml-syntax

## Insert/Update by ID, Delete rows does not exist in source

```
MERGE MyDataset.table_test01 test
USING MyDataset.table_test01_tmp tmp
ON test.ID = tmp.ID
WHEN MATCHED THEN
    UPDATE SET NAME = tmp.name, CREATION_DATE = tmp.CREATION_DATE
WHEN NOT MATCHED THEN
  INSERT ROW
```
