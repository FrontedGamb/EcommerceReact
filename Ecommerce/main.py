from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

# Configuración de CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:5173", "http://localhost:5174","http://localhost:5175"],
    allow_credentials=True,
    allow_methods=["GET", "POST", "PUT", "DELETE"],
    allow_headers=["*"],
)


@app.get("/api/products")
def products():
    return [
        {
            "id": 0,
            "categoryName": "Clothes",
             "description": "Esta blusa sin mangas presenta un diseño moderno con colores azul y blanco. Es perfecta para lucir elegante y cómoda en cualquier ocasión. Está confeccionada con materiales de alta calidad y su estilo versátil la hace combinable con diferentes prendas.",
            "categoryId": 1,
            "title": "Blusa Sin Mangas Azul Y Blanca",
            "image": "https://images.pexels.com/photos/2850487/pexels-photo-2850487.jpeg?auto=compress&cs=tinysrgb&w=1260&h=750&dpr=1",
            "price": 1000,
            
        },
        {
            "id": 1,
            "categoryName": "Clothes",
            "categoryId": 1,
            "title": "Bolso Bandolera De Cuero Amarillo Y Negro",
            "image": "https://images.pexels.com/photos/2002717/pexels-photo-2002717.jpeg?auto=compress&cs=tinysrgb&w=1260&h=750&dpr=1",
            "price": 700,
            "description": ": Este bolso bandolera combina el estilo y la funcionalidad. Confeccionado con cuero de alta calidad, presenta un diseño moderno en colores amarillo y negro. Es ideal para llevar tus objetos personales de manera segura y con estilo."
        },
        {
            "id": 2,
            "categoryName": "Clothes",
            "categoryId": 1,
            "title": "Jeans Azules",
            "image": "https://images.pexels.com/photos/1082528/pexels-photo-1082528.jpeg?auto=compress&cs=tinysrgb&w=1260&h=750&dpr=1",
            "price": 400
        },
        {
            "id": 3,
            "categoryName": "Clothes",
            "categoryId": 1,
            "title": "Sueteres de colores",
            "image": "https://images.pexels.com/photos/3812433/pexels-photo-3812433.jpeg?auto=compress&cs=tinysrgb&w=1260&h=750&dpr=1",
            "price": 200,
             "description":"Estos suéteres de colores vibrantes te mantendrán abrigado/a y a la moda durante la temporada de invierno. Confeccionados con materiales suaves y cálidos, son perfectos para combinar con tus pantalones o faldas favoritas.",
        },
        {
            "id": 4,
            "categoryName": "Clothes",
            "categoryId": 1,
            "title": "Gorra Nike Roja Y Negra Entallada",
            "image": "https://images.pexels.com/photos/1124465/pexels-photo-1124465.jpeg?auto=compress&cs=tinysrgb&w=1260&h=750&dpr=1",
            "price": 200,
             "description":"Esta gorra entallada de Nike en colores rojo y negro te brinda protección solar y estilo deportivo. Confeccionada con materiales de alta calidad, cuenta con el logotipo distintivo de Nike en la parte frontal. Es ideal para complementar tu outfit deportivo o casual."
        },
        {
            "id": 5,
            "categoryName": "Clothes",
            "categoryId": 1,
            "title": "Zapatillas Nike Rojas Y Negras",
            "image": "https://images.pexels.com/photos/786003/pexels-photo-786003.jpeg?auto=compress&cs=tinysrgb&w=1260&h=750&dpr=1",
            "price": 200,
            "description":"Estas zapatillas Nike en colores rojo y negro combinan estilo y comodidad. Confeccionadas con materiales transpirables y suela de goma resistente, ofrecen un ajuste óptimo y amortiguación para tus actividades diarias o deportivas"
        },
        {
            "id": 6,
            "categoryName": "Clothes",
            "categoryId": 1,
            "title": "Zapatillas Nike Blancas y negras",
            "image": "https://images.pexels.com/photos/1698359/pexels-photo-1698359.jpeg",
            "price": 300,
            "description":"Estas zapatillas Puma son perfectas para los amantes del deporte y el estilo urbano. Confeccionadas con materiales de calidad y tecnología de amortiguación, brindan comodidad y soporte durante tus actividades físicas. Su diseño moderno en colores llamativos las convierte en un accesorio de moda versátil."
            
        },
        {
            "id": 7,
            "categoryName": "Clothes",
            "categoryId": 1,
            "title": "Zapatillas Puma",
            "image": "https://images.pexels.com/photos/2759783/pexels-photo-2759783.jpeg?auto=compress&cs=tinysrgb&w=1260&h=750&dpr=1",
            "price": 500,
             "description":"Estas zapatillas Puma son perfectas para los amantes del deporte y el estilo urbano. Confeccionadas con materiales de calidad y tecnología de amortiguación, brindan comodidad y soporte durante tus actividades físicas. Su diseño moderno en colores llamativos las convierte en un accesorio de moda versátil."
        },
        {
            "id": 8,
            "categoryName": "Clothes",
            "categoryId": 1,
            "title": "Jordan 1 Naranjas",
            "image": "https://images.pexels.com/photos/12010216/pexels-photo-12010216.jpeg?auto=compress&cs=tinysrgb&w=1260&h=750&dpr=1",
            "price": 400,
            "description":" Estas zapatillas Jordan 1 en color naranja son un ícono de estilo y rendimiento. Confeccionadas con materiales de alta calidad y una silueta clásica, brindan comodidad y estilo urbano. Son ideales para los amantes del baloncesto y los seguidores de la marca Jordan."
        },
        {
            "id": 9,
            "categoryName": "Clothes",
            "categoryId": 1,
            "title": "Jordan 1 grises",
            "image": "https://images.pexels.com/photos/345415/pexels-photo-345415.jpeg?auto=compress&cs=tinysrgb&w=1260&h=750&dpr=1",
            "price": 350,
             "description":" Estas zapatillas Jordan 1 en color naranja son un ícono de estilo y rendimiento. Confeccionadas con materiales de alta calidad y una silueta clásica, brindan comodidad y estilo urbano. Son ideales para los amantes del baloncesto y los seguidores de la marca Jordan."
        },
        {
            "id": 10,
            "categoryName": "Electronics",
            "categoryId": 2,
            "title": "Corneta JBL",
            "image": "https://images.pexels.com/photos/15684881/pexels-photo-15684881/free-photo-of-hombre-brazo-mano-tecnologia.jpeg?auto=compress&cs=tinysrgb&w=1260&h=750&dpr=1",
            "price": 150,
            "description":"  La corneta JBL es un altavoz portátil que ofrece un sonido potente y de alta calidad. Con su diseño compacto y elegante, puedes llevarla contigo a cualquier lugar y disfrutar de tu música favorita con una excelente calidad de audio. Además, cuenta con tecnología inalámbrica para que puedas conectarla fácilmente a tus dispositivos."
        },
        {
            "id": 11,
            "categoryName": "Electronics",
            "categoryId": 2,
            "title": "Silver Imac",
            "image": "https://images.pexels.com/photos/1779487/pexels-photo-1779487.jpeg?auto=compress&cs=tinysrgb&w=1260&h=750&dpr=1",
            "price": 750,
            "description":"El iMac plateado es una computadora todo-en-uno de Apple que combina rendimiento y elegancia. Con su diseño delgado y minimalista, esta poderosa máquina ofrece una experiencia de usuario fluida y eficiente. Con una pantalla de alta resolución y potentes componentes internos, el iMac es perfecto para el trabajo creativo, el entretenimiento y mucho más."
        },
        {
            "id": 12,
            "categoryName": "Electronics",
            "categoryId": 2,
            "title": "Dron",
            "image": "https://images.pexels.com/photos/15825389/pexels-photo-15825389/free-photo-of-tecnologia-rock-dispositivo-artilugio.jpeg?auto=compress&cs=tinysrgb&w=1260&h=750&dpr=1",
            "price": 350,
            "description":"Este dron te permite explorar el mundo desde una perspectiva única. Con su sistema de vuelo estable y cámara integrada, puedes capturar impresionantes imágenes aéreas y grabar videos de alta calidad. Además, cuenta con funciones avanzadas como seguimiento de objetos y modos de vuelo preprogramados para una experiencia de vuelo emocionante y controlada."
        },
        {
            "id": 13,
            "categoryName": "Electronics",
            "categoryId": 2,
            "title": "Iphone X Plateado Con Airpods",
            "image": "https://images.pexels.com/photos/788946/pexels-photo-788946.jpeg?auto=compress&cs=tinysrgb&w=1260&h=750&dpr=1",
            "price": 250,
            "description": " El iPhone X es un teléfono inteligente de última generación con un diseño elegante y funciones avanzadas. Viene en un llamativo color plateado e incluye los populares AirPods para disfrutar de una experiencia auditiva inalámbrica. Con su potente rendimiento y pantalla de alta resolución, el iPhone X te brinda acceso a una amplia gama de aplicaciones y características innovadoras."
        },
        {
            "id": 14,
            "categoryName": "Electronics",
            "categoryId": 2,
            "title": "Iphone 7",
            "image": "https://images.pexels.com/photos/699122/pexels-photo-699122.jpeg?auto=compress&cs=tinysrgb&w=1260&h=750&dpr=1",
            "price": 150,
            "description": "El iPhone 7 es un teléfono inteligente icónico que combina funcionalidad y estilo. Con su diseño elegante y construcción de alta calidad, este dispositivo ofrece un rendimiento rápido y confiable. Además, cuenta con una cámara de alta resolución, pantalla brillante y una amplia gama de características y aplicaciones para satisfacer todas tus necesidades diarias."
        },
        {
            "id": 15,
            "categoryName": "Electronics",
            "categoryId": 2,
            "title": "Control Xbox 360",
            "image": "https://images.pexels.com/photos/1298601/pexels-photo-1298601.jpeg?auto=compress&cs=tinysrgb&w=1260&h=750&dpr=1",
            "price": 50,
             "description":"El control Xbox 360 es el accesorio perfecto para los amantes de los videojuegos. Con su diseño ergonómico y botones sensibles, te brinda un control preciso durante tus sesiones de juego. Conéctalo a tu consola Xbox 360 y disfruta de una experiencia de juego inmersiva y emocionante."
        },
        {
            "id": 16,
            "categoryName": "Electronics",
            "categoryId": 2,
            "title": "Macbook Air",
            "image": "https://images.pexels.com/photos/812264/pexels-photo-812264.jpeg?auto=compress&cs=tinysrgb&w=1260&h=750&dpr=1",
            "price": 500,
             "description": "El MacBook Air es una computadora portátil ligera y potente que combina rendimiento y portabilidad. Con su diseño delgado y elegante, es ideal para aquellos que necesitan trabajar o entretenerse sobre la marcha. Equipado con un procesador rápido, una pantalla de alta resolución y una larga duración de batería, el MacBook Air te ofrece un rendimiento excepcional en cualquier lugar."
        },
        {
            "id": 18,
            "categoryName": "Electronics",
            "categoryId": 2,
            "title": "Control ps4",
            "image": "https://images.pexels.com/photos/459762/pexels-photo-459762.jpeg?auto=compress&cs=tinysrgb&w=1260&h=750&dpr=1",
            "price": 50,
            "description": " El control PS4 es el mando oficial de la consola PlayStation 4. Con su diseño ergonómico y botones sensibles, te brinda una experiencia de juego cómoda y precisa. Conéctalo a tu consola PS4 y sumérgete en tus juegos favoritos con un control total."
        },
        {
            "id": 19,
            "categoryName": "Electronics",
            "categoryId": 2,
            "title": "Control ps2",
            "image": "https://images.pexels.com/photos/1579240/pexels-photo-1579240.jpeg?auto=compress&cs=tinysrgb&w=1260&h=750&dpr=1",
            "price": 25,
             "description":"El control PS2 es el mando clásico de la consola PlayStation 2. Con su diseño icónico y botones intuitivos, te permite disfrutar de tus juegos retro de la PS2 con autenticidad. Conéctalo a tu consola y revive la nostalgia de los videojuegos de antaño."
        },
        {
            "id": 20,
            "categoryName": "Electronics",
            "categoryId": 2,
            "title": "Auriculares Inalambricos",
            "image": "https://images.pexels.com/photos/3394650/pexels-photo-3394650.jpeg?auto=compress&cs=tinysrgb&w=1260&h=750&dpr=1",
            "price": 75,
            "description": "Estos auriculares inalámbricos te brindan libertad y comodidad mientras disfrutas de tu música favorita. Conecta los auriculares a tu dispositivo mediante Bluetooth y disfruta de un sonido envolvente y de alta calidad. Además, su diseño ergonómico y liviano los hace ideales para uso diario o actividades deportivas. Con una batería duradera, puedes disfrutar de horas de reproducción sin interrupciones."
        },
        {
            "id": 21,
            "categoryName": "Furniture",
            "categoryId": 3,
            "title": "Sofá De 2 Plazas De Cuero",
            "image": "https://images.pexels.com/photos/1866149/pexels-photo-1866149.jpeg?auto=compress&cs=tinysrgb&w=1260&h=750&dpr=1",
            "price": 90,
             "description":"Este sofá seccional de tela negra es ideal para espacios modernos y contemporáneos. Con su diseño modular y versátil, puedes adaptarlo a la configuración que mejor se ajuste a tu sala de estar. La tela de alta calidad y los cojines suaves te brindan comodidad y durabilidad a largo plazo."
        },
        {
            "id": 22,
            "categoryName": "Furniture",
            "categoryId": 3,
            "title": "Sofá Seccional De Tela Negra",
            "image": "https://images.pexels.com/photos/276583/pexels-photo-276583.jpeg?auto=compress&cs=tinysrgb&w=1260&h=750&dpr=1",
            "price": 120,
            "description":" Este sofá seccional de tela negra es ideal para espacios modernos y contemporáneos. Con su diseño modular y versátil, puedes adaptarlo a la configuración que mejor se ajuste a tu sala de estar. La tela de alta calidad y los cojines suaves te brindan comodidad y durabilidad a largo plazo."
        },
        {
            "id": 23,
            "categoryName": "Furniture",
            "categoryId": 3,
            "title": "Aparador De Madera Gris",
            "image": "https://images.pexels.com/photos/271816/pexels-photo-271816.jpeg?auto=compress&cs=tinysrgb&w=1260&h=750&dpr=1",
            "price": 60,
            "description":"Este aparador de madera gris es una pieza funcional y estilizada para tu comedor o sala de estar. Con su diseño elegante y acabado en gris, agrega un toque de sofisticación a cualquier espacio. Cuenta con amplio espacio de almacenamiento, ideal para guardar vajillas, utensilios u otros elementos."
        },
        {
            "id": 24,
            "categoryName": "Furniture",
            "categoryId": 3,
            "title": "Cojines",
            "image": "https://images.pexels.com/photos/1248583/pexels-photo-1248583.jpeg?auto=compress&cs=tinysrgb&w=1260&h=750&dpr=1",
            "price": 10,
             "description":"Cojines comodos para recostar tu cabeza en los mejores momentos"
        },
        {
            "id": 25,
            "categoryName": "Furniture",
            "categoryId": 3,
            "title": "Taburete De Bar Redondo Rojo",
            "image": "https://images.pexels.com/photos/2180883/pexels-photo-2180883.jpeg?auto=compress&cs=tinysrgb&w=1260&h=750&dpr=1",
            "price": 22,
            "description":"Este taburete de bar redondo en color rojo agrega un toque vibrante y moderno a tu cocina o bar. Con su asiento cómodo y base resistente, proporciona comodidad y estabilidad mientras disfrutas de tus comidas o bebidas. Su diseño compacto y elegante lo hace adecuado para espacios reducidos."
        },
        {
            "id": 26,
            "categoryName": "Furniture",
            "categoryId": 3,
            "title": "Sofá Gris",
            "image": "https://images.pexels.com/photos/1631918/pexels-photo-1631918.jpeg?auto=compress&cs=tinysrgb&w=1260&h=750&dpr=1",
            "price": 46,
             "description":"Este sofá gris es una opción versátil para cualquier sala de estar. Con su diseño contemporáneo y tono neutro, se adapta fácilmente a diferentes estilos de decoración. El sofá ofrece asientos cómodos y un respaldo acolchado para momentos de relajación y entretenimiento."
        },
        {
            "id": 27,
            "categoryName": "Furniture",
            "categoryId": 3,
            "title": "Toalla Gris",
            "image": "https://images.pexels.com/photos/4210372/pexels-photo-4210372.jpeg?auto=compress&cs=tinysrgb&w=1260&h=750&dpr=1",
            "price": 6,
            "description":" Esta toalla gris es suave y absorbente, perfecta para el uso diario en el baño o la playa. Con su tejido de alta calidad, proporciona una sensación lujosa y se seca rápidamente. Su color gris neutro le da un toque de elegancia y combina con cualquier estilo de decoración."
        },
        {
            "id": 28,
            "categoryName": "Furniture",
            "categoryId": 3,
            "title": "Sillón De Mimbre Blanco ",
            "image": "https://images.pexels.com/photos/3705539/pexels-photo-3705539.jpeg?auto=compress&cs=tinysrgb&w=1260&h=750&dpr=1",
            "price": 32,
             "description":"Este sillón de mimbre blanco agrega un toque de encanto y calidez a tu espacio exterior o interior. Con su diseño de mimbre trenzado y cojín suave, proporciona comodidad y estilo. Disfruta de momentos de relajación mientras te balanceas suavemente en este acogedor sillón."
        },
        {
            "id": 29,
            "categoryName": "Furniture",
            "categoryId": 3,
            "title": "Mesa Redonda Blanca Y Negra",
            "image": "https://images.pexels.com/photos/6198655/pexels-photo-6198655.jpeg?auto=compress&cs=tinysrgb&w=1260&h=750&dpr=1",
            "price": 22,
            "description":" Esta mesa redonda en blanco y negro es una opción moderna y elegante para tu comedor o sala de estar. Con su superficie espaciosa y patas robustas, ofrece un espacio perfecto para reuniones y comidas familiares. Su combinación de colores añade un toque visual interesante a tu espacio."
        },
        {
            "id": 30,
            "categoryName": "Furniture",
            "categoryId": 3,
            "title": "Estante De Madera Marrón",
            "image": "https://images.pexels.com/photos/2086676/pexels-photo-2086676.jpeg?auto=compress&cs=tinysrgb&w=1260&h=750&dpr=1",
            "price": 45,
            "description": "Este estante de madera marrón es una solución práctica y estilizada para organizar tus libros, decoraciones y otros objetos en tu hogar. Con su diseño moderno y acabado en madera natural, se adapta a diferentes estilos de decoración. Sus estantes espaciosos te permiten exhibir y almacenar tus pertenencias de forma ordenada."
        },
        {
            "id": 31,
            "categoryName": "Toys",
            "categoryId": 4,
            "title": "Figuras De Super Mario, Luigi Y Yoshi",
            "image": "https://images.pexels.com/photos/163036/mario-luigi-yoschi-figures-163036.jpeg?auto=compress&cs=tinysrgb&w=1260&h=750&dpr=1",
            "price": 10,
            "description":"Estas figuras de Super Mario, Luigi y Yoshi son perfectas para los amantes de los videojuegos. Revive las aventuras del mundo de Super Mario con estas figuras detalladas. Cada figura está hecha de material duradero y cuenta con colores vibrantes que capturan la esencia de los personajes."
        },
        {
            "id": 32,
            "categoryName": "Toys",
            "categoryId": 4,
            "title": "Spin Top Multicolor",
            "image": "https://images.pexels.com/photos/158838/pexels-photo-158838.jpeg?auto=compress&cs=tinysrgb&w=1260&h=750&dpr=1",
            "price": 1.5,
             "description":" Este trompo multicolor es un juguete clásico que proporciona horas de diversión. Con su diseño colorido y asa resistente, puedes girarlo y verlo dar vueltas rápidamente. Practica tus habilidades de equilibrio y disfruta de la emoción de hacerlo girar durante mucho tiempo."
        },
        {
            "id": 33,
            "categoryName": "Toys",
            "categoryId": 4,
            "title": "Cubo De Rubik ",
            "image": "https://images.pexels.com/photos/19677/pexels-photo.jpg?auto=compress&cs=tinysrgb&w=1260&h=750&dpr=1",
            "price": 7,
            "description": "El cubo de Rubik es un rompecabezas desafiante que ha entretenido a personas de todas las edades durante décadas. Con sus colores brillantes y superficie giratoria suave, este cubo te desafiará a resolver sus diferentes capas y a poner a prueba tu destreza mental."
        },
        {
            "id": 34,
            "categoryName": "Toys",
            "categoryId": 4,
            "title": "Fidget Tri Spinner Amarillo",
            "image": "https://images.pexels.com/photos/1330638/pexels-photo-1330638.jpeg?auto=compress&cs=tinysrgb&w=1260&h=750&dpr=1",
            "price": 2,
            "description":"Este Fidget Tri Spinner amarillo es un juguete antiestrés que te ayuda a mantener las manos ocupadas y a aliviar el estrés. Con su diseño compacto y aspas suaves, puedes girarlo rápidamente con tus dedos y disfrutar de la sensación de relajación y concentración."
        },
        {
            "id": 35,
            "categoryName": "Toys",
            "categoryId": 4,
            "title": "Coche Modelo A Escala Verde",
            "image": "https://images.pexels.com/photos/35967/mini-cooper-auto-model-vehicle.jpg?auto=compress&cs=tinysrgb&w=1260&h=750&dpr=1",
            "price": 16,
             "description":"Este coche modelo a escala verde es perfecto para los entusiastas de los automóviles. Con su diseño detallado y acabado en color verde vibrante, captura la esencia de los coches deportivos. Es un excelente artículo de colección o un regalo para los amantes de los vehículos."
        },
        {
            "id": 36,
            "categoryName": "Toys",
            "categoryId": 4,
            "title": "Juguete Wall E ",
            "image": "https://images.pexels.com/photos/2103864/pexels-photo-2103864.jpeg?auto=compress&cs=tinysrgb&w=1260&h=750&dpr=1",
            "price": 12,
            "description": "Este juguete de Wall E está inspirado en el popular personaje de la película de animación. Con su diseño adorable y detalles realistas, este juguete te permitirá recrear las aventuras de Wall E en tu propia casa. Es un regalo perfecto para los fans de la película."
        },
        {
            "id": 37,
            "categoryName": "Toys",
            "categoryId": 4,
            "title": "Avion Amarillo",
            "image": "https://images.pexels.com/photos/243167/pexels-photo-243167.jpeg?auto=compress&cs=tinysrgb&w=1260&h=750&dpr=1",
            "price": 12,
            "description":" Este avión amarillo es un juguete clásico que despierta la imaginación de los niños. Con su diseño aerodinámico y colores brillantes, este avión te permitirá volar alto en tus juegos imaginarios. Su tamaño y forma son ideales para que los niños lo sostengan y jueguen con él."
        },
        {
            "id": 38,
            "categoryName": "Toys",
            "categoryId": 4,
            "title": "Peluche Pájaro Azul",
            "image": "https://images.pexels.com/photos/1364562/pexels-photo-1364562.jpeg?auto=compress&cs=tinysrgb&w=1260&h=750&dpr=1",
            "price": 14,
            "description": "Este peluche de pájaro azul es suave y adorable. Con su plumaje azul brillante y ojos expresivos, este peluche te brindará compañía y confort. Su tamaño compacto lo hace perfecto para abrazar y llevar contigo a todas partes."
        },
        {
            "id": 39,
            "categoryName": "Toys",
            "categoryId": 4,
            "title": "Volkswagen Rojo",
            "image": "https://images.pexels.com/photos/772393/pexels-photo-772393.jpeg?auto=compress&cs=tinysrgb&w=1260&h=750&dpr=1",
            "price":   19,
            "description":"Este modelo a escala de un Volkswagen rojo es un regalo ideal para los amantes de los coches clásicos. Con su diseño detallado y acabado en color rojo llamativo, captura la esencia de este icónico automóvil. Es un artículo de colección perfecto o un juguete para los aficionados a los coches."
        },
        {
            "id": 40,
            "categoryName": "Others",
            "categoryId": 5,
            "title": "Pelota de baloncesto",
            "image": "https://images.pexels.com/photos/1462618/pexels-photo-1462618.jpeg?auto=compress&cs=tinysrgb&w=1260&h=750&dpr=1",
            "price": 30,
             "description":"Este modelo a escala de un Volkswagen rojo es un regalo ideal para los amantes de los coches clásicos. Con su diseño detallado y acabado en color rojo llamativo, captura la esencia de este icónico automóvil. Es un artículo de colección perfecto o un juguete para los aficionados a los coches."
        },
        {
            "id": 42,
            "categoryName": "Others",
            "categoryId": 5,
            "title": "Despertador De Anillo Blanco",
            "image": "https://images.pexels.com/photos/2277923/pexels-photo-2277923.jpeg?auto=compress&cs=tinysrgb&w=1260&h=750&dpr=1",
            "price": 10,
             "description":"Este modelo a escala de un Volkswagen rojo es un regalo ideal para los amantes de los coches clásicos. Con su diseño detallado y acabado en color rojo llamativo, captura la esencia de este icónico automóvil. Es un artículo de colección perfecto o un juguete para los aficionados a los coches."
        },
        {
            "id": 43,
            "categoryName": "Others",
            "categoryId": 5,
            "title": "Vaso De Café",
            "image": "https://images.pexels.com/photos/2744760/pexels-photo-2744760.jpeg?auto=compress&cs=tinysrgb&w=1260&h=750&dpr=1",
            "price": 4,
             "description":"Este modelo a escala de un Volkswagen rojo es un regalo ideal para los amantes de los coches clásicos. Con su diseño detallado y acabado en color rojo llamativo, captura la esencia de este icónico automóvil. Es un artículo de colección perfecto o un juguete para los aficionados a los coches."
        },
        {
            "id": 44,
            "categoryName": "Others",
            "categoryId": 5,
            "title": "Proyector Rolleiflex De Carrete A Carrete Negro",
            "image": "https://images.pexels.com/photos/821738/pexels-photo-821738.jpeg?auto=compress&cs=tinysrgb&w=1260&h=750&dpr=1",
            "price": 100,
             "description":"Este modelo a escala de un Volkswagen rojo es un regalo ideal para los amantes de los coches clásicos. Con su diseño detallado y acabado en color rojo llamativo, captura la esencia de este icónico automóvil. Es un artículo de colección perfecto o un juguete para los aficionados a los coches."
        },
        {
            "id": 45,
            "categoryName": "Others",
            "categoryId": 5,
            "title": "Colección De Fotos Antiguas Instantáneas Con Viajes",
            "image": "https://images.pexels.com/photos/5653734/pexels-photo-5653734.jpeg?auto=compress&cs=tinysrgb&w=1260&h=750&dpr=1",
            "price": 77,
             "description":"Este modelo a escala de un Volkswagen rojo es un regalo ideal para los amantes de los coches clásicos. Con su diseño detallado y acabado en color rojo llamativo, captura la esencia de este icónico automóvil. Es un artículo de colección perfecto o un juguete para los aficionados a los coches."
        },
        {
            "id": 46,
            "categoryName": "Others",
            "categoryId": 5,
            "title": "Disco De Vinilo Negro Y Gris",
            "image": "https://images.pexels.com/photos/2746823/pexels-photo-2746823.jpeg?auto=compress&cs=tinysrgb&w=1260&h=750&dpr=1",
            "price": 37,
             "description":"Este modelo a escala de un Volkswagen rojo es un regalo ideal para los amantes de los coches clásicos. Con su diseño detallado y acabado en color rojo llamativo, captura la esencia de este icónico automóvil. Es un artículo de colección perfecto o un juguete para los aficionados a los coches."
        },
        {
            "id": 47,
            "categoryName": "Others",
            "categoryId": 5,
            "title": "Pinturas Surtidas",
            "image": "https://images.pexels.com/photos/354939/pexels-photo-354939.jpeg?auto=compress&cs=tinysrgb&w=1260&h=750&dpr=1",
            "price": 27,
             "description":"Este modelo a escala de un Volkswagen rojo es un regalo ideal para los amantes de los coches clásicos. Con su diseño detallado y acabado en color rojo llamativo, captura la esencia de este icónico automóvil. Es un artículo de colección perfecto o un juguete para los aficionados a los coches."
        },
        {
            "id": 48,
            "categoryName": "Others",
            "categoryId": 5,
            "title": "Botellas De Vino Surtidas",
            "image": "https://images.pexels.com/photos/1283219/pexels-photo-1283219.jpeg?auto=compress&cs=tinysrgb&w=1260&h=750&dpr=1",
            "price": 47,
             "description":"Este modelo a escala de un Volkswagen rojo es un regalo ideal para los amantes de los coches clásicos. Con su diseño detallado y acabado en color rojo llamativo, captura la esencia de este icónico automóvil. Es un artículo de colección perfecto o un juguete para los aficionados a los coches."
        },
        {
            "id": 49,
            "categoryName": "Others",
            "categoryId": 5,
            "title": "Botella De Whisky Gallantry",
            "image": "https://images.pexels.com/photos/2529468/pexels-photo-2529468.jpeg?auto=compress&cs=tinysrgb&w=1260&h=750&dpr=1",
            "price": 77,
             "description":"Este modelo a escala de un Volkswagen rojo es un regalo ideal para los amantes de los coches clásicos. Con su diseño detallado y acabado en color rojo llamativo, captura la esencia de este icónico automóvil. Es un artículo de colección perfecto o un juguete para los aficionados a los coches."
        },
    ]
if __name__ == "__main__":
    import uvicorn

    uvicorn.run(app, host="0.0.0.0", port=8888)


