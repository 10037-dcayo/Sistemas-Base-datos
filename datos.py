{
 "cells": [
  {
   "cell_type": "markdown",
   "id": "3d59342e",
   "metadata": {},
   "source": [
    "# Conjunto de datos personalizado"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "76e065cb",
   "metadata": {},
   "source": [
    "En situaciones en las que los datos no están fácilmente disponibles pero son necesarios, **tendrá que recurrir a recopilar los datos usted mismo.** Hay muchos métodos que puede usar para adquirir estos datos, desde webscraping hasta API. Pero a veces, terminará necesitando crear **datos falsos o \"ficticios\".** Los datos ficticios pueden ser útiles en momentos en los que conoce las funciones exactas que utilizará y los tipos de datos incluidos, pero simplemente no tiene los datos en sí.\n",
    "\n",
    "Aquí, le mostraré **cómo creé 100 000 filas de datos ficticios.** Estos datos tampoco son puramente aleatorios. Si lo fuera, construirlo habría sido mucho más fácil. A veces, al crear datos ficticios desde cero, deberá desarrollar tendencias o patrones dentro de los datos que puedan reflejar el comportamiento del mundo real. "
   ]
  },
  {
   "cell_type": "markdown",
   "id": "1ac08fd8",
   "metadata": {},
   "source": [
    "# **La necesidad de construir un conjunto de datos**"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "71e91264",
   "metadata": {},
   "source": [
    "**Supongamos que está creando una aplicación desde cero y necesita establecer una gran base de usuarios para, por ejemplo, realizar pruebas.** Se le proporciona una lista de características y sus respectivos tipos de datos.\n",
    "\n",
    "**Esta base de usuarios también debe reflejar con cierta precisión los usuarios y las tendencias del mundo real, por lo que no puede ser completamente aleatoria.** Por ejemplo, no desea que un usuario tenga un título universitario y también tenga 10 años. Además, es posible que no desee una sobrerrepresentación de un punto de datos específico, como más hombres que mujeres. Todos estos son puntos a tener en cuenta a la hora de crear su conjunto de datos.\n",
    "\n",
    "**Dado que los datos del mundo real rara vez son verdaderamente aleatorios, un conjunto de datos como este sería una excelente simulación para otros conjuntos de datos que manejará en el futuro.**"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "c6482288",
   "metadata": {},
   "source": [
    "# Construcción del conjunto de datos"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "d02a8e8d",
   "metadata": {},
   "source": [
    "Para codificar, comience importando las siguientes bibliotecas:"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 4,
   "id": "97b3d6da",
   "metadata": {},
   "outputs": [],
   "source": [
    "import pandas as pd\n",
    "import uuid\n",
    "import random\n",
    "from faker import Faker\n",
    "import datetime"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "db21c16c",
   "metadata": {},
   "source": [
    "**Size**"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "44ce2a03",
   "metadata": {},
   "source": [
    "El tamaño del conjunto de datos será de 5000 puntos de datos (puede hacer más, pero el procesamiento puede demorar más). Asigné esta cantidad a una variable constante, que usé en todo momento:"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 5,
   "id": "29f6b5ac",
   "metadata": {},
   "outputs": [],
   "source": [
    "num_users = 5000"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "4f8ba686",
   "metadata": {},
   "source": [
    "**Características**"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "555a14da",
   "metadata": {},
   "source": [
    "Elegí 10 características que esperaba que fueran las más comunes en un conjunto de datos regular de usuarios. Estas características y los respectivos tipos de datos son:\n",
    "\n",
    "     - ID: una cadena única de caracteres para identificar a cada usuario.\n",
    "     - Gender (Sexo:) tipo de datos de cadena de tres opciones.\n",
    "     - Subscriber (Suscriptor:) una opción binaria Verdadero/Falso de su estado de suscripción.\n",
    "     - Name (Nombre:) tipo de datos de cadena del nombre y apellido del usuario.\n",
    "     - Email (Correo electrónico:) q  tipo de datos de cadena de la dirección de correo electrónico del usuario.\n",
    "     - Last Login (Último inicio de sesión:) tipo de datos de cadena de la última hora de inicio de sesión.\n",
    "     - Date of Birth (Fecha de nacimiento:) formato de cadena de año-mes-día.\n",
    "     - Education (Educación:) nivel de educación actual como un tipo de datos de cadena.\n",
    "     - Bio: descripciones de cadenas cortas de palabras aleatorias.\n",
    "     - Rating (Calificación:) tipo entero de una calificación de 1 a 5 de algo."
   ]
  },
  {
   "cell_type": "markdown",
   "id": "17841653",
   "metadata": {},
   "source": [
    "Ingresé lo anterior como una lista de características para inicializar un marco de datos de Pandas:"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 6,
   "id": "5a145d81",
   "metadata": {},
   "outputs": [],
   "source": [
    "# A list of 10 features\n",
    "features = [\n",
    "    \"id\",\n",
    "    \"gender\",\n",
    "    \"subscriber\",\n",
    "    \"name\",\n",
    "    \"email\",\n",
    "    \"last_login\",\n",
    "    \"dob\",\n",
    "    \"education\",\n",
    "    \"bio\",\n",
    "    \"rating\"\n",
    "]# Creating a DF for these features\n",
    "df = pd.DataFrame(columns=features)"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "32e7f58f",
   "metadata": {},
   "source": [
    "**Creación de datos**"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "b84da0a2",
   "metadata": {},
   "source": [
    "Algunos atributos anteriores normalmente deberían contener datos desequilibrados. Se puede asumir con seguridad con una investigación rápida, algunas opciones no estarán igualmente representadas. Para un conjunto de datos más realista, estas tendencias deben reflejarse."
   ]
  },
  {
   "cell_type": "markdown",
   "id": "6707781a",
   "metadata": {},
   "source": [
    "**IDs**"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "57be8b83",
   "metadata": {},
   "source": [
    "Para el atributo ID, utilicé la biblioteca uuid para generar una cadena aleatoria de caracteres 100 000 veces. Luego, lo asigné al atributo ID en el marco de datos."
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 7,
   "id": "9417eb1d",
   "metadata": {},
   "outputs": [],
   "source": [
    "df['id'] = [uuid.uuid4().hex for i in range(num_users)]"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "92e30db5",
   "metadata": {},
   "source": [
    "**UUID es una gran biblioteca para generar identificaciones únicas para cada usuario debido a su posibilidad astronómicamente baja de duplicar una identificación.** Es una gran opción cuando se trata de generar conjuntos de caracteres de identificación únicos. Pero, si desea asegurarse de que no se repitieron las ID, puede realizar una verificación simple en el marco de datos con lo siguiente:"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 8,
   "id": "4be6d244",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "True\n"
     ]
    }
   ],
   "source": [
    "print(df['id'].nunique()==num_users)"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "a14229fb",
   "metadata": {},
   "source": [
    "Esto devolverá True si todas las ID en el conjunto de datos son únicas."
   ]
  },
  {
   "cell_type": "markdown",
   "id": "e42be811",
   "metadata": {},
   "source": [
    "**Gender**"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "a189353d",
   "metadata": {},
   "source": [
    "**Este atributo es uno de los casos en los que probablemente no se debería utilizar una elección igualmente aleatoria. Porque se puede suponer con seguridad que cada elección no tiene la misma probabilidad de ocurrir.**\n",
    "\n",
    "Para el género, proporcioné tres opciones: masculino, femenino y na. Sin embargo, si tuviera que usar la biblioteca aleatoria de Python, cada opción podría mostrarse igualmente en el conjunto de datos. En realidad, habría significativamente más opciones masculinas y femeninas que na. Así que decidí mostrar ese desequilibrio en los datos:"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 10,
   "id": "53792c85",
   "metadata": {},
   "outputs": [],
   "source": [
    "genders = [\"male\", \"female\", \"na\"]"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 11,
   "id": "bc4eb9a8",
   "metadata": {},
   "outputs": [],
   "source": [
    "df['gender'] = random.choices(\n",
    "    genders, \n",
    "    weights=(47,47,6), \n",
    "    k=num_users\n",
    ")"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "9744528c",
   "metadata": {},
   "source": [
    "Al usar la biblioteca aleatoria, proporcioné la función de opciones/choices () con la lista de opciones de género, pesos para cada opción y cuántas opciones hacer representadas por \"k\". Luego se asignó al atributo de \"género\" del marco de datos. El desequilibrio que describí antes está representado en la sección de ponderaciones con una opción \"na\" que aparece aproximadamente el 6% de las veces."
   ]
  },
  {
   "cell_type": "markdown",
   "id": "57f6abcf",
   "metadata": {},
   "source": [
    "**Subscriber**"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "06faf5ef",
   "metadata": {},
   "source": [
    "Para este atributo, las opciones se pueden seleccionar aleatoriamente entre Verdadero y Falso. Dado que se puede esperar razonablemente que aproximadamente la mitad de los usuarios sean suscriptores."
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 14,
   "id": "63766ad3",
   "metadata": {},
   "outputs": [],
   "source": [
    "choice = [True, False]\n",
    "df['subscriber'] = random.choices(\n",
    "    choice, \n",
    "    k=num_users\n",
    ")"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "734bcb93",
   "metadata": {},
   "source": [
    "Al igual que \"Género\" antes, usé random.choices() pero sin pesos porque este atributo se puede dividir aleatoriamente entre las dos opciones."
   ]
  },
  {
   "cell_type": "markdown",
   "id": "fd9b2e7f",
   "metadata": {},
   "source": [
    "**Name**"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "f5a065c3",
   "metadata": {},
   "source": [
    "Aquí usé la biblioteca Faker para crear miles de nombres para todos estos usuarios. **La biblioteca Faker es excelente en esta situación porque tiene una opción para nombres masculinos y femeninos.**}} Para procesar los nombres de género, creé una función para asignar nombres en función de un género determinado."
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 16,
   "id": "b3fd6f7f",
   "metadata": {},
   "outputs": [],
   "source": [
    "# Instantiating faker\n",
    "faker = Faker()\n",
    "\n",
    "def name_gen(gender):\n",
    "    \"\"\"\n",
    "    Quickly generates a name based on gender\n",
    "    \"\"\"\n",
    "    if gender=='male':\n",
    "        return faker.name_male()\n",
    "    elif gender=='female':\n",
    "        return faker.name_female()\n",
    "    \n",
    "    return faker.name()# Generating names for each user\n",
    "df['name'] = [name_gen(i) for i in df['gender']]"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "fbbe6fc8",
   "metadata": {},
   "source": [
    "Usé mi función simple para producir rápidamente una lista de nombres basada en los datos del atributo \"Género\" antes y la asigné al marco de datos."
   ]
  },
  {
   "cell_type": "markdown",
   "id": "4ae541de",
   "metadata": {},
   "source": [
    "**Email**"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "e81f6c90",
   "metadata": {},
   "source": [
    "El correo electrónico resultó ser uno de los atributos más complicados. Quería crear direcciones de correo electrónico relacionadas con los nombres generados. Sin embargo, probablemente habría una posibilidad de duplicación porque las personas pueden compartir el mismo nombre pero no el mismo correo electrónico.\n",
    "\n",
    "Primero, creé una nueva función que daría formato a los nombres en direcciones de correo electrónico con un nombre de dominio predeterminado. También manejaría direcciones duplicadas simplemente agregando un número aleatorio al final del nombre formateado:"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 17,
   "id": "670b3855",
   "metadata": {},
   "outputs": [],
   "source": [
    "def emailGen(name, duplicateFound=False):\n",
    "    \"\"\"\n",
    "    Generates a random email address based on the given name. \n",
    "    Adds a number at the end if a duplicate address was found.\n",
    "    \"\"\"\n",
    "    # Fake domain name to use\n",
    "    dom = \"@fakemail.com\"\n",
    "    \n",
    "    # Lowercasing and splitting\n",
    "    name = name.lower().split(\" \")\n",
    "    \n",
    "    # Random character to insert in the name\n",
    "    chars = [\".\", \"_\"]\n",
    "    \n",
    "    new_name = name[0] + random.choice(chars) + name[1] \n",
    "    \n",
    "    # Further distinguishing the email if a duplicate was found\n",
    "    if duplicateFound:\n",
    "        \n",
    "        # Random number to insert at the end\n",
    "        num = random.randint(0,100)\n",
    "        \n",
    "        # Inserting at the end\n",
    "        new_name = new_name + str(num)\n",
    "        \n",
    "    # Returning the email address with the domain name attached\n",
    "    return new_name + dom"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "c488a9f8",
   "metadata": {},
   "source": [
    "Ahora, para aprovechar adecuadamente el propósito de esta función, creé un ciclo que volvería a ejecutar la función cuando fuera necesario mientras iteraba a través del atributo \"Nombre\". El ciclo seguiría volviendo a ejecutar la función hasta que se creara un nombre de correo electrónico único."
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 20,
   "id": "97cd6b45",
   "metadata": {},
   "outputs": [],
   "source": [
    "emails = []\n",
    "\n",
    "for name in df['name']:\n",
    "    \n",
    "    # Generating the email\n",
    "    email = emailGen(name)\n",
    "    \n",
    "    # Looping until a unique email is generated\n",
    "    while email in emails:\n",
    "        \n",
    "        # Creating an email with a random number\n",
    "        email = emailGen(name, duplicateFound=True)\n",
    "    \n",
    "    # Attaching the new email to the list\n",
    "    emails.append(email)\n",
    "    \n",
    "df['email'] = emails"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "813169e8",
   "metadata": {},
   "source": [
    "Después de generar todos los correos electrónicos, los asigné al atributo \"Correo electrónico\" del marco de datos. También puede hacer una verificación opcional para ver que cada correo electrónico sea único con el mismo método que las ID."
   ]
  },
  {
   "cell_type": "markdown",
   "id": "1ecb641a",
   "metadata": {},
   "source": [
    "**Last Login**"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "175d145c",
   "metadata": {},
   "source": [
    "Este atributo ahora requiere un formato específico que se hizo más fácil con la utilización de la biblioteca de fecha y hora. Aquí quería que los usuarios tuvieran un historial de inicio de sesión durante el último mes más o menos. Usé otra función personalizada para ayudar:"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 21,
   "id": "8d954a24",
   "metadata": {},
   "outputs": [],
   "source": [
    "def randomtimes(start, end, n):\n",
    "    \"\"\"\n",
    "    Generates random time stamps based on a given amount between two time periods.\n",
    "    \"\"\"\n",
    "    # The timestamp format\n",
    "    frmt = \"%Y-%m-%d %H:%M:%S\"\n",
    "    \n",
    "    # Formatting the two time periods\n",
    "    stime = datetime.datetime.strptime(start, frmt)\n",
    "    etime = datetime.datetime.strptime(end, frmt)\n",
    "    \n",
    "    # Creating the pool for random times\n",
    "    td = etime - stime\n",
    "    \n",
    "    # Generating a list with the random times\n",
    "    times = [(random.random() * td + stime).strftime(frmt) for _ in range(n)]\n",
    "    \n",
    "    return times\n",
    "\n",
    "# Setting the start and end times\n",
    "start = \"2021-08-01 00:00:00\"\n",
    "\n",
    "end = \"2021-08-24 00:00:00\"\n",
    "\n",
    "df['last_login'] = randomtimes(start, end, num_users)"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "fb2b963d",
   "metadata": {},
   "source": [
    "La función básicamente genera una lista de marcas de tiempo entre dos horas dadas. Generó una lista de marcas de tiempo aleatorias para asignar al marco de datos."
   ]
  },
  {
   "cell_type": "markdown",
   "id": "cc8905e5",
   "metadata": {},
   "source": [
    "**Date of Birth**"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "f2cba8d5",
   "metadata": {},
   "source": [
    "Este atributo es fácil ya que es similar a \"Último inicio de sesión\". Todo lo que hice fue cambiar el formato de la hora eliminando la hora, los minutos y los segundos. Usé datetime nuevamente para ayudar a elegir aleatoriamente una fecha para cada usuario, pero esta vez el rango de tiempo comenzó desde 1980 hasta 2006 para obtener una buena distribución aleatoria de edades. El siguiente código es prácticamente el mismo que antes, pero con un formato y un intervalo de fechas diferentes:"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 23,
   "id": "07a97010",
   "metadata": {},
   "outputs": [],
   "source": [
    "def random_dob(start, end, n):\n",
    "    \"\"\"\n",
    "    Generating a list of a set number of timestamps\n",
    "    \"\"\"\n",
    "    \n",
    "    # The timestamp format\n",
    "    frmt = \"%Y-%m-%d\"\n",
    "    \n",
    "    # Formatting the two time periods\n",
    "    stime = datetime.datetime.strptime(start, frmt)\n",
    "    etime = datetime.datetime.strptime(end, frmt)\n",
    "    \n",
    "    # Creating the pool for random times\n",
    "    td = etime - stime\n",
    "    \n",
    "    # Generating a list with the random times\n",
    "    times = [(random.random() * td + stime).strftime(frmt) for _ in range(n)]\n",
    "    \n",
    "    return times\n",
    "\n",
    "df['dob'] = random_dob(\"1980-01-01\", \"2006-01-01\", num_users)"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "a2ee2109",
   "metadata": {},
   "source": [
    "**Education**"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "5aec2aa8",
   "metadata": {},
   "source": [
    "El atributo \"educación\" depende de \"dob\". En estos casos, el nivel de educación se basa en la edad del usuario y no en el nivel de educación más alto que alcanzó. Este es otro de esos atributos en los que elegir aleatoriamente un nivel de educación no reflejaría las tendencias del mundo real.\n",
    "\n",
    "Creé otra función simple que verifica la edad de un usuario según la fecha de hoy y devuelve su nivel de educación actual."
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 24,
   "id": "340b8f4b",
   "metadata": {},
   "outputs": [],
   "source": [
    "def getEducation(dob):\n",
    "    \"\"\"\n",
    "    Assigns an education level based on the given date of birth\n",
    "    \"\"\"\n",
    "    # Current date\n",
    "    now = datetime.datetime.now()\n",
    "    \n",
    "    # Date of birth\n",
    "    dob = datetime.datetime.strptime(dob, \"%Y-%m-%d\")\n",
    "    \n",
    "    # Subtracting the times to get an age\n",
    "    age = int((now - dob).days/365.25)\n",
    "    \n",
    "    # Returning education level based on age\n",
    "    if age <= 18:\n",
    "        return 'high school'\n",
    "    elif age <= 22:\n",
    "        return 'undergrad'\n",
    "    elif age <= 25:\n",
    "        return 'grad'\n",
    "    else:\n",
    "        return 'employed'\n",
    "\n",
    "df['education'] = [getEducation(i) for i in df['dob']]"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "b1570a1c",
   "metadata": {},
   "source": [
    "Después de generar una lista de niveles de educación, la asigné al marco de datos."
   ]
  },
  {
   "cell_type": "markdown",
   "id": "59c8665b",
   "metadata": {},
   "source": [
    "**Bio**"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "7802fa7e",
   "metadata": {},
   "source": [
    "Para este atributo, quería variar la longitud de la biografía según el estado de suscripción del usuario. Si un usuario fuera un suscriptor, asumiría que sus biografías serían más largas que las de los no suscriptores.\n",
    "\n",
    "Para dar cabida a este aspecto, construí una función que verifica su estado de suscripción y devuelve una oración aleatoria de Faker que varía en longitud."
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 25,
   "id": "8889cfa6",
   "metadata": {},
   "outputs": [],
   "source": [
    "def makeBio(subscriber):\n",
    "    \"\"\"\n",
    "    Making a short or long bio depending their subscription status.\n",
    "    \"\"\"\n",
    "    \n",
    "    if subscriber==True:\n",
    "        \n",
    "        # Randomizing bio length but skewed towards longer bios\n",
    "        bio_len = random.choices([10,20], weights=(10,90), k=1)[0]\n",
    "        \n",
    "    elif subscriber==False:\n",
    "        \n",
    "        # Randomizing bio length but skewed towards shorter bios\n",
    "        bio_len = random.choices([1,3], weights=(10,90), k=1)[0]\n",
    "        \n",
    "    return faker.sentence(bio_len)\n",
    "    \n",
    "\n",
    "df['bio'] = [makeBio(i) for i in df['subscriber']]"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "153d8103",
   "metadata": {},
   "source": [
    "En la función anterior, elegí aleatoriamente la longitud de las oraciones falsas según el estado de la suscripción. Si eran suscriptores, sus biografías tendían a ser más largas de lo habitual y viceversa."
   ]
  },
  {
   "cell_type": "markdown",
   "id": "ca9a071a",
   "metadata": {},
   "source": [
    "**Rating**"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "3e128c96",
   "metadata": {},
   "source": [
    "Para completar este conjunto de datos, quería incluir un tipo de datos numérico. Elegí \"calificación\" para que sea de tipo entero. La calificación de 1 a 5 representa cualquier cosa y solo está ahí para cualquier propósito discrecional.\n",
    "\n",
    "Para las calificaciones en sí, opté por sesgar la distribución de 1 a 5 hacia los extremos para reflejar la tendencia de los usuarios a ser aparentemente más absolutos con sus calificaciones."
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 26,
   "id": "924d3e68",
   "metadata": {},
   "outputs": [],
   "source": [
    "# The different ratings available\n",
    "ratings = [1,2,3,4,5]# Weighted ratings with a skew towards the ends\n",
    "df['rating'] = random.choices(\n",
    "    ratings, \n",
    "    weights=(30,10,10,10,30), \n",
    "    k=num_users\n",
    ")"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "b15041c3",
   "metadata": {},
   "source": [
    "Usé la función random.choices() una vez más pero con los pesos sesgados hacia 1 y 5."
   ]
  },
  {
   "cell_type": "markdown",
   "id": "545e8963",
   "metadata": {},
   "source": [
    "**Saving the Dataset**"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "743e5aed",
   "metadata": {},
   "source": [
    "Ahora que los datos están completos y si estaba codificando, siéntase libre de ver el marco de datos antes de decidir guardarlo. Si todo se ve bien, guarde el marco de datos como un archivo .csv con este simple comando:"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 28,
   "id": "b746f91d",
   "metadata": {},
   "outputs": [],
   "source": [
    "df.to_csv('dataset_users.csv')"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 0,
   "id": "ea5400f3",
   "metadata": {},
   "outputs": [],
   "source": []
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3 (ipykernel)",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.9.7"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 5
}