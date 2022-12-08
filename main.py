from chatterbot import ChatBot
from chatterbot.trainers import ListTrainer
from flask import Flask, render_template, request
#Creamos un bot llamado LCCBot
chatbot = ChatBot('LCCBot',logic_adapters=[{'import_path': 'chatterbot.logic.BestMatch'},])



trainer = ListTrainer(chatbot)

trainer.train([
"Que ocupa para titularme de LCC?",
"Haber cubierto todos los créditos del programa, haber obtenido por lo menos 900 puntos  en el EGEL del CENEVAL, haber cumplido con el Servicio Social, haber satisfecho con los requerimientos específicos para la opción de titulación seleccionada y cumplir con los requisitos establecidos en los artículos 84 y 85 del Reglamento Escolar vigente.",
"¿Cuántos créditos tengo que completar?",
"Debes de completar 383 créditos para titularte de LCC",
"Donde puedo ver cuántos créditos llevó completado? ",
"Puedes consultar tus créditos completados en el portal de alumnos > Mis Materias > Kardex > Resumen ",
"Que ocupa para titularme de LCC?",
"Haber cubierto todos los créditos del programa, haber obtenido por lo menos 900 puntos  en el EGEL del CENEVAL, haber cumplido con el Servicio Social, haber satisfecho con los requerimientos específicos para la opción de titulación seleccionada y cumplir con los requisitos establecidos en los artículos 84 y 85 del Reglamento Escolar vigente.",
"Cómo presentar el EGEL?",
"Puedes consultar el como presentar el EGEL en: https://serviciosescolares.unison.mx/titulacion-por-ceneval/",
"Que ocupa para titularme de LCC?",
"Haber cubierto todos los créditos del programa, haber obtenido por lo menos 900 puntos  en el EGEL del CENEVAL, haber cumplido con el Servicio Social, haber satisfecho con los requerimientos específicos para la opción de titulación seleccionada y cumplir con los requisitos establecidos en los artículos 84 y 85 del Reglamento Escolar vigente.",
"Cuales son las opciones de titulación?",
"Puedes revisar las opciones de titulación y sus requisitos en: https://serviciosescolares.unison.mx/opcionestitulacion/",
"Donde puedo recibir ayuda con mi titulación?",
"Puedes recibir ayuda para tu titulación en Servicios Escolares",
"Dónde está el edificio de servicios escolares?",
"La dirección de servicios escolares es: Del Conocimiento, Edificio 8A, Centro, 83000 Hermosillo, Son. ",
"Que ocupa para titularme de LCC?",
"Haber cubierto todos los créditos del programa, haber obtenido por lo menos 900 puntos  en el EGEL del CENEVAL, haber cumplido con el Servicio Social, haber satisfecho con los requerimientos específicos para la opción de titulación seleccionada y cumplir con los requisitos establecidos en los artículos 84 y 85 del Reglamento Escolar vigente.",
"Cuales son los requisitos establecidos en el artículo 84?",
"Puedes consultar el articulo 84 en: https://www.unison.mx/institucional/marconormativo/reglamentosescolares/ReglamentoEscolar2017/#p=28",
"Cuáles son los requisitos establecidos en el artículo 85?",
"Puedes consultar el articulo 85 en: https://www.unison.mx/institucional/marconormativo/reglamentosescolares/ReglamentoEscolar2017/#p=28",
"¿Qué nivel de inglés te piden para titularme?",
"Debes de tener por lo menos 4 en tu nivel de inglés",
"Puedo titularme con un nivel de ingles menor a 4?",
"No, ocupas un nivel de inglés mayor o igual a 4 para titularte",
"Donde puedo consultar mi nivel de inglés?",
"Puedes consultar tu nivel de inglés en portal de alumnos > Mis Materias > Kardex > Resumen",
"Cuantos puntos CULTUREST ocupo para titularme?",
"Ocupas 4 puntos culturest para poder titularte",
"Donde puedo consultar cuántos puntos CULTUREST ulturest llevó completado?",
"Puedes consultar tus puntos culturest completados en portal de alumnos > Mis Materias >Actividades Culturales y Deportivas ",
"Puedo titularme si tengo menos de 4 puntos CULTUREST ?",
"No, necesitas 4 puntos culturest para titularte",
"Necesito puntos culturest para hacer el servicio social?",
"No necesitas puntos culturest para realizar tu servicio social.",
"Donde puedo consultar mi estado de titulación?",
"Puedes consultar tu estado de titulación en portal de alumnos > Titulación",
"Puedo titularme si debo colegiaturas?",
"No puedes titularte si tienes deudas",
"Donde puedo consultar mis deudas?",
"Puedes consultar tus deudas en portal de alumnos > Estado de Cuenta",
"Cuando puedo darme de baja de una materia?",
"Puedes solicitar el darte de baja de una materia dentro de los primeros 45 días naturales contados a partir del inicio del período escolar.",
"Donde puedo solicitar el darme de baja de una materia?",
"Puedes solicitar el darte de baja de una materia en portal de alumnos > Mis Materias > Bajas Voluntarias",
"¿Qué materias puedo dar de baja?",
"Sólo podrás dar de baja las materias en las que te encuentres inscrito(a) en el ciclo actual",
"Qué pasa si doy de baja una materia por equivocación?",
"Si por error diste de baja alguna asignatura acude a Servicios Escolares antes de la fecha establecida por el Calendario Oficial.",
"Que necesito para el servicio social?",
"Puedes empezar el proceso de inscripción al servicio social después de tener el 70% de los créditos. Cumplir con el proceso de inducción al servicio social, en donde recibirá una constancia de su asistencia (Concibe por evento de inducción en semestres nones asistencia a Feria Universitaria de Servicio Social y plática de inducción y semestres pares plática de inducción, ambas de acuerdo a calendario establecido por el CISSU). Presentar para su autorización y por triplicado, el Formato F02 (anexo) al responsable de servicio social de su programa educativo o al coordinador de su división, para solicitar el registro a un proyecto en condición de aprobado. El coordinador divisional de servicio social, autoriza el registro y lo asigna a un proyecto. Atender a lo anterior conforme a los tiempos establecidos en la convocatoria.",
"Donde puedo encontrar información sobre el servicio social?",
"El siguiente link te llevara al manual oficial de la universidad: https://buhos.uson.mx/ServicioSocial/Avisos/mostrarAdjunto?id=NTYuV2VTSGtyY1dkbEtqdWFFZXcxLzEvMDAwMSAxMjowMDowMCBBTQ==",
"¿Cuánto dura el servicio social?",
"Dependiendo del proyecto y de las horas que se trabajen puede durar más de un semestre, pero todos los proyectos necesitan un mínimo de 480 horas empeñadas por participante.",
"A quién puedo consultar información sobre el servicio social?",
"Al coordinador divisional de servicio social",
"Necesito créditos CULTUREST para hacer el servicio social?",
"No, puedes realizar tu servicio social sin tener en cuenta los puntos culturest que llevas acreditados",
"¿Qué son las prácticas profesionales?",
"Son un conjunto de actividades y quehaceres propios de la formación profesional del estudiante, que le permite relacionarse con el medio laboral donde se desempeñará y le da la oportunidad de aplicar los conocimientos y habilidades adquiridas a través de su formación académica en el programa educativo.",
"Las prácticas profesionales son obligatorias?",
"Si,son obligatorias para poder titularse en LCC ",
"Donde puedo encontrar información sobre las prácticas profesionales?",
"El reglamento oficial de las practicas se encuentra aqui: https://www.unison.mx/institucional/marconormativo/reglamentosescolares/ReglamentoPracticasProfesionales/ReglamentoPracticasProfesionales2017/ReglamentoPracticasProfesionales_2017.pdf",
"¿Qué son las prácticas profesionales?",
"Las prácticas profesionales serán obligatorias en todos los programas educativos de nivel licenciatura",
"¿Cuánto tiempo duran las prácticas profesionales? ",
"Deberán satisfacer 250 horas, equivalentes a 10 créditos del plan de estudios",
"A quién le puedo pedir información específica sobre las prácticas profesionales?",
"Puedes pedir información específica a la coordinadora de las prácticas profesionales, Dra. Lilia Encinas Norzagaray. Puedes mandar correo a lilia.encinasnorzagaray@unison.mx",
"A quién le puedo pedir información específica sobre el servicio social?",
"Puedes pedir información específica a la coordinadora de Servicio Social de la División de Ciencias Sociales, Dra. Dolores Guadalupe Morales Flores. Puedes mandar correo a dolores.morales@unison.mx",
"Quién es la coordinación de la carrera?",
"Dra. Sonia Guadalupe Sosa León, E-mail: sonia@mat.uson.mx,",
"Cómo me puedo comunicar con la coordinación de la carrera?",
"Con la Dra. Sonia Guadalupe Sosa León, Tel: (662) 259-2155 ext 2486, E-mail: sonia@mat.uson.mx, Ubicación: Edificio 3K-4",
"Con quién me puedo asesorar para la tesis?",
"Dr. Julio Waissman Villanova. E-mail: juliowaissman@mat.uson.mx",
"Dónde se ubica el edificio de LCC?",
"El edificio de LCC se ubica en: Edificio 3K4, Ciencias de la Computación, Boulevard Luis Encinas y Rosales s/n, Col. Centro, Hermosillo, Sonora. CP 83000",
"En qué horario está abierto el edificio?",
"El edificio 3K4 está abierto en un horario de 8:00 a 14:00 horas",
"¿Cuál es el número de teléfono de LCC?",
"El número de teléfono es (662) 259 2155",
"En qué horario se puede utilizar ese teléfono?",
"El horario de atención de la línea es de 8:00 a 14:00 horas",
"¿Cuál es el correo de LCC?",
"El correo de LCC es computacion@mat.uson.mx",
"Cuál es el contacto de LCC?",
"LCC cuenta con un número de teléfono: (662) 259 2155, también cuenta con un correo electrónico: computacion@mat.uson.mx",
"En qué horario se puede marcar al teléfono?",
"El horario de atención de la línea es de 8:00 a 14:00 horas",
"LCC tiene página web?",
"La página web de LCC es https://cc.unison.mx",
"¿Qué puedo encontrar en la página de LCC?",
"Puedes encontrar información general de la carrera, así como el programa y plan de estudios, ubicación y el contacto de coordinación",
"Dónde puedo consultar el programa de LCC?",
"Puedes consultarlo desde la página de LCC: https://cc.unison.mx",
"Dónde puedo consultar información general de LCC?",
"Puedes consultar información en la página de LCC: https://cc.unison.mx",
"Dónde puedo consultar noticias o avisos de LCC?",
"En la página de LCC: https://cc.unison.mx",
])

app = Flask(__name__)
app.static_folder = 'static'

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/get")
def get_bot_response():
    userText = request.args.get('msg')
    return str(chatbot.get_response(userText))


if __name__ == '__main__':
    app.run()