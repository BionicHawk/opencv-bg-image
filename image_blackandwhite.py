import cv2 as cv
from cv2.typing import MatLike

def write_csv(matLike: MatLike, filename: str):
    WIDTH = matLike.shape[1]
    HEIGHT = matLike.shape[0]

    csv_result = ""

    for row in range(HEIGHT):
        for col in range(WIDTH):
            if col == WIDTH - 1:
                csv_result += f"{matLike[row, col]}\n"
                break

            csv_result += f"{matLike[row, col]},"

    with open(filename, mode="w") as csv_file:
        csv_file.write(csv_result)

        
def resize_image(img: MatLike, percent: float) -> MatLike:
    WIDTH = int(img.shape[1] * percent)
    HEIGHT = int(img.shape[0] * percent)

    return cv.resize(img, (WIDTH, HEIGHT), interpolation=cv.INTER_NEAREST)


# Leyendo la imagen
img = cv.imread("mario.png")
# Escribiendo la imagen orginal en un archivo csv
write_csv(img, "matriz_original.csv")

# Mostrando la imagen original
cv.imshow("Mario original", resize_image(img, 10.0))

# Convirtiendo a imagen a escala de grises
img = cv.cvtColor(img, cv.COLOR_RGB2GRAY, dst=img)
# Escribiendo la imagen nueva a un archivo csv
write_csv(img, "matriz_bg.csv")

# Mostrando la imagen a escala de grises
cv.imshow("Mario escala de grises", resize_image(img, 10.0))

# Esperando una tecla para cerrar el programa
cv.waitKey(0)