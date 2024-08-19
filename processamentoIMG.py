from PIL import Image, ImageFilter


# Funções de utilidades para imagem
def load_image(path):
    """Carrega uma imagem de um caminho especificado."""
    return Image.open(path)


def save_image(image, path):
    """Salva a imagem em um caminho especificado."""
    image.save(path)


def show_image(image):
    """Exibe a imagem."""
    image.show()


# Filtros para imagem
def apply_grayscale(image):
    """Converte a imagem para escala de cinza."""
    return image.convert("L")


def apply_blur(image, radius=2):
    """Aplica um filtro de desfoque na imagem."""
    return image.filter(ImageFilter.GaussianBlur(radius))


# Transformações de imagem
def resize_image(image, size):
    """Redimensiona a imagem para o tamanho especificado."""
    return image.resize(size)


def rotate_image(image, angle):
    """Rotaciona a imagem pelo ângulo especificado."""
    return image.rotate(angle)


# Exemplo de uso do pacote
if __name__ == "__main__":
    # Carregar uma imagem
    image = load_image("caminho/para/sua/imagem.jpg")

    # Aplicar alguns filtros
    gray_image = apply_grayscale(image)
    blurred_image = apply_blur(image, radius=5)

    # Redimensionar e rotacionar
    resized_image = resize_image(image, (200, 200))
    rotated_image = rotate_image(image, 45)

    # Exibir e salvar os resultados
    show_image(gray_image)
    save_image(gray_image, "caminho/para/sua/imagem_gray.jpg")

    show_image(blurred_image)
    save_image(blurred_image, "caminho/para/sua/imagem_blurred.jpg")
