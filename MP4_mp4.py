# +
import os
import subprocess

input_folder = 'Autonomousdriving-Dataset/Lima/DASHCAM'
output_folder = 'Autonomousdriving-Dataset/Lima/DASHCAM2'



# +
# Asegurarse de que la carpeta de salida exista
if not os.path.exists(output_folder):
    os.makedirs(output_folder)

# Iterar sobre los archivos en la carpeta de entrada
for filename in os.listdir(input_folder):
    if filename.endswith('.MP4'):
        # Construir las rutas de entrada y salida
        input_file = os.path.join(input_folder, filename)
        output_file = os.path.join(output_folder, filename[:-4] + '.mp4')

        # Ejecutar el comando ffmpeg para convertir el archivo
        cmd = ['ffmpeg', '-i', input_file, '-c', 'copy', output_file]
        subprocess.run(cmd, check=True)
# -


