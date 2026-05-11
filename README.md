Patrón Composite

Descripción
El programa permite gestionar una estructura jerárquica de elementos de logística, donde se pueden tratar de la misma manera los paquetes individuales y los contenedores que agrupan múltiples elementos. Esto facilita el cálculo recursivo del peso total de un envío, sin importar qué tan compleja sea su composición.
Los componentes implementados son:
•	PaqueteIndividual (Hoja): Representa un objeto simple con un peso definido. No contiene otros elementos.
•	ContenedorCarga (Compuesto): Representa una caja o contenedor que puede almacenar tanto paquetes individuales como otros contenedores, calculando el peso total de todo su contenido.

Ejecución
Antes de ejecutar el programa, es necesario ubicarse desde la terminal en la carpeta del proyecto. Si la terminal no se encuentra dentro de la carpeta correcta, utilizar el comando:
•	cd ruta_de_descarga\Exposicion-Patrones-de-Disenio-Composite-Decorator-main\EjercicioComposite
Después de ubicarse en la carpeta, ejecutar:
•	EjercicioComposite.py

Ejemplo de salida
Calculando el peso total del cargamento... El peso total de la 'Caja Principal' es: 12.5 kg.Explicación
Sin el patrón Composite, el sistema tendría que verificar constantemente si lo que está procesando es un solo paquete o una caja con más objetos dentro, lo que llenaría el código de condicionales (if/else).
Con Composite, tratamos tanto a los objetos simples como a las agrupaciones bajo una misma interfaz. Esto permite crear estructuras tipo "árbol" tan profundas como sea necesario, haciendo que el sistema sea escalable y fácil de mantener.

Autor
Proyecto realizado por Jesús Jared Morales Tirado

===================================================================================================================================================================
Patrón Decorator

Descripción
Esta parte del proyecto corresponde a la implementación del patrón de diseño Decorator en Python.
El programa permite agregar funcionalidades adicionales a una notificación de manera dinámica, sin modificar directamente la clase principal. En este caso, una notificación simple puede marcarse como urgente y también incluir una firma.
Los decoradores implementados son:
•	DecoradorUrgente: agrega la etiqueta [URGENTE] al mensaje. 
•	DecoradorFirmado: agrega una firma al final de la notificación. 

Ejecución
Antes de ejecutar el programa, es necesario ubicarse desde la terminal en la carpeta del proyecto.
Si la terminal no se encuentra dentro de la carpeta correcta, utilizar el comando:
•	cd ruta_de_descarga\Exposicion-Patrones-de-Disenio-Composite-Decorator-main\EjercicioDecorator
Después de ubicarse en la carpeta, ejecutar:
•	python main.py

Ejemplo de salida
[URGENTE] Servidor caido en produccion — DevOps Team

Explicación
Sin el patrón Decorator sería necesario crear múltiples combinaciones de clases para cada tipo de notificación.
Con Decorator es posible agregar funcionalidades dinámicamente sin modificar la clase original, haciendo el sistema más flexible y reutilizable.
Autor
Proyecto realizado por Ignacio Calixto León
