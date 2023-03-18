import cv2

# Nombre del archivo de video y directorio de destino para las imágenes
video_file = 'Autonomousdriving-Dataset/Cajamarca2/2023_02_15_115538_06.mp4'
output_dir = 'Autonomousdriving-Dataset/Frames/Cajamarca/caj_'

# Abre el archivo de video
cap = cv2.VideoCapture(video_file)
cap

# Inicializa el contador de fotogramas
frame_count = 0

# Recorre cada fotograma del video
while cap.isOpened():
    # Lee el siguiente fotograma
    ret, frame = cap.read()

    # Si no hay más fotogramas, sal del bucle
    if not ret:
        break

    # Guarda el fotograma actual como una imagen en el directorio de salida
    filename = output_dir + f'frame_{frame_count:04d}.jpg'
    cv2.imwrite(filename, frame)

    # Incrementa el contador de fotogramas
    frame_count += 1

    # Muestra el progreso en la consola
    if frame_count % 100 == 0:
        print(f'Processed {frame_count} frames...')

# Cierra el archivo de video
cap.release()

# +
#contador de frames de video
video_file = 'Autonomousdriving-Dataset/Cajamarca2/2023_02_15_115538_06.mp4'

cap = cv2.VideoCapture(video_file)
total_frames = int(cap.get(cv2.CAP_PROP_FRAME_COUNT))

print("El video tiene", total_frames, "frames")
# -


