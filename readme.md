pip install --upgrade google-cloud-bigquery
pip install python-dotenv
pip install pandas

https://googleapis.dev/python/bigquery/latest/index.html
https://cloud.google.com/bigquery/docs/quickstarts/quickstart-client-libraries#client-libraries-install-python
https://cloud.google.com/bigquery/docs/loading-data-local
https://cloud.google.com/bigquery/docs/reference/standard-sql/dml-syntax

# Insert/Update by ID, Delete rows does not exist in source/N/A

```
MERGE MyDataset.table_test01 test
USING MyDataset.table_test01_tmp tmp
ON test.ID = tmp.ID
WHEN MATCHED THEN
    UPDATE SET NAME = tmp.name, CREATION_DATE = tmp.CREATION_DATE
WHEN NOT MATCHED THEN
  INSERT ROW
```

# Opcion 1

## Definir fecha desde cuando se va a reprocesar
## Extraer datos a CSV
## Borrar datos mas viejos que x fecha en tabla grande
## Insertar datos nuevos en tabla temporal(Trunca/Inserta)
## Merge de las dos tablas

# Opcion 2

## Definir fecha desde cuando se va a reprocesar
## Extraer datos a CSV
## Borrar datos mas viejos que x fecha en tabla grande
## Insertar datos nuevos en tabla grande, append
