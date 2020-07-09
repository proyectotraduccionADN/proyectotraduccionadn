# Proyecto traducción ADN
## Sobre el proyecto 
El traductor de ADN se encarga de convertir cadenas de tipo DNAsense, DNAantisense, o RNA a cadenas de tipo DNAsense, DNAantisense, RNA, proteína o proteína simple. El programa consiste en una interfaz bastante fácil de usar.
## Cómo descargar y usar
Los archivos del programa corresponden a: 
- Dos archivos de texto .txt, estos son dos cadenas de DNAsense para que pueda probar el programa si así lo desea.
- Una imagen .png que corresponde al fondo de la interfaz.
- Una carpeta con imágenes que corresponden a la información en el README.md  
- El archivo principal interface.py que contiene todo el código, es en pocas palabras el traductor en si.

Todos los archivos se pueden descargar en un archivo ZIP (en el botón verde que dice "Code").

O puede clonar este repositorio en su equipo usando https://github.com/proyectotraduccionADN/proyectotraduccionadn.git 

Para poder usar el programa es necesario tener instalado Python (recomendamos una versión reciente como 3.8 o 3.7) y además asegurarse que también este instalada la librería Tkinter, la cual es la que permite crear la interfaz gráfica del programa.

Después de descargar todo lo necesario y correr el programa en Python debería aparecer la siguiente pantalla:

<img src="https://github.com/proyectotraduccionADN/proyectotraduccionadn/blob/master/readme%20images/1.jpg">

El programa tiene varias opciones, primero, la cadena de entrada es la cadena que se ingresará en el cuadro central superior y la que se busca convertir a otra cadena, la cual es la cadena de salida. Es necesario escoger entre las opciones debajo de "Cadena de entrada" y "Cadena de salida" (si no reconoce los terminos de estas opciones recomendamos leer más abajo sobre el dogma central de la biología). 

<img src="https://github.com/proyectotraduccionADN/proyectotraduccionadn/blob/master/readme%20images/2.jpg"> 

Después de esto solo se debe hacer click en en el botón traducir y de inmediato aparecerá la cadena traducida en el cuadro con borde amarillo junto a un pequeño aviso que dice "La cadena se tradujo exitosamente".

<img src="https://github.com/proyectotraduccionADN/proyectotraduccionadn/blob/master/readme%20images/3.jpg">

Si hipotéticamente la cadena de entrada que va a subir es muy larga, puede usar la opción archivo abrir para cargar archivos .txt directamente al programa.

<img src="https://github.com/proyectotraduccionADN/proyectotraduccionadn/blob/master/readme%20images/4.jpg">

Esta opción le dejará seleccionar archivos desde su equipo.

<img src="https://github.com/proyectotraduccionADN/proyectotraduccionadn/blob/master/readme%20images/5.jpg">

Si después de traducir la cadena desea guardarla en un archivo .txt en su equipo, puede hacer esto con la opción archivo guardar.

<img src="https://github.com/proyectotraduccionADN/proyectotraduccionadn/blob/master/readme%20images/6.jpg">

Existe otra opción adicional en el programa que es la de "Codón de inicio", si decide traducir su cadena con esta opción seleccionada, lo que sucederá es que la traducción de proteinas solo comenzará cuando aparezca el codón de inicio y terminará cuando encuentre alguno de los codones de parada, el programa realizará este proceso las veces que sea posible hasta terminar la traducción de la cadena de entrada.

<img src="https://github.com/proyectotraduccionADN/proyectotraduccionadn/blob/master/readme%20images/7.jpg">

## Más información sobre el dogma central de la biología 

Este dogma de forma simplificada nos dice que la información en la célula pasa de ADN a ARN a proteínas. 

El DNA o ADN contiene la información genética que codifica para la síntesis de todas las proteínas celulares, de manera que cada célula de un individuo contiene el mismo DNA que las demás. El DNA se compone de dos cadenas que se enrollan para formar una estructura de doble hélice, estas cadenas reciben el nombre una de DNAsense y la otra de DNAantisense y se conforman de nucletidos los cuales se enlazan por pares muy específicos.  

Los nucleótidos son cada una de las unidades que forman los ácidos nucleicos, el ácido desoxirribonucleico (DNA) y el ácido ribonucleico (RNA). Los nucleótidos están formados por una base nitrogenada, una pentosa (azúcar cíclico de 5 átomos de carbono) y un grupo fosfato, unidos por enlaces covalentes (fuertes). Las bases nitrogenadas son purinas (adenina (A) y guanina (G)) y pirimidinas (citosina (C) timina (T) (en el caso del DNA) o Uracilo (U) (en el caso del RNA)). En el ácido desoxirribonucleico (DNA) la pentosa es la desoxirribosa, mientras que en el ácido ribonucleico (RNA) es la ribosa. 

Los nucleótidos de las dos cadenas del DNA se enlazan unicamente "A con T" y "C con G" este sistema tan particular permite lo que se conoce como duplicación del DNA, que es el proceso principal para que una célula pueda reproducirse, esto de forma simple implica que de una sola cadena de DNA la célula puede obtener la otra, y no solo eso también puede realizar un proceso conocido como transcripción del DNA, por el cual se crea el RNA, usa este mismo principio de pares de bases pero en este caso A se junta con U. El RNA tiene una única cadena.

Si usted como un ejercicio mental quisiera pasar de DNAsense a RNA, simplemente tendria que cambiar cada T por U, si quisiera pasar de DNAantisense a RNA debería usar todo el proceso de transcripción del DNA.

Por último para traducir el RNA a proteínas, las cuales estan hechas de aminoácidos, la célula usa un codigo de tripletas, esto quiere decir cada grupo de tres nucleótidos codifica para un aminoácido específico, estas tripletas de aminoácidos se conocen como codones, también existen tripletas especiales que le indican a la célula donde iniciar este proceso de traducción y donde terminarlo (es la opción de codón de inicio en el programa), esto se debe a que existe mucha información en el DNA que no es necesaria en este proceso y que codificaría para proteínas sin sentido o innecesarias. En biología existen tablas que muestran todos los aminoacidos y sus codones correspondientes, se usan dos códigos uno de tres letras, que en este programa correponde a la opción "Proteinas", y uno de una letra, que en este programa corresponde a "ProteinasSimple".   

REFERENCIAS http://ghr.nlm.nih.gov/handbook/howgeneswork/makingprotein
