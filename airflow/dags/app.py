import extractingToSql
import moveFromSqlToPostgre
from readWithPands import get_dataframes, rename_dataframes


def data_transfer_workflow():
    # Get and rename dataframes
    df_list = get_dataframes()
    df_list = rename_dataframes(df_list)

    # Create tables in the source SQL database
    extractingToSql.create_tables()

    # Save dataframes to the source SQL database
    extractingToSql.save_all_to_sql(df_list)

    # Create tables in the destination PostgreSQL database
    moveFromSqlToPostgre.create_tables()

    # Move data from the source SQL database to the destination PostgreSQL database
    moveFromSqlToPostgre.move()


if __name__ == "__main__":
    data_transfer_workflow()
