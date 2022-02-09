/*

@Author : Komil
Language : C++
Mentor/Professor : REDACTED FOR PRIVACY

Description: The code takes in the customers beginning and ending meter,
then calculating how much money spent on the gallons used according to the
meter and the customer's code.

*/

#include <iostream>
#include <iomanip> // to use setprecision to get the right decimal 
using namespace std;

float customer_residential(int total_gal)
{

	float const residential_cost = 5;
	float const dol_per_gal = 0.0005;
	float money_used;

	money_used = (dol_per_gal * total_gal) + residential_cost;
	//cout << "TEST:" << money_used << endl;

	return money_used;
}

double customer_commercial(int total_gal)
{
	double const commercial_cost = 1000;
	double const dol_per_gal = 0.00025;
	double money_used;

	if (total_gal <= 4000000)
	{
		money_used = commercial_cost;
	}

	else
	{
		total_gal = total_gal - 4000000;
		//cout << "Total gal before calculation:" << total_gal << endl;
		money_used = (dol_per_gal * total_gal) + commercial_cost;
		//cout << "TEST:" << money_used << endl;
	}

	return money_used;
}

double customer_industrial(int total_gal)
{
	double const industrial_cost = 1000;
	double const dol_per_gal = 0.00025;
	double money_used;

	if (total_gal <= 4000000)
	{
		money_used = industrial_cost;
	}

	if (total_gal >= 4000001)
	{
		money_used = industrial_cost + 1000;

		if (total_gal >= 10000001)
		{
			total_gal = total_gal - 10000000;
			money_used = (dol_per_gal * total_gal) + (industrial_cost + 1000);
		}
	}

	return money_used;
}

int main()
{
	int cont = 1; // to keep the loop going
	int begin_meter; // customer's beginning meter
	int end_meter; // customer's ending meter
	char cust_code; // the code to charge on (the amount)
	char user_choice; // choice to either exit or try again
	int total_gal; // gallons used from the beginning to the ending

	do
	{
		cout << "Enter your beginning meter:";
		cin >> begin_meter;

		if (begin_meter > 999999999)// checks if beginning meter is valid
		{
			cout << "You have given an invalid meter! Exiting program!" << endl;
			break;
		}

		cout << "Enter your ending meter:";
		cin >> end_meter;

		if (end_meter > 999999999) // checks if ending meter is valid
		{
			cout << "You have given an invalid meter! Exiting program!" << endl;
			break;
		}

		cout << "Enter your code:";
		cin >> cust_code;
		cust_code = toupper(cust_code); // Converts the letter to a capital for no errors.

		total_gal = end_meter - begin_meter; // if negative, follow the notes

		if (total_gal <= 0) // Get the total galons used IF the beginning meter is less than the ending meter
		{
			total_gal = (1000000000 - begin_meter) + end_meter;
		}

		cout << "\n\t" << "Details Summary" << endl;
		cout << "\nBeginning meter\t:" << begin_meter << endl; // Prints out the beginning meter
		cout << "ending meter\t:" << end_meter << endl; // Prints out the ending meter
		cout << "Customer code\t:" << cust_code << endl; // Prints out the beginning meter
		cout << "Gallons used\t:" << total_gal << endl; // Prints out the total galons used


		if (cust_code == 'R')
		{
			cout << "Money billed\t:" << customer_residential(total_gal) << "$" << endl; // Prints out total money used
		}

		else if (cust_code == 'C')
		{
			cout << setprecision(15) << "Money billed\t:" << customer_commercial(total_gal) << "$" << endl; // Prints out total money used
		}

		else if (cust_code == 'I')
		{
			cout << setprecision(15) << "Money billed\t:" << customer_industrial(total_gal) << "$" << endl; // Prints out total money used
		}

		else
		{
			cout << "Entered an invalid code!" << endl;
			main();
		}

		// Prompt the user if they want to try again or exit

		cout << "\n" << "Try another bill?(y/n):";
		cin >> user_choice;
		user_choice = tolower(user_choice);
		cout << "\n";

		if (user_choice == 'y')
		{
			continue; // continues to prompt the user
		}

		else
		{
			cout << "Thank you, and goodbye!";
			break; // ends the loop and the code overall
		}

	} while (cont);

	return 0;
}

