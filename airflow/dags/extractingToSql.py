import pyodbc


def save_all_to_sql(df_list):
    table_names = ['Comments', 'Trending_Video', 'Videos_Stats', 'YouTube_Video']
    server = 'DESKTOP-T260KV7'
    database = 'YoutubeDb'
    connection_string = f'DRIVER={{ODBC Driver 18 for SQL Server}}; SERVER={server}; DATABASE={database}; Trusted_Connection=yes; TrustServerCertificate=YES'
    conn = pyodbc.connect(connection_string)
    cursor = conn.cursor()

    def insert_dataframe_to_sql(df, table_name):
        columns = ', '.join(df.columns)
        placeholders = ', '.join(['?' for _ in df.columns])
        sql_query = f"INSERT INTO {table_name} ({columns}) VALUES ({placeholders})"

        # Iterate over DataFrame rows and execute the query
        for row in df.itertuples(index=False):
            try:
                cursor.execute(sql_query, *row)
                conn.commit()
            except Exception as e:
                print(f"Error inserting into {table_name}: {e}")
                print(f"Problematic SQL query: {sql_query}")
                print(f"Problematic row data: {row}")
                conn.rollback()

    for df, table_name in zip(df_list, table_names):
        insert_dataframe_to_sql(df, table_name)

    conn.close()


def create_tables():
    server = 'DESKTOP-T260KV7'
    database = 'YoutubeDb'
    connection_string = f'DRIVER={{ODBC Driver 18 for SQL Server}}; SERVER={server}; DATABASE={database}; Trusted_Connection=yes; TrustServerCertificate=YES;'

    conn = pyodbc.connect(connection_string)
    cursor = conn.cursor()

    cursor.execute('DROP TABLE IF EXISTS Videos_Stats')
    cursor.execute('''
        CREATE TABLE Videos_Stats (
            Id INT PRIMARY KEY,
            VideoTitle VARCHAR(255),
            VideoID VARCHAR(255),
            PublishedAt DATETIME,
            VideoKeyword VARCHAR(255),
            VideoLikes FLOAT,
            VideoComments INT,
            VideoViews BIGINT
        )
    ''')

    cursor.execute('DROP TABLE IF EXISTS Comments')
    cursor.execute('''
        CREATE TABLE Comments (
            Id INT PRIMARY KEY,
            VideoID VARCHAR(255),
            CommentText TEXT,
            CommentLikes FLOAT,
            CommentSentiment FLOAT
        )
    ''')

    cursor.execute('DROP TABLE IF EXISTS Trending_Video')
    cursor.execute('''
        CREATE TABLE Trending_Video (
            Id INT PRIMARY KEY,
            ChannelID VARCHAR(255),
            ChannelTitle VARCHAR(255),
            VideoID VARCHAR(255),
            PublishedAt DATETIME,
            VideoTitle VARCHAR(255),
            VideoDescription TEXT,
            VideoCategoryID INT,
            VideoCategoryLabel VARCHAR(255),
            VideoDuration VARCHAR(255),
            VideoDurationSec INT,
            VideoDimension VARCHAR(255),
            VideoDefinition VARCHAR(255),
            VideoCaption BIT,
            VideoLicensedContent FLOAT,
            ViewCount INT,
            LikeCount FLOAT,
            DislikeCount FLOAT,
            FavoriteCount INT,
            CommentCount FLOAT
        )
    ''')

    cursor.execute('DROP TABLE IF EXISTS YouTube_Video')
    cursor.execute('''
        CREATE TABLE YouTube_Video (
            Id INT IDENTITY(1,1) PRIMARY KEY,
            VideoURL VARCHAR(255),
            VideoTitle VARCHAR(255),
            VideoCategory VARCHAR(255),
            VideoDescription TEXT
        )
    ''')

    conn.commit()
    conn.close()
