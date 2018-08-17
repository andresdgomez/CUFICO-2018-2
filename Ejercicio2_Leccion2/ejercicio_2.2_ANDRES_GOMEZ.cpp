# include <iostream>

using namespace std;

int main(){

	long f1 = 1 ;
	long f2 = 1;
	int  s;

	for (int i = 0; i < 80; i++) {

		s = f1 + f2;
		f1 = f2;
		f2 = s;

		if (s % 2 == 0){

			cout << s << endl; 
		}
	}
 	return 0;
}
