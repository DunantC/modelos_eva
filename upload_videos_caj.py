import boto3

# +
s3 = boto3.client('s3')

params = {
    "Bucket": "autonomousdriving-dataset",
    "Prefix": "cajamarca-videos/"
}

happy_objects = s3.list_objects_v2(**params)
videos = [obj.get("Key") for obj in happy_objects["Contents"] if obj.get("Key", "").endswith(".MP4")]
print(videos)
# -
for video in videos:
    video_name = video.split("/")[-1]
    #print(f"Descargando {video_name}")
    s3.download_file(Bucket="autonomousdriving-dataset", Key=video, Filename="Autonomousdriving-Dataset/Cajamarca/"+ video_name)
    #connection.commit()
    #cursor.close()
    print(f"{video} descargado y guardado en Oracle!")

# +
s3 = boto3.client('s3')

params = {
    "Bucket": "autonomousdriving-dataset",
    "Prefix": "Lima-videos/DASHCAM/01_09_23/"
}

happy_objects = s3.list_objects_v2(**params)
videos = [obj.get("Key") for obj in happy_objects["Contents"] if (obj.get("Key", "").endswith(".MP4") or obj.get("Key", "").endswith(".mp4"))]
#print(videos)
for video in videos:
    video_name = video.split("/")[-1]
    #print(f"Descargando {video_name}")
    s3.download_file(Bucket="autonomousdriving-dataset", Key=video, Filename="Autonomousdriving-Dataset/Lima/DASHCAM/"+ video_name)
    #connection.commit()
    #cursor.close()
    print(f"{video} en Oracle!")
print("FIN!")


# +
s3 = boto3.client('s3')

params = {
    "Bucket": "autonomousdriving-dataset",
    "Prefix": "Lima-videos/DASHCAM/01_10_23/"
}

happy_objects = s3.list_objects_v2(**params)
videos = [obj.get("Key") for obj in happy_objects["Contents"] if (obj.get("Key", "").endswith(".MP4") or obj.get("Key", "").endswith(".mp4"))]
#print(videos)
for video in videos:
    video_name = video.split("/")[-1]
    #print(f"Descargando {video_name}")
    s3.download_file(Bucket="autonomousdriving-dataset", Key=video, Filename="Autonomousdriving-Dataset/Lima/DASHCAM/"+ video_name)
    #connection.commit()
    #cursor.close()
    print(f"{video} en Oracle!")
print("FIN!")

# +
s3 = boto3.client('s3')

params = {
    "Bucket": "autonomousdriving-dataset",
    "Prefix": "Lima-videos/DASHCAM/12_01_23/"
}

happy_objects = s3.list_objects_v2(**params)
videos = [obj.get("Key") for obj in happy_objects["Contents"] if (obj.get("Key", "").endswith(".MP4") or obj.get("Key", "").endswith(".mp4"))]
#print(videos)
for video in videos:
    video_name = video.split("/")[-1]
    #print(f"Descargando {video_name}")
    s3.download_file(Bucket="autonomousdriving-dataset", Key=video, Filename="Autonomousdriving-Dataset/Lima/DASHCAM/"+ video_name)
    #connection.commit()
    #cursor.close()
    print(f"{video} en Oracle!")
print("FIN!")
# -


