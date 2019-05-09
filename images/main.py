from PIL import Image
# ============== ABRIR UNA IMAGEN Y MOSTRARLA ==========
# try:
#     img = Image.open("images/imagen2.jpg")

#     img.show()
# except IOError:
#     print("No es posible abrir la imagen")

# ========== Modo de las imagenes =============
try:
    img = Image.open("images/imagen3.jpg")
    img.convert("L")  # cambiar el formato de una imagen
    img.rotate(-50)
    img.save("news/imagen2.jpg")
    img.show()
    # print(img.mode) #RGB
    # x y
    # print(img.getpixel((100,200))) # los pixele de colores en la poiciocn x y y
    # cambiar el modo de la imagen
    # img.convert("RGBA") # cambiar el formato de una imagen

    # img.save("news/imagen2.jpg")

except IOError:
    print("No es posible abrir la imagen")
