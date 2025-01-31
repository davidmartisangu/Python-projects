# Lista de las 20 primeras frases
import random

frases = [
    "Bajo la luna brillante, el río fluye sereno, reflejando estrellas en su superficie tranquila.",
    "La brisa marina acaricia mi piel mientras observo el horizonte, perdido en pensamientos profundos.",
    "En el corazón de la ciudad, el bullicio de la gente contrasta con la tranquilidad de un parque silencioso.",
    "El aroma a tierra mojada después de la lluvia es un regalo para los sentidos en un día gris.",
    "Las luces parpadeantes de la ciudad nocturna crean un escenario de ensueño en la distancia.",
    "El sonido del violín en una melodía triste me hace sentir una profunda melancolía.",
    "Un abrazo apretado transmite más amor que mil palabras en un momento de necesidad.",
    "La mirada comprensiva de un amigo fiel es un faro en medio de la tormenta de la vida.",
    "La primera luz del alba revela un mundo lleno de promesas y oportunidades frescas.",
    "El susurro de las hojas en un bosque antiguo es un eco de historias pasadas y secretos guardados.",
    "Un viaje en tren a través de montañas majestuosas ofrece vistas que roban el aliento.",
    "Las estrellas fugaces cruzan el cielo nocturno como deseos en busca de ser concedidos.",
    "El sabor de la comida casera me transporta instantáneamente a mi infancia y a la comodidad del hogar.",
    "El aroma a café recién molido inunda la cocina, despertando los sentidos con su fragancia embriagadora.",
    "La carcajada de un niño es una sinfonía de alegría que llena el aire y hace sonreír a todos.",
    "Las olas rompen con fuerza en la costa, recordándonos la majestuosidad del océano.",
    "Un libro bien escrito es un portal a mundos inexplorados y a aventuras que aguardan ser vividas.",
    "El tañido de las campanas de una iglesia en un día soleado crea un ambiente sereno y espiritual.",
    "El crujir de la nieve bajo los pies es música de invierno que nos hace sentir vivos.",
    "Un atardecer anaranjado pinta el cielo con tonos cálidos y evoca un sentimiento de nostalgia."
]

def test_sentence():
    sentence=random.choice(frases)
    return sentence

