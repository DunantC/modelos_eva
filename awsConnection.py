import boto3

# +
#codigo para subir varios videos en un bucket en s3
s3 = boto3.client('s3')

params = {
    "Bucket": "autonomousdriving-dataset",
    "Prefix": "cusco-videos/"
}

happy_objects = s3.list_objects_v2(**params)
videos = [obj.get("Key") for obj in happy_objects["Contents"] if obj.get("Key", "").endswith(".mp4")]
for video in videos:
    video_name = video.split("/")[-1]
    s3.download_file(Bucket="autonomousdriving-dataset", Key=video, Filename="Autonomousdriving-Dataset/Cusco/"+ video_name)
    print(f"{video} descargado y guardado en Oracle!")
# -
#Codigo para subir zip o archivos uno por uno
#se cambia el Key y el Filename
s3 = boto3.client('s3')
s3.download_file(
    Bucket="ad-datasets", Key="KittyDataset.zip", Filename="Testing-Datasets/KittyDataset.zip"
)



