import boto3

# Create an S3 access object
s3 = boto3.client("s3")
s3.download_file(
    Bucket="autonomousdriving-dataset", Key="cusco-videos/Cusco_Dia2_Video_26.mp4", Filename="Autonomousdriving-Dataset/Cusco/Cusco_Dia2_Video_26.mp4"
)

# +
s3 = boto3.client('s3')

params = {
    "Bucket": "autonomousdriving-dataset",
    "Prefix": "cusco-videos/"
}

happy_objects = s3.list_objects_v2(**params)
videos = [obj.get("Key") for obj in happy_objects["Contents"] if obj.get("Key", "").endswith(".mp4")]
print(videos)

# +
s3 = boto3.client('s3')

params = {
    "Bucket": "autonomousdriving-dataset",
    "Prefix": "cusco-videos/"
}

happy_objects = s3.list_objects_v2(**params)
print(happy_objects)

# +
s3 = boto3.client('s3')

params = {
    "Bucket": "autonomousdriving-dataset",
    "Prefix": "cusco-videos/"
}

happy_objects = s3.list_objects_v2(**params)
videos = [obj.get("Key") for obj in happy_objects["Contents"] if obj.get("Key", "").endswith(".mp4")]
for video in videos:
    video_name = video.split("/")[-1]
    #print(f"Descargando {video_name}")
    s3.download_file(Bucket="autonomousdriving-dataset", Key=video, Filename="Autonomousdriving-Dataset/Cusco/"+ video_name)
    #connection.commit()
    #cursor.close()
    print(f"{video} descargado y guardado en Oracle!")
# -


