import pygame
import os
import json
from constantes import *
from biblioteca import *
from assets import *
from datos import lista
# Cambiar el directorio de trabajo al directorio del script
os.chdir(os.path.dirname(os.path.abspath(__file__)))

#------------------------------------------------------------------------------------------
pregunta = ""
respuesta_1 = ""
respuesta_2 = ""
respuesta_3 = ""
lista_preguntas = []
lista_a = []
lista_b = []
lista_c = []
lista_correcta = []
lista_jugadores = []
contador = 0

for e_lista in lista:
    lista_preguntas.append(e_lista["pregunta"])

'''Me guardo en 3 listas distintas las respuesta'''
for e_res_a in lista:
    lista_a.append(e_res_a["a"])
for e_res_b in lista:
    lista_b.append(e_res_b["b"])
for e_res_c in lista:
    lista_c.append(e_res_c["c"])

for e_res_correcta in lista:
    lista_correcta.append(e_res_correcta["correcta"])

#------------------------------------------------------------------------------------------

#iniciamos el juego
pygame.init()

#crear la pantalla 
pantalla = pygame.display.set_mode((ANCHO_VENTANA, ALTO_VENTANA))
#titulo de la ventana
pygame.display.set_caption("¨Carrera UTN")

#imagenes
imagen_logo = load_image("assets/images/carrera-de-mente.png", (230,200))
imagen_utn = load_image("assets/images/logo-utn.png", (150,50))
imagen_flecha = load_image_conv_alpha("assets/images/flecha.png", (90,50))
imagen_flecha_2 = load_image_conv_alpha("assets/images/flecha-2.png", (50,150))
imagen_personaje = load_image_conv_alpha("assets/images/luigi.png", (50,100))

#Rect() del personaje
rect_personaje = imagen_personaje.get_rect()
rect_personaje.x = 664
rect_personaje.y = 120
#Rect() de las casillas superiores
rect_casilla_salida = pygame.Rect(90,300,80,50)
rect_casilla_1 = pygame.Rect(190,300,80,50)
rect_casilla_2 = pygame.Rect(280,300,80,50)
rect_casilla_3 = pygame.Rect(370,300,80,50)
rect_casilla_4 = pygame.Rect(460,300,80,50)
rect_casilla_5 = pygame.Rect(550,300,80,50)
rect_casilla_avanzar = pygame.Rect(640,300,80,50)
rect_casilla_7 = pygame.Rect(730,300,80,50)
rect_casilla_8 = pygame.Rect(820,300,80,50)
#Rect() de las casillas inferiores
rect_casilla_9 = pygame.Rect(820,450,80,50)
rect_casilla_10 = pygame.Rect(730,450,80,50)
rect_casilla_11 = pygame.Rect(640,450,80,50)
rect_casilla_12 = pygame.Rect(550,450,80,50)
rect_casilla_retroceder = pygame.Rect(460,450,80,50)
rect_casilla_14 = pygame.Rect(370,450,80,50)
rect_casilla_15 = pygame.Rect(280,450,80,50)
rect_casilla_16 = pygame.Rect(190,450,80,50)
rect_casilla_llegada = pygame.Rect(20,450,80,50)
#lista de casillas
lista_casillas = [
    rect_casilla_salida, rect_casilla_1, rect_casilla_2, rect_casilla_3, rect_casilla_4,
    rect_casilla_5, rect_casilla_avanzar, rect_casilla_7, rect_casilla_8,
    rect_casilla_9, rect_casilla_10, rect_casilla_11, rect_casilla_12,
    rect_casilla_retroceder, rect_casilla_14, rect_casilla_15, rect_casilla_16, rect_casilla_llegada
]
#Rect() de los botones comenzar y terminar 
rect_comenzar = pygame.Rect(225,550,200,100)
rect_terminar = pygame.Rect(575,550,200,100)
#Rect() de las respuestas
rect_a = pygame.Rect(310, 100,300,20)
rect_b = pygame.Rect(310, 140,300,20)
rect_c = pygame.Rect(310, 180,300,20)

#PARTE DE ESCRIBIR Y GUARDAR EL NOMBRE
nombre = ""
rect_nombre = pygame.Rect(850, 500, 200, 25)
rect_nombre_escrito = pygame.Rect(850, 500, 200, 25)
rect_listo = pygame.Rect(850, 550, 65, 30)

#Fuentes
fuente = pygame.font.SysFont("Arial", 45)
fuente_2 = pygame.font.SysFont("Calibri", 17)
fuente_3 = pygame.font.SysFont("Calibri", 25)
fuente_4 = pygame.font.SysFont("Calibri", 40)
fuente_5 = pygame.font.SysFont("Arial", 18)
#Textos juego
txt_tiempo = fuente.render("Tiempo:", True, COLOR_LETRAS_GRIS)
txt_puntaje = fuente.render("Puntaje:", True, COLOR_LETRAS_GRIS)
txt_avanza = fuente_2.render("Avanza", True, COLOR_NEGRO)
txt_retrocede = fuente_2.render("Retrocede", True, COLOR_NEGRO)
txt_1 = fuente_2.render("1", True, COLOR_NEGRO)
txt_salida = fuente_3.render("Salida", True, COLOR_NEGRO)
txt_llegada = fuente_3.render("Llegada", True, COLOR_NEGRO)
txt_comenzar = fuente_4.render("Comenzar", True, COLOR_LETRAS_GRIS_OSCURO)
txt_terminar = fuente_4.render("Terminar", True, COLOR_LETRAS_GRIS_OSCURO)
#Texto juego terminado
txt_puntaje_tabla = fuente.render("Puntajes", True, COLOR_LETRAS_GRIS)

#Timer 1 segundo
timer_segundos = pygame.USEREVENT
pygame.time.set_timer(timer_segundos, 1000) #1000 es 1 segundo
segundos = "5"
flag_tiempo = False
activar_timer = False

#Puntaje
puntaje = 0
contador_casilla = 0

flag_nombre = False
flag_actualizar_datos = False

flag_acc_avanzar = False
flag_acc_retroceder = False
flag_correcta = False
flag_incorrecta = False
flag_comenzar = False
flag_terminar = False 
flag_luigi = False 
flag_correr = True

# Nombre del archivo JSON
archivo_json = 'datos.json'

# Verificar si el archivo JSON existe
if os.path.exists(archivo_json):
    # Cargar datos existentes si el archivo ya existe
    with open(archivo_json, 'r') as archivo:
        lista_jugadores = json.load(archivo)

while flag_correr:
    lista_eventos = pygame.event.get()
    for evento in lista_eventos:
        #si el evento es salir, cierra la ventana
        if evento.type == pygame.QUIT:
            flag_correr = False
        if evento.type == pygame.MOUSEBUTTONDOWN:
            posicion_click = list(evento.pos)
            print(f"Clic en las coordenadas: {posicion_click}")
            if rect_comenzar.collidepoint(evento.pos):
                flag_comenzar = True
                flag_luigi = True
                activar_timer = True
            if rect_terminar.collidepoint(evento.pos):
                flag_terminar = True

            if rect_a.collidepoint(evento.pos):
                if lista_correcta[contador] == "a":
                    flag_correcta = True
                else:
                    flag_incorrecta = True
            elif rect_b.collidepoint(evento.pos):
                if lista_correcta[contador] == "b":
                    flag_correcta = True
                else:
                    flag_incorrecta = True
            elif rect_c.collidepoint(evento.pos):
                if lista_correcta[contador] == "c":
                    flag_correcta = True
                else:
                    flag_incorrecta = True

            if rect_nombre.collidepoint(evento.pos):
                flag_nombre = True
            else:
                flag_nombre = False
            
            if rect_listo.collidepoint(evento.pos):
                flag_actualizar_datos = True

        if evento.type == pygame.KEYDOWN and flag_nombre:
            if evento.key == pygame.K_BACKSPACE:
                nombre = nombre[0:-1]
            else:
                nombre += evento.unicode
                print(nombre)
        
        if activar_timer == True:
            if evento.type == pygame.USEREVENT:
                if evento.type == timer_segundos:
                    if flag_tiempo == False:
                        segundos = int(segundos) - 1
                        if int(segundos) == -1:
                            flag_tiempo = True
                            segundos = "Fin"

    #pintamos el fondo de la pantalla 
    pantalla.fill(COLOR_PANTALLA)

    if flag_terminar == False:
        #imagen de logo
        pantalla.blit(imagen_logo, (20,20))
        pantalla.blit(imagen_utn, (20,450))
        pantalla.blit(imagen_flecha, (90,300))
        pantalla.blit(imagen_flecha_2, (930, 325))

        #dibujamos rectangulos
        pygame.draw.rect(pantalla, COLOR_RECT_VERDE, (270,20,560,200))

        #rectangulos del camino superior
        pygame.draw.rect(pantalla, COLOR_NARANJA, rect_casilla_1, border_radius=10)
        pygame.draw.rect(pantalla, COLOR_VERDE_AGUA, rect_casilla_2, border_radius=10)
        pygame.draw.rect(pantalla, COLOR_AMARILLO, rect_casilla_3, border_radius=10)
        pygame.draw.rect(pantalla, COLOR_CELESTE, rect_casilla_4, border_radius=10)
        pygame.draw.rect(pantalla, COLOR_ROJO, rect_casilla_5, border_radius=10)
        pygame.draw.rect(pantalla, COLOR_VIOLETA, rect_casilla_avanzar, border_radius=10)
        pygame.draw.rect(pantalla, COLOR_BEIGE, rect_casilla_7, border_radius=10)
        pygame.draw.rect(pantalla, COLOR_VERDE, rect_casilla_8, border_radius=10)
        #rectangulos del camino inferior
        pygame.draw.rect(pantalla, COLOR_VERDE, rect_casilla_9, border_radius=10)
        pygame.draw.rect(pantalla, COLOR_BEIGE, rect_casilla_10, border_radius=10)
        pygame.draw.rect(pantalla, COLOR_VIOLETA, rect_casilla_11, border_radius=10)
        pygame.draw.rect(pantalla, COLOR_ROJO, rect_casilla_12, border_radius=10)
        pygame.draw.rect(pantalla, COLOR_CELESTE, rect_casilla_retroceder, border_radius=10)
        pygame.draw.rect(pantalla, COLOR_AMARILLO, rect_casilla_14, border_radius=10)
        pygame.draw.rect(pantalla, COLOR_VERDE_AGUA, rect_casilla_15, border_radius=10)
        pygame.draw.rect(pantalla, COLOR_NARANJA, rect_casilla_16, border_radius=10)
        #rectangulos de comenzar y terminar. Suponiendo que son botones
        pygame.draw.rect(pantalla, COLOR_BOTONES, rect_comenzar, border_radius=25)
        pygame.draw.rect(pantalla, COLOR_BOTONES, rect_terminar, border_radius=25)
        #prueba de rectangulo para respuesta
        pygame.draw.rect(pantalla, COLOR_RECT_VERDE, rect_a, width=3)
        pygame.draw.rect(pantalla, COLOR_RECT_VERDE, rect_b, width=3)
        pygame.draw.rect(pantalla, COLOR_RECT_VERDE, rect_c, width=3)

        #Texto de tiempo y puntaje
        pantalla.blit(txt_tiempo, (850,20)) 
        pantalla.blit(txt_puntaje, (850,130)) 
        #Texto de retroceder y avanzar
        pantalla.blit(txt_avanza, (655,309)) 
        pantalla.blit(txt_1, (676,329)) 
        pantalla.blit(txt_retrocede, (463,459)) 
        pantalla.blit(txt_1, (493,480))  
        #Textos de salida y llegada
        pantalla.blit(txt_salida, (20,315)) 
        #Textos de comenzar y terminar
        pantalla.blit(txt_comenzar, (240,580))
        pantalla.blit(txt_terminar, (590,580))
        #Texto timer
        
        if flag_comenzar: 
            txt_timer = fuente.render(str(segundos), True, COLOR_LETRAS_GRIS)
            pantalla.blit(txt_timer, (1025,20))
        #Texto pregunta
            pregunta = lista_preguntas[contador]
            respuesta_1 = lista_a[contador]
            respuesta_2 = lista_b[contador]
            respuesta_3 = lista_c[contador]

            #Texto codigo
            txt_pregunta = fuente_5.render(str(pregunta), True, COLOR_NEGRO)
            pantalla.blit(txt_pregunta, (310, 50))
            txt_res_a = fuente_5.render(str(respuesta_1), True, COLOR_NEGRO)
            pantalla.blit(txt_res_a, (310, 100))
            txt_res_b = fuente_5.render(str(respuesta_2), True, COLOR_NEGRO)
            pantalla.blit(txt_res_b, (310, 140))
            txt_res_c = fuente_5.render(str(respuesta_3), True, COLOR_NEGRO)
            pantalla.blit(txt_res_c, (310, 180))

            if flag_luigi == True:
                rect_personaje.centerx = lista_casillas[0].centerx
                rect_personaje.centery = lista_casillas[0].centery
                flag_luigi = False
        
        if flag_correcta:
            puntaje = int(puntaje + 10)
            contador_casilla = contador_casilla + 2
            if contador_casilla >= (len(lista_casillas)-1):
                rect_personaje.centerx = lista_casillas[-1].centerx
                rect_personaje.centery = lista_casillas[-1].centery
                flag_terminar = True
            else:
                rect_personaje.centerx = lista_casillas[contador_casilla].centerx
                rect_personaje.centery = lista_casillas[contador_casilla].centery
        txt_puntaje_num = fuente.render(str(puntaje), True, COLOR_LETRAS_GRIS)
        pantalla.blit(txt_puntaje_num, (1025,130))

        if flag_incorrecta == True:
            if contador_casilla <= 0:
                rect_personaje.centerx = lista_casillas[0].centerx
                rect_personaje.centery = lista_casillas[0].centery
                flag_incorrecta = False
            else:
                contador_casilla = contador_casilla - 1
                rect_personaje.centerx = lista_casillas[contador_casilla].centerx
                rect_personaje.centery = lista_casillas[contador_casilla].centery
                flag_incorrecta = False

        if rect_personaje.colliderect(rect_casilla_avanzar):
            flag_acc_avanzar = True
        if rect_personaje.colliderect(rect_casilla_retroceder):
            flag_acc_retroceder = True  

        if flag_acc_avanzar == True:
            contador_casilla = contador_casilla + 1
            rect_personaje.centerx = lista_casillas[contador_casilla].centerx
            rect_personaje.centery = lista_casillas[contador_casilla].centery
            flag_acc_avanzar = False

        if flag_acc_retroceder == True:
            if flag_correcta == True:
                contador_casilla = contador_casilla - 2
            else:
                contador_casilla = contador_casilla - 1
            rect_personaje.centerx = lista_casillas[contador_casilla].centerx
            rect_personaje.centery = lista_casillas[contador_casilla].centery
            flag_acc_retroceder = False

        if flag_tiempo == True or flag_correcta == True or flag_incorrecta == True:
            contador = contador + 1 
            if contador >= len(lista_preguntas):
                contador = 0
            segundos = "5"
            flag_tiempo = False
            flag_correcta = False
            flag_incorrecta = False

        #Imprimir en pantallos los Rect()
        pantalla.blit(imagen_personaje, rect_personaje)

    '''Cambio de escena. Puntajes de los jugadores.'''
    if flag_terminar == True:
        pantalla.blit(imagen_logo, (20,20))
        pantalla.blit(txt_puntaje_tabla, (430,50)) 
        #personaje
        imagen_personaje = pygame.transform.scale(imagen_personaje, (100,200))
        rect_personaje.x = 50
        rect_personaje.y = 350      
        pantalla.blit(imagen_personaje, rect_personaje)

        #renderiza nombres y puntajes
        lista_ordenda = []
        y_offset = 150
        lista_ordenada = ordenamiento(lista_jugadores, "puntaje", True)
        lista_ordenada = lista_ordenada[:10]
        for jugador in lista_ordenada:
            nombre_render = fuente.render(jugador['nombre'], True, COLOR_NEGRO)
            puntaje_render = fuente.render(str(jugador['puntaje']), True, COLOR_NEGRO)
            pantalla.blit(nombre_render, (400, y_offset))
            pantalla.blit(puntaje_render, (660, y_offset))
            y_offset += 50  # Incrementar el offset para la próxima línea

        #casilla para el nombre
        pygame.draw.rect(pantalla, COLOR_NEGRO, rect_nombre, width=2)
        txt_nombre_info = fuente_3.render("Aca escribi tu nombre", True, COLOR_NEGRO)
        pantalla.blit(txt_nombre_info, (rect_nombre.x, rect_nombre.y - 30))
        #escribir el nombre
        nombre_escrito = fuente_3.render(nombre, True, COLOR_NEGRO)
        pygame.draw.rect(pantalla, COLOR_NEGRO, rect_nombre_escrito, width=2)
        pantalla.blit(nombre_escrito, (rect_nombre_escrito.x+5, rect_nombre_escrito.y+1)) 

        pygame.draw.rect(pantalla, COLOR_GRIS, rect_listo)
        txt_listo = fuente_3.render("Listo", True, COLOR_BLANCO)
        pantalla.blit(txt_listo, (rect_listo.x + 5, rect_listo.y + 5))

        if flag_actualizar_datos:
            nuevo_dato = {'nombre': nombre, 'puntaje': puntaje}
            # Agregar el nuevo dato a la lista de jugadores
            lista_jugadores.append(nuevo_dato)
            # Escribir la lista completa al archivo JSON
            with open(archivo_json, 'w') as archivo:
                json.dump(lista_jugadores, archivo, indent=4)

            flag_actualizar_datos = False

    pygame.display.flip()
pygame.quit()

