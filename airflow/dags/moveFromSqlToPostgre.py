import psycopg2
import pyodbc

postgres_connection = psycopg2.connect(
    user="postgres",
    password="pass",
    host="host.docker.internal",
    port="5432",
    database="YoutubeDb",
)


def create_tables():
    # Create a cursor
    cursor = postgres_connection.cursor()

    cursor.execute('DROP TABLE IF EXISTS Videos_Stats')
    cursor.execute('''
        CREATE TABLE Videos_Stats (
            Id SERIAL PRIMARY KEY,
            VideoTitle VARCHAR(255),
            VideoID VARCHAR(255),
            PublishedAt TIMESTAMP,
            VideoKeyword VARCHAR(255),
            VideoLikes DOUBLE PRECISION,
            VideoComments INTEGER,
            VideoViews BIGINT
        )
    ''')
    cursor.execute('DROP TABLE IF EXISTS Comments')
    cursor.execute('''
        CREATE TABLE Comments (
            Id SERIAL PRIMARY KEY,
            VideoID VARCHAR(255),
            CommentText TEXT,
            CommentLikes DOUBLE PRECISION,
            CommentSentiment DOUBLE PRECISION
        )
    ''')
    cursor.execute('DROP TABLE IF EXISTS Trending_Video')
    cursor.execute('''
        CREATE TABLE Trending_Video (
            Id SERIAL PRIMARY KEY,
            ChannelID VARCHAR(255),
            ChannelTitle VARCHAR(255),
            VideoID VARCHAR(255),
            PublishedAt TIMESTAMP,
            VideoTitle VARCHAR(255),
            VideoDescription TEXT,
            VideoCategoryID INTEGER,
            VideoCategoryLabel VARCHAR(255),
            VideoDuration VARCHAR(255),
            VideoDurationSec INTEGER,
            VideoDimension VARCHAR(255),
            VideoDefinition VARCHAR(255),
            VideoCaption BOOLEAN,
            VideoLicensedContent DOUBLE PRECISION,
            ViewCount INTEGER,
            LikeCount DOUBLE PRECISION,
            DislikeCount DOUBLE PRECISION,
            FavoriteCount INTEGER,
            CommentCount DOUBLE PRECISION
        )
    ''')

    cursor.execute('DROP TABLE IF EXISTS YouTube_Video')
    cursor.execute('''
        CREATE TABLE YouTube_Video (
            ID SERIAL PRIMARY KEY,
            VideoURL VARCHAR(255),
            VideoTitle VARCHAR(255),
            VideoCategory VARCHAR(255),
            VideoDescription TEXT
        )
    ''')

    # Commit the changes and close the cursor and connection
    postgres_connection.commit()



def move():
    server = 'DESKTOP-T260KV7'
    database = 'YoutubeDb'
    connection_string = f'DRIVER={{ODBC Driver 18 for SQL Server}}; SERVER={server}; DATABASE={database}; Trusted_Connection=yes; TrustServerCertificate=YES'
    mssql_connection = pyodbc.connect(connection_string)

    mssql_cursor = mssql_connection.cursor()
    postgres_cursor = postgres_connection.cursor()

    mssql_cursor.execute(
        'SELECT Id, VideoTitle, VideoID, PublishedAt, VideoKeyword, VideoLikes, VideoComments, VideoViews FROM Videos_Stats')
    videos_stats_data = mssql_cursor.fetchall()

    mssql_cursor.execute(
        'SELECT  Id, VideoID, CommentText, CommentLikes, CommentSentiment  FROM Comments')
    comments_data = mssql_cursor.fetchall()

    mssql_cursor.execute(
        'SELECT Id, ChannelID, ChannelTitle, VideoID, PublishedAt, VideoTitle, VideoDescription, VideoCategoryID, '
        'VideoCategoryLabel, VideoDuration, VideoDurationSec, VideoDimension,'
        'VideoDefinition, VideoCaption, VideoLicensedContent, ViewCount, LikeCount,'
        'DislikeCount, FavoriteCount, CommentCount FROM Trending_Video')
    trending_video_data = mssql_cursor.fetchall()

    mssql_cursor.execute(
        'SELECT ID, VideoURL, VideoTitle, VideoCategory, VideoDescription FROM YouTube_Video')
    youtube_video_data = mssql_cursor.fetchall()

    for row in videos_stats_data:
        postgres_cursor.execute(
            'INSERT INTO Videos_Stats (Id, VideoTitle, VideoID, PublishedAt, VideoKeyword, VideoLikes, VideoComments, VideoViews) VALUES (%s, %s, %s, %s, %s, %s, %s, %s)',
            row
        )

    for row in comments_data:
        postgres_cursor.execute(
            'INSERT INTO Comments (Id, VideoID, CommentText, CommentLikes, CommentSentiment) VALUES (%s, %s, %s, %s, %s)',
            row
        )

    for row in youtube_video_data:
        postgres_cursor.execute(
            'INSERT INTO YouTube_Video (ID, VideoURL, VideoTitle, VideoCategory, VideoDescription) VALUES (%s, %s, %s, %s, %s)',
            row
        )

    for row in trending_video_data:
        postgres_cursor.execute(
            'INSERT INTO Trending_Video ('
            'Id, ChannelID, ChannelTitle, VideoID, PublishedAt, VideoTitle, VideoDescription, VideoCategoryID, '
            'VideoCategoryLabel, VideoDuration, VideoDurationSec, VideoDimension,'
            'VideoDefinition, VideoCaption, VideoLicensedContent, ViewCount, LikeCount,'
            'DislikeCount, FavoriteCount, CommentCount) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)',
            row
        )


    postgres_connection.commit()

    mssql_cursor.close()
    mssql_connection.close()

    postgres_cursor.close()
    postgres_connection.close()
