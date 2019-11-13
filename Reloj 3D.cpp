
//Dependecnias:
//+freeglut
#define _CRT_SECURE_NO_WARNINGS

#define tasaFPS 60

#include <iostream>
#include <sstream>
#include <GL/Utilidades.h>
#include <ctime>
static GLuint  estrellaDavid;
GLuint petalo, corola, florSec, florMin, florHora;
using namespace std;

//variable dependiente del tiempo
static float alfa = 0; //angulo que rotan las teteras

time_t curr_time = time(NULL);

tm *tm_local = localtime(&curr_time);

static float alfaSegundo = tm_local->tm_sec;
static float alfaMinuto = 360 / (60) * tm_local->tm_min;
static float alfaHora = (360 / 12) * tm_local->tm_hour;


void init() {

	glClearColor(1.0f, 1.0f, 1.0f, 1.0f);


	//////////////////////////Definicion de estrellaDavid
	estrellaDavid = glGenLists(1); //corazón del reloj
	glNewList(estrellaDavid, GL_COMPILE);

	//Pentagono
	float radio1 = 1;
	float radio07 = 0.7;
	glPointSize(10);


	//glPolygonMode(GL_FRONT, GL_LINE);
	glBegin(GL_TRIANGLE_STRIP);
	for (int i = 0; i < 3; i++) {
		//glColor3f(i / 4.0, i / 3.0, i / 7.0);
		glVertex3f(radio07*cos((i * 2 * PI / 3.0) + PI / 2.0), radio07*sin((i * 2 * PI / 3.0) + PI / 2.0), 0.0);
		glVertex3f(radio1*cos((i * 2 * PI / 3.0) + PI / 2.0), radio1*sin((i * 2 * PI / 3.0) + PI / 2.0), 0.0);
	}

	glVertex3f(radio07*cos(PI / 2.0), radio07*sin(PI / 2.0), 0.0);
	glVertex3f(radio1*cos(PI / 2.0), radio1*sin(PI / 2.0), 0.0);

	glEnd();

	glBegin(GL_TRIANGLE_STRIP);
	for (int i = 0; i < 3; i++) {
		//glColor3f(i / 4.0, i / 3.0, i / 7.0);
		glVertex3f(radio07*cos((-i * 2 * PI / 3.0) - PI / 2.0), radio07*sin((-i * 2 * PI / 3.0) - PI / 2.0), 0.0);
		glVertex3f(radio1*cos((-i * 2 * PI / 3.0) - PI / 2.0), radio1*sin((-i * 2 * PI / 3.0) - PI / 2.0), 0.0);
	}

	glVertex3f(radio07*cos(-PI / 2.0), radio07*sin(-PI / 2.0), 0.0);
	glVertex3f(radio1*cos(-PI / 2.0), radio1*sin(-PI / 2.0), 0.0);

	glEnd();
	glEndList();

	//////////////////////////////Fin estrella David

	////////////////////////////////////////////Inicio Flor
		//Petalo
	petalo = glGenLists(1);
	glNewList(petalo, GL_COMPILE);
	glColor3f(0, 0, 1);
	glPushMatrix();
	glScalef(0.15, 0.5, 0.15);
	glutSolidSphere(1, 20, 20);
	glPopMatrix();
	glEndList();

	//Corola
	corola = glGenLists(1);
	glNewList(corola, GL_COMPILE);
	for (auto i = 0; i < 12; i++) {
		glPushMatrix();
		glRotatef(i * 30, 0, 0, 1);
		glTranslatef(0, 0.25, 0);
		glScalef(0.5, 0.5, 0.5);
		glCallList(petalo);

		glPopMatrix();

	}
	glColor3f(1, 1, 0);
	glPushMatrix();
	glScalef(0.2, 0.2, 0.2);
	glutSolidSphere(1, 20, 20);
	glPopMatrix();

	glEndList();

	//FlorSec
	florSec = glGenLists(1);
	glNewList(florSec, GL_COMPILE);

	glPushMatrix();
	glColor3f(0, 0.9, 0.1);
	glTranslatef(0, -0.8, 0);
	glScalef(0.04, 1.3, 0.04);
	glutSolidCube(1.0);
	glPopMatrix();

	glPushMatrix();
	glTranslatef(0, 0.1, 0);
	glScalef(0.5, 0.5, 0.5);
	glCallList(corola);
	glPopMatrix();
	glEndList();


	//FlorMin
	florMin = glGenLists(1);
	glNewList(florMin, GL_COMPILE);

	glPushMatrix();
	glColor3f(0, 0.8, 0.2);
	glTranslatef(0, -0.5, 0);
	glScalef(0.04, 0.9, 0.04);
	glutSolidCube(1.0);
	glPopMatrix();

	glPushMatrix();
	glTranslatef(0, 0.2, 0);
	glScalef(0.5, 0.5, 0.5);
	glCallList(corola);
	glPopMatrix();
	glEndList();

	//FlorHora
	florHora = glGenLists(1);
	glNewList(florHora, GL_COMPILE);

	glPushMatrix();
	glColor3f(0, 0.7, 0.3);
	glTranslatef(0, -0.25, 0);
	glScalef(0.04, 0.6, 0.04);
	glutSolidCube(1.0);
	glPopMatrix();

	glPushMatrix();
	glTranslatef(0, 0.25, 0);
	glScalef(0.5, 0.5, 0.5);
	glCallList(corola);
	glPopMatrix();
	glEndList();
	/////////////////////////////////////////////////////////////////////Fin Flor





		//Configurar el motor de render
	glEnable(GL_DEPTH_TEST);
}

void FPS() {
	//Muestra los FPS en la barra de titulo
	int ahora, tiempoT;
	static int antes = glutGet(GLUT_ELAPSED_TIME);
	static int fotogramas = 0;

	fotogramas++;
	ahora = glutGet(GLUT_ELAPSED_TIME);
	tiempoT = ahora - antes;

	if (tiempoT > 1000) {

		// reiniciar la cuenta
		fotogramas = 0;
		antes = ahora;
	}
}

void display() {
	//Funcion de atencion al dibujo
	glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT);



	//Seleccion de la matriz modelo-vista
	glMatrixMode(GL_MODELVIEW);
	glLoadIdentity();

	// situamos y orientamos la camara
	gluLookAt(0, 0, -3.5, 0, 0, 0, 0, 1, 0);

	//ejes();

	//Estrellas
	glPushMatrix();
	glScalef(0.25, 0.25, 0.25);
	glColor3f(0.5, 0, 0.5);
	glRotatef(alfa / 2, 0, 1, 0);
	glCallList(estrellaDavid);
	glPopMatrix();

	glPushMatrix();
	glScalef(0.25, 0.25, 0.25);
	glColor3f(0.4, 0, 0.6);
	glRotatef(alfa / 2, alfa / 2, 1, 0);
	glCallList(estrellaDavid);
	glPopMatrix();

	glPushMatrix();
	glScalef(0.25, 0.25, 0.25);
	glColor3f(0.6, 0, 0.4);
	glRotatef(alfa / 2, 0, 1, alfa / 2);
	glCallList(estrellaDavid);
	glPopMatrix();

	//teteras

	for (int i = 0; i < 12; i++) {
		glPushMatrix();
		glColor3f(1, 0, 0);
		glRotatef(360 / 12 * i, 0, 0, 1);
		glTranslatef(0, 0.9, 0);
		glRotatef(-90, 1, 0, 0);
		glRotatef(90, 0, 1, 0);
		glRotatef(alfa / 4, 0, 1, 0);
		glScalef(0.15, 0.15, 0.15);

		glutSolidTeapot(0.5);
		glPopMatrix();

	}


	//Varillas

	//Segundos
	glPushMatrix();
	glRotatef(alfaSegundo, 0, 0, 1);
	glScalef(0.5, 0.5, 0.5);
	glTranslatef(0, 1.5, 0);
	glCallList(florSec);
	glPopMatrix();

	//Minutos
	glPushMatrix();
	glRotatef(alfaMinuto, 0, 0, 1);
	glScalef(0.5, 0.5, 0.5);
	glTranslatef(0, 1, 0);
	glCallList(florMin);
	glPopMatrix();

	//Horas
	glPushMatrix();
	glRotatef(alfaHora, 0, 0, 1);
	glScalef(0.5, 0.5, 0.5);
	glTranslatef(0, 0.6, 0);
	glCallList(florHora);
	glPopMatrix();


	glutSwapBuffers(); //darle una patada a todo lo que queda pendiente

	FPS();
}


void timerSegundos(int valor) {
	alfaSegundo += 360 / 60;
	glutPostRedisplay();
	glutTimerFunc(valor, timerSegundos, valor);
}

void timerMinutos(int valor) {
	alfaMinuto += (360 / 60);
	glutPostRedisplay();
	glutTimerFunc(valor, timerMinutos, valor);
}

void timerHoras(int valor) {
	alfaHora += (360 / 12);
	glutPostRedisplay();
	glutTimerFunc(valor, timerHoras, valor);
}



void reshape(int w, int h) {

	float ra = (float)w / h; //Relacion de aspecto de la ventana

	//fijamos el marco dentro de la ventana de dibujo
	glViewport(0, 0, w, h);


	//Seleccionar la camara
	glMatrixMode(GL_PROJECTION);
	glLoadIdentity();

	/*
	Camara ortografica con isometria
	if (ra < 1)
		glOrtho(-2, 2, -2 / ra, 2 / ra, -1, 10);
	else
		glOrtho(-2*ra, 2*ra, -2 , 2 , -1, 10);
	*/

	//Camara Perspectiva
	gluPerspective(40, ra, 0.1, 100);


}

void update() {
	//Callback de atencion al evento idle

	//Cmbiar la variable temporal
	//alfa += 0.1;

	//Control de tiempo transcurrido
	static int antes = glutGet(GLUT_ELAPSED_TIME);
	int ahora = glutGet(GLUT_ELAPSED_TIME);
	float tiempoTranscurrido = float(ahora - antes) / 1000;

	// Velocidad angular constante
	static const float omega = 1; //Vueltas/sg.

	alfa += omega * 360 * tiempoTranscurrido;

	//Actualizar la hora
	antes = ahora;
	//Encolar un evento de display
	glutPostRedisplay();
}

void onTimer(int tiempo) {
	//Encolar un nuevo temporizador
	glutTimerFunc(tiempo, onTimer, tiempo);
	//Llamar a update
	update();
}

int main(int argc, char ** argv)
{
	// Inicializaciones
	glutInit(&argc, argv);
	glutInitDisplayMode(GLUT_DOUBLE | GLUT_RGB | GLUT_DEPTH); //RESERVA MEMORIA EN LA TARJETA
	glutInitWindowSize(600, 600);
	glutInitWindowPosition(200, 200);

	//Crear la ventana
	glutCreateWindow("Reloj 3D");

	
	init();
	std::cout << "Reloj 3D" << std::endl;

	// Callbacks
	glutDisplayFunc(display);
	glutReshapeFunc(reshape);
	//glutIdleFunc(update); //captura idle

	glutTimerFunc(1000 / tasaFPS, onTimer, 1000 / tasaFPS);
	glutTimerFunc(1000 - tm_local->tm_sec * 1000, timerSegundos, 1000);
	glutTimerFunc(60 * 60 * 1000 - tm_local->tm_min * 60 * 1000, timerHoras, 60 * 60 * 1000);
	glutTimerFunc(60 * 1000 - tm_local->tm_sec * 1000, timerMinutos, 60 * 1000);

	//Poner en marcha el bucle de atencion a eventos
	glutMainLoop();
}