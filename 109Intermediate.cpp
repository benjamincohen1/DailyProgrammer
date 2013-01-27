#include <iostream>
#include <string> 
#include <stdio.h>
#include <stdlib.h>
#include "109Intermediate.h"
#include <sstream>
using namespace std;

int main(){
	int a1=0;
	int a2=100;
	int b1=0;
	int b2=100;

	for(int x = a1;x<=a2;x++){
		for(int y = b1;y<=b2;y++){
			if(isPalendrome(x*y)){
				cout<<"X "<<x<<" "<<y<<endl;
			}
		}
	}
}
bool isPalendrome(int x){
	int i = x;
	std::string s;
	std::stringstream out;
	out << i;
	s = out.str();	
	string str=s;
	string tmp=str;
	for(int z=0;z<=str.length();z++){
		//cout<<tmp<<endl;;

		tmp[z]=s[s.length()-z-1];
	}
	//cout<<"Num is: "<<x<<" palendrome is: "<<tmp<<endl;

	int x2;
	istringstream ( tmp ) >> x2;
	//cout<<x2<<endl;

	if(x2==x){
		return true;
	}
	return false;

}