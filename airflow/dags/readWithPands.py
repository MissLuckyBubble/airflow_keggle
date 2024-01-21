import pandas as pd


def get_dataframes():
    datasets = ['comments', 'Trending videos on youtube dataset', 'videos-stats', 'Youtube Video Dataset']
    path = 'C:/Users/MissLuckyBubble/Desktop/AI/python_direktoriq/csvs'
    df_comments = pd.read_csv(f'{path}/{datasets[0]}.csv').fillna('')
    df_trending_video = pd.read_csv(f'{path}/{datasets[1]}.csv').fillna('')
    df_videos_stats = pd.read_csv(f'{path}/{datasets[2]}.csv').fillna('')
    df_youtube_video = pd.read_csv(f'{path}/{datasets[3]}.csv').fillna('')

    return [df_comments, df_trending_video, df_videos_stats, df_youtube_video]


def rename_dataframes(dataframes):

    renames_videos_stats = {
        'Unnamed: 0': 'Id',
        'Title': 'VideoTitle',
        'Video ID': 'VideoID',
        'Published At': 'PublishedAt',
        'Keyword': 'VideoKeyword',
        'Likes': 'VideoLikes',
        'Comments': 'VideoComments',
        'Views': 'VideoViews'
    }

    renames_comments = {
        'Unnamed: 0': 'Id',
        'Video ID': 'VideoID',
        'Comment': 'CommentText',
        'Likes': 'CommentLikes',
        'Sentiment': 'CommentSentiment'
    }

    renames_trending_video = {
        'Unnamed: 0': 'Id',
        'channelId': 'ChannelID',
        'channelTitle': 'ChannelTitle',
        'videoId': 'VideoID',
        'publishedAt': 'PublishedAt',
        'videoTitle': 'VideoTitle',
        'videoDescription': 'VideoDescription',
        'videoCategoryId': 'VideoCategoryID',
        'videoCategoryLabel': 'VideoCategoryLabel',
        'duration': 'VideoDuration',
        'durationSec': 'VideoDurationSec',
        'dimension': 'VideoDimension',
        'definition': 'VideoDefinition',
        'caption': 'VideoCaption',
        'licensedContent': 'VideoLicensedContent',
        'viewCount': 'ViewCount',
        'likeCount': 'LikeCount',
        'dislikeCount': 'DislikeCount',
        'favoriteCount': 'FavoriteCount',
        'commentCount': 'CommentCount'
    }

    renames_youtube_video = {
        'Videourl': 'VideoURL',
        'Title': 'VideoTitle',
        'Category': 'VideoCategory',
        'Description': 'VideoDescription'
    }

    dataframes[0].rename(columns=renames_comments, inplace=True)
    dataframes[1].rename(columns=renames_trending_video, inplace=True)
    dataframes[2].rename(columns=renames_videos_stats, inplace=True)
    dataframes[3].rename(columns=renames_youtube_video, inplace=True)

    return dataframes
