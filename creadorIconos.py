#Es necesario tener instalada la libreria "Pillow": pip install Pillow



#Para no volver a escribir las rutas dejarlas aca y escribir el nombre del icono al final:

#Ruta de origen: 

#Ruta de destino: 
               

#Aclaración: es posible tener problemas al querer comentar usando """. Es por eso que los comentarios estan hechos con #. 


from PIL import Image
import os

def generar_imagenes(input_path, nombres_imagenes, output_dir):
    # Verificar si el archivo de entrada es una imagen .png
    if not input_path.lower().endswith(".png"):
        print("El archivo seleccionado no es una imagen .png :(")
        return

    # Abrir la imagen de entrada
    with Image.open(input_path) as img:
        # Crear el directorio de salida si no existe
        os.makedirs(output_dir, exist_ok=True)

        # Generar y guardar las imágenes con los nombres deseados
        for i, nombre in enumerate(nombres_imagenes, start=1):
            # Reemplazar espacios por guiones en el nombre
            nombre = nombre.replace(" ", "-")
            output_name = f"{nombre}.png"
            output_path = os.path.join(output_dir, output_name)
            img.save(output_path)
            print(f"Imagen generada: {output_path}")

if __name__ == "__main__":
    # Solicitar al usuario el archivo de entrada
    input_file = input('Ingrese la ruta y el archivo .png (agregar la terminación ".png" al final del nombre de la imagen): ')

    # Solicitar al usuario la lista de nombres de las imágenes
    nombres_input = input("Ingrese los nombres de los iconos usando dos espacios para separar un nombre de un icono del otro: ")
    nombres_imagenes = nombres_input.split("  ")

    # Solicitar al usuario la ruta de salida
    output_dir = input("Ingrese la ruta donde desea descargar los iconos (agregar una \ al final de la ruta): ")

    # Generar las imágenes
    generar_imagenes(input_file, nombres_imagenes, output_dir)
