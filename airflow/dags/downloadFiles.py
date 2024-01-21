import kaggle

# Specify the directory where you want to download the dataset
download_dir = 'C:/Users/MissLuckyBubble/Desktop/AI/python_direktoriq/csvs'

# First Dataset
# Replace 'dataset-owner/dataset-name' with the actual owner and dataset name from the Kaggle URL
dataset_owner = 'advaypatil'
dataset_name = 'youtube-statistics'

# Use the Kaggle API to download the dataset
kaggle.api.dataset_download_files(f'{dataset_owner}/{dataset_name}', path=download_dir, unzip=True)

# Second
# Replace 'dataset-owner/dataset-name' with the actual owner and dataset name from the Kaggle URL
dataset_owner = 'anushabellam'
dataset_name = 'trending-videos-on-youtube'

# Use the Kaggle API to download the dataset
kaggle.api.dataset_download_files(f'{dataset_owner}/{dataset_name}', path=download_dir, unzip=True)

# Third
# Replace 'dataset-owner/dataset-name' with the actual owner and dataset name from the Kaggle URL
dataset_owner = 'rahulanand0070'
dataset_name = 'youtubevideodataset'

# Use the Kaggle API to download the dataset
kaggle.api.dataset_download_files(f'{dataset_owner}/{dataset_name}', path=download_dir, unzip=True)