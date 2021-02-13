//#include <iostream>
//using namespace std;
//
//int main() {
//    cout << "Hello, world! Its inside Cpp" << endl;
//    return 0;
//}

#include <iostream>
using namespace std;
/*
An polymorphism example (fuunction overloading)
/* <conio.h> is uincluded to use getch
*/

float area(int);  /*This is function declaration taking 1 arg (circle)*/
int  area(int, int); /*This is function declaration taking 2 arg (rectangle)*/

int main(){
    cout << "Inside cpp";
    int r;

	cout << "Enter radius of circle: ";
	cin >> r;
	cout << "Area of circle is: " << area(r);
	cout <<endl;

	int l,b;

	cout << "Enter length and breadth of a rectangle: ";
	cin >> l >> b;
	cout << "Area of a rectangle is: " <<  area(l,b);
	cout <<endl;

	return 0;
}

int area(int a, int b){
	return a*b;
}

float area(int r){
	return (3.14*r*r);
}

