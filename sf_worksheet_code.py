# The Snowpark package is required for Python Worksheets.
# You can add more packages by selecting them using the Packages control and then importing them.

import snowflake.snowpark as snowpark
from snowflake.snowpark.functions import col, concat, lit, when


def clean_transactions_table_data(dataframe):
    # remove duplicates
    dataframe = dataframe.drop_duplicates()

    # collect rows where store name, client name and product name are null
    store_name_null_rows = dataframe.filter(
        col("Store_Name").isNull()).collect()
    client_name_null_rows = dataframe.filter(
        col("Client_Name").isNull()).collect()
    product_name_null_rows = dataframe.filter(
        col("Product_Name").isNull()).collect()

    for row in store_name_null_rows:
        store_id_to_fill = row["STORE_ID"]
        dataframe = dataframe.withColumn("Store_Name",
                                         when(col("Store_ID") == store_id_to_fill,
                                              concat(lit("Store_"), col("Store_ID"))).otherwise(col("Store_Name")))
    for row in client_name_null_rows:
        store_id_to_fill = row["CLIENT_ID"]
        dataframe = dataframe.withColumn("CLient_Name",
                                         when(col("Client_ID") == store_id_to_fill,
                                              concat(lit("Client_"), col("Client_ID"))).otherwise(col("CLient_Name")))
    for row in product_name_null_rows:
        store_id_to_fill = row["PRODUCT_ID"]
        dataframe = dataframe.withColumn("Product_Name",
                                         when(col("Product_ID") == store_id_to_fill,
                                              concat(lit("Product_"), col("Product_ID"))).otherwise(col("Product_Name")))
    return dataframe

# dimension tables


def create_client_table(dataframe):
    client_table = dataframe.select(
        "CLIENT_ID", "CLIENT_NAME", "CLIENT_LASTNAME", "EMAIL")
    return client_table


def create_store_table(dataframe):
    store_table = dataframe.select("STORE_ID", "STORE_NAME", "LOCATION")
    return store_table


def create_product_table(dataframe):
    product_table = dataframe.select(
        "PRODUCT_ID", "PRODUCT_NAME", "CATEGORY", "BRAND")
    return product_table


def create_address_table(dataframe):
    address_table = dataframe.select(
        "ADDRESS_ID", "STREET", "CITY", "STATE", "ZIP_CODE")
    return address_table

# fact table


def create_sales_table(dataframe):
    sales_table = dataframe.select("TRANSACTION_ID", "QUANTITY_OF_ITEMS_SOLD",
                                   "UNIT_PRICE", "DISCOUNT", "CLIENT_ID", "SORE_ID", "PRODUCT_ID", "ADDRESS_ID")
    return sales_table


def main(session: snowpark.Session):
    tableName = 'TRANSACTIONS'
    dataframe = session.table(tableName)

    cleaned_dataframe = clean_transactions_table_data(dataframe)

    client_table = create_client_table(cleaned_dataframe)
    store_table = create_store_table(cleaned_dataframe)
    product_table = create_product_table(cleaned_dataframe)
    address_table = create_address_table(cleaned_dataframe)
    sales_table = create_sales_table(cleaned_dataframe)
