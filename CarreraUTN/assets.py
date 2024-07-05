import pygame

def load_image(path:str, scale:tuple):
    try:
        image = pygame.image.load(path)
        image = pygame.transform.scale(image, scale)
        return image
    except pygame.error as e:
        print(f"Error al cargar la imagen {path}: {e}")
    
def load_image_conv_alpha(path:str, scale:tuple):
    try:
        image = pygame.image.load(path).convert_alpha()
        image = pygame.transform.scale(image, scale)
        return image
    except pygame.error as e:
        print(f"Error al cargar la imagen {path}: {e}")
    
