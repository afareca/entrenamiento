# -*- coding: utf-8 -*-
# Brief de ilustraciones de Vigor y Amplitud: id (= nombre de archivo en medios/<app>/), nombre y movimiento.
# Es la fuente de los prompts que se pegan en el generador de imágenes. "fija" = postura sostenida, una sola imagen.
# 'fija' = postura sostenida: una sola imagen.
SILLA='una silla firme sin ruedas'
VIGOR=[
 ['Calentamiento · todos los días',[
  ['marcha','Marcha en el sitio','De pie, marcha en el sitio subiendo las rodillas y balanceando los brazos: rodilla derecha arriba → pies juntos → rodilla izquierda arriba → pies juntos.'],
  ['circulos_brazos','Círculos de brazos','De pie, brazos extendidos a los lados a la altura de los hombros haciendo círculos amplios: brazos adelante → arriba → atrás → abajo.'],
  ['bisagra','Bisagra de cadera','De pie, manos en la cadera: de pie → cadera hacia atrás con la espalda recta → torso a 45° → volviendo.']]],
 ['Día A · Piernas',[
  ['sentarse_pararse','Sentarse y pararse','Sentado al borde de '+SILLA+', brazos cruzados al pecho: sentado → inclinando el torso adelante → de pie → bajando a sentarse.'],
  ['puente','Puente de glúteo','Boca arriba, rodillas dobladas: cadera en el piso → subiendo → cadera arriba en línea de rodillas a hombros → bajando.'],
  ['zancada_apoyo','Zancada estática con apoyo','Una mano en el espaldar de '+SILLA+', un pie adelante y otro atrás: arriba → bajando vertical → rodilla de atrás cerca del piso → subiendo.'],
  ['elevacion_talones','Elevación de talones','De pie frente a una pared, manos apoyadas: talones en el piso → subiendo en puntas → arriba → bajando.'],
  ['escalon','Subir escalón','De perfil a un escalón de una escalera, mano en la baranda: un pie en el escalón → subiendo → de pie sobre el escalón → bajando.'],
  ['sentadilla','Sentadilla','Sin peso, brazos al frente: de pie → bajando → muslos paralelos al piso → subiendo.'],
  ['puente_una_pierna','Puente a una pierna','Boca arriba, una pierna estirada al aire en línea con el muslo contrario: cadera abajo → subiendo sobre un pie → arriba → bajando.'],
  ['zancada_atras','Zancada atrás','De pie: un pie da un paso atrás → bajando → ambas rodillas a 90° → volviendo a de pie.'],
  ['sentadilla_bulgara','Sentadilla búlgara','Pie de atrás apoyado sobre el asiento de '+SILLA+': arriba → bajando vertical → rodilla de atrás cerca del piso → subiendo.'],
  ['pmr_libre','Peso muerto a una pierna','Sin peso, brazos al frente: de pie → inclinando el torso con la pierna libre hacia atrás → torso y pierna horizontales → volviendo.']]],
 ['Día B · Torso y brazos',[
  ['flexion_pared','Flexión en pared','De pie frente a una pared, manos a la altura del pecho: brazos extendidos → bajando el pecho hacia la pared → cerca de la pared → empujando.'],
  ['remo_toalla','Remo con toalla en la puerta','Toalla pasada por la manija de una puerta cerrada, sosteniendo un extremo en cada mano, cuerpo inclinado hacia atrás con los pies cerca de la puerta: brazos extendidos → tirando → codos atrás y pecho cerca de la puerta → volviendo.'],
  ['angel_pared','Ángel en pared','De pie con espalda, cabeza y glúteos contra la pared, brazos en W: codos abajo → brazos subiendo pegados a la pared → brazos en V arriba → bajando.'],
  ['plancha_inclinada','Plancha inclinada','Antebrazos apoyados sobre el borde de una mesa firme, cuerpo en línea recta de cabeza a talones, sostenida.','fija'],
  ['birddog','Bird dog','En cuatro apoyos: posición neutra → extendiendo brazo derecho al frente y pierna izquierda atrás → ambos extendidos en línea con la espalda → volviendo.'],
  ['flexion_inclinada','Flexión inclinada','Manos sobre el borde de una mesa firme: brazos extendidos → bajando → pecho cerca del borde → subiendo.'],
  ['deadbug','Dead bug','Boca arriba, brazos al techo y rodillas a 90°: posición inicial → extendiendo brazo derecho y pierna izquierda → ambos extendidos casi al piso → volviendo.'],
  ['flexion_rodillas','Flexión en rodillas','Plancha con las rodillas apoyadas en el piso: brazos extendidos → bajando → pecho cerca del piso → subiendo.'],
  ['plancha','Plancha en antebrazos','Antebrazos y rodillas o puntas de pie en el piso, cuerpo en línea recta, sostenida.','fija'],
  ['plancha_lateral','Plancha lateral en rodillas','De lado sobre el antebrazo, rodillas dobladas apoyadas: cadera abajo → subiendo → cuerpo en línea de rodillas a cabeza → sostenida.']]],
 ['Día C · Equilibrio y tenis',[
  ['equilibrio_un_pie','Equilibrio en un pie','De pie sobre una pierna, la otra rodilla levantada a la altura de la cadera, una mano rozando el espaldar de '+SILLA+'.','fija'],
  ['talon_punta','Caminar talón–punta','Caminando sobre una línea recta en el piso, poniendo el talón de un pie justo delante de la punta del otro: 4 pasos seguidos.'],
  ['rotacion_tronco','Rotación de tronco de tenis','De pie en posición de tenis, rodillas suaves, brazos como sosteniendo una raqueta imaginaria: hombros al frente → girando el tronco a la derecha → girando a la izquierda → al frente.'],
  ['paso_lateral','Desplazamiento lateral','De pie en posición atlética, rodillas semiflexionadas: pies juntos → paso lateral amplio → pies separados → el otro pie se acerca.'],
  ['abre_libro','Libro abierto','Acostado de lado, rodillas dobladas, brazos estirados al frente juntos: brazos juntos → el brazo de arriba abre en arco hacia atrás siguiendo la mirada → pecho abierto al techo → volviendo.'],
  ['reloj','Reloj de equilibrio','De pie sobre una pierna, la otra toca el piso con la punta en distintas direcciones: adelante → al lado → atrás en diagonal → de vuelta al centro.'],
  ['zancada_lateral','Zancada lateral','De pie: paso lateral amplio → doblando la rodilla de ese lado con la otra pierna estirada → abajo con cadera atrás → volviendo.'],
  ['split_step','Split step de tenis','Saltito corto de tenis: posición atlética → pequeño salto → cae con pies separados al ancho de hombros y rodillas suaves → listo para moverse.']]],
 ['Día D · Movilidad',[
  ['gato','Gato–camello','En cuatro apoyos: espalda neutra → espalda redondeada hacia el techo → neutra → espalda arqueada hacia el piso.'],
  ['pantorrilla_pared','Estiramiento de pantorrilla','De pie frente a una pared, manos apoyadas, una pierna atrás estirada con el talón en el piso y la otra adelante doblada.','fija'],
  ['isquios_silla','Isquiotibiales en silla','Sentado al borde de '+SILLA+', una pierna estirada con el talón en el piso y la punta arriba, torso inclinado adelante con la espalda recta.','fija'],
  ['pecho_puerta','Estiramiento de pecho en puerta','De pie en el marco de una puerta, antebrazos apoyados en los lados del marco a la altura de los hombros, un pie adelante y el pecho avanzando.','fija'],
  ['flexor_cadera','Flexor de cadera','Una rodilla apoyada en un cojín en el piso y el otro pie adelante, torso erguido, una mano en '+SILLA+' para equilibrio, cadera adelantada.','fija']]],
]
AMPLITUD=[
 ['Inicio · todos los días',[
  ['respira_sentada','Respiración lenta sentada','Sentada en '+SILLA+', espalda erguida, manos sobre las costillas: costillas en reposo → expandiéndose al inhalar → máxima expansión → cerrándose al exhalar.'],
  ['circulos_brazos','Círculos de brazos','De pie, brazos extendidos a los lados a la altura de los hombros haciendo círculos amplios: brazos adelante → arriba → atrás → abajo.'],
  ['marcha','Marcha en el sitio','De pie, marcha en el sitio subiendo las rodillas y balanceando los brazos: rodilla derecha arriba → pies juntos → rodilla izquierda arriba → pies juntos.']]],
 ['Día A · Cadera y piernas',[
  ['isquios_silla','Isquiotibiales en silla','Sentada al borde de '+SILLA+', una pierna estirada con el talón en el piso y la punta arriba, torso inclinado adelante con la espalda recta.','fija'],
  ['flexor_cadera_pie','Flexor de cadera de pie','De pie en zancada corta con una mano en el espaldar de '+SILLA+', rodilla de atrás casi estirada, cadera adelantada y torso erguido.','fija'],
  ['figura4_silla','Glúteo en figura 4 sentada','Sentada en '+SILLA+', tobillo derecho cruzado sobre la rodilla izquierda, torso inclinado levemente adelante con la espalda recta.','fija'],
  ['pantorrilla_pared','Estiramiento de pantorrilla','De pie frente a una pared, manos apoyadas, una pierna atrás estirada con el talón en el piso y la otra adelante doblada.','fija'],
  ['mariposa','Mariposa','Sentada en el piso con la espalda recta, plantas de los pies juntas y rodillas abiertas hacia los lados, manos en los tobillos.','fija'],
  ['isquios_toalla','Isquiotibiales con toalla','Boca arriba, una pierna estirada hacia el techo sostenida con una toalla en el pie, la otra pierna doblada con el pie apoyado.','fija'],
  ['flexor_cadera','Flexor de cadera en rodilla','Una rodilla apoyada en un cojín en el piso y el otro pie adelante, torso erguido, una mano en '+SILLA+', cadera adelantada.','fija'],
  ['figura4','Glúteo en figura 4 acostada','Boca arriba, tobillo derecho cruzado sobre la rodilla izquierda, manos abrazando el muslo izquierdo hacia el pecho.','fija'],
  ['cuadriceps','Estiramiento de cuádriceps','De pie, una mano en el espaldar de '+SILLA+', la otra mano sostiene el empeine llevando el talón hacia el glúteo, rodillas juntas.','fija'],
  ['zancada_rotacion','Zancada con rotación','Zancada baja con la rodilla de atrás apoyada en un cojín, una mano en el piso por dentro del pie de adelante y el otro brazo abierto hacia el techo girando el tronco.','fija'],
  ['sentadilla_sostenida','Sentadilla sostenida con apoyo','Sentadilla profunda sosteniéndose con las dos manos del borde de una mesa firme, talones en el piso, espalda larga.','fija']]],
 ['Día B · Hombros y columna',[
  ['pecho_puerta','Estiramiento de pecho en puerta','De pie en el marco de una puerta, antebrazos apoyados en los lados del marco a la altura de los hombros, un pie adelante y el pecho avanzando.','fija'],
  ['brazo_cruzado','Hombro con brazo cruzado','De pie, un brazo estirado cruzando el pecho, sostenido por encima del codo con la otra mano, hombros abajo.','fija'],
  ['toracica_silla','Rotación de tronco sentada','Sentada en '+SILLA+', pies apoyados, brazos cruzados al pecho: al frente → girando el tronco a la derecha → al frente → girando a la izquierda.'],
  ['gato_silla','Gato–camello sentada','Sentada al borde de '+SILLA+', manos sobre las rodillas: espalda neutra → espalda redondeada mirando al ombligo → neutra → pecho abierto y espalda arqueada.'],
  ['lateral_pie','Inclinación lateral','De pie, pies al ancho de la cadera, un brazo arriba: brazo arriba → inclinando el tronco hacia el lado contrario → máxima inclinación → volviendo.'],
  ['angel_pared','Ángel en pared','De pie con espalda, cabeza y glúteos contra la pared, brazos en W: codos abajo → brazos subiendo pegados a la pared → brazos en V arriba → bajando.'],
  ['gato','Gato–camello','En cuatro apoyos: espalda neutra → espalda redondeada hacia el techo → neutra → espalda arqueada hacia el piso.'],
  ['abre_libro','Libro abierto','Acostada de lado, rodillas dobladas, brazos estirados al frente juntos: brazos juntos → el brazo de arriba abre en arco hacia atrás siguiendo la mirada → pecho abierto al techo → volviendo.'],
  ['toalla_espalda','Hombros con toalla en la espalda','De pie, sosteniendo una toalla detrás de la espalda: una mano arriba por detrás de la cabeza y la otra abajo a la altura de la cintura, tirando suave.','fija'],
  ['nino','Postura del niño','De rodillas sobre un cojín, glúteos hacia los talones, torso adelante y brazos estirados al frente en el piso, frente apoyada.','fija']]],
 ['Día C · Fuerza y equilibrio',[
  ['sentarse_pararse','Sentarse y pararse','Sentada al borde de '+SILLA+', brazos cruzados al pecho: sentada → inclinando el torso adelante → de pie → bajando a sentarse.'],
  ['equilibrio_un_pie','Equilibrio en un pie','De pie sobre una pierna, la otra rodilla levantada a la altura de la cadera, una mano rozando el espaldar de '+SILLA+'.','fija'],
  ['flexion_pared','Flexión en pared','De pie frente a una pared, manos a la altura del pecho: brazos extendidos → bajando el pecho hacia la pared → cerca de la pared → empujando.'],
  ['puente','Puente de glúteo','Boca arriba, rodillas dobladas: cadera en el piso → subiendo → cadera arriba en línea de rodillas a hombros → bajando.'],
  ['elevacion_talones','Elevación de talones','De pie frente a una pared, manos apoyadas: talones en el piso → subiendo en puntas → arriba → bajando.'],
  ['talon_punta','Caminar talón–punta','Caminando sobre una línea recta en el piso, poniendo el talón de un pie justo delante de la punta del otro: 4 pasos seguidos.'],
  ['zancada_apoyo','Zancada estática con apoyo','Una mano en el espaldar de '+SILLA+', un pie adelante y otro atrás: arriba → bajando vertical → rodilla de atrás cerca del piso → subiendo.'],
  ['flexion_inclinada','Flexión inclinada','Manos sobre el borde de una mesa firme: brazos extendidos → bajando → pecho cerca del borde → subiendo.'],
  ['reloj','Reloj de equilibrio','De pie sobre una pierna, la otra toca el piso con la punta en distintas direcciones: adelante → al lado → atrás en diagonal → de vuelta al centro.'],
  ['sentadilla','Sentadilla','Sin peso, brazos al frente: de pie → bajando → muslos paralelos al piso → subiendo.'],
  ['zancada_atras','Zancada atrás','Una mano en el espaldar de '+SILLA+': de pie → un pie da un paso atrás → ambas rodillas dobladas → volviendo.'],
  ['puente_marcha','Puente con marcha','Puente con la cadera arriba: ambos pies apoyados → un pie sube con la rodilla a 90° → baja → sube el otro.']]],
]
