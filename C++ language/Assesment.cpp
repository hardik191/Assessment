#include <iostream>
using namespace std;
int main()
{
    string name, order;
    char yes;
    int i, j;

    do
    {
        cout << "\n----------Tops Tech. Fast Food----------\n";

        cout << "Place Enter Your Name:";
        cin >> name;

        cout << "Hello " << name << "\n";

        cout << "\nWhat Would You like to order?\n";

        cout << "\n--------Menu--------\n";

        cout << "1) Pizzas\n";
        cout << "2) Burgers\n";
        cout << "3) Sandwich\n";
        cout << "4) Rolls\n";
        cout << "5) Biryani\n";

        cout << "\n\nPlease Enter Your Choice :";
        cin >> i;

        switch (i)
        {
        case 1:
            cout << "Pizzas";
            break;

        case 2:
            cout << "Burgers";
            break;

        case 3:
            cout << "\n1 Club Sandwich Rs.240\n";
            cout << "2 Veg. Crispy Sandwich Rs.160\n";
            cout << "3 Extream Veg Sandwich Rs.100\n";

            cout << "\nPlease Enter Which Sandwich you would like to have?:";
            cin >> j;

            switch (j)
            {
            case 1:
                int qut;
                cout << "\nPlease Enter Quantity: ";
                cin >> qut;

                cout << "1 Club Sandwich \n";
                cout << "Your Total Bill is :" << 240 * qut;
                break;

            case 2:
                cout << "\nPlease Enter Quantity: ";
                cin >> qut;

                cout << "2 Veg. Crispy Sandwich \n";
                cout << "Your Total Bill is :" << 160 * qut;
                break;

            case 3:
                cout << "\nPlease Enter Quantity: ";
                cin >> qut;

                cout << "\n3 Extream Veg Sandwich \n";
                cout << "Your Total Bill is :" << 100 * qut;
                break;
            default:
                cout << "\n Other \n";
                break;
            }
            break;

        case 4:
            cout << "Rolls";
            break;

        case 5:
            cout << "Biryani";
            break;

        default:
            break;
        }

        cout << "\nYour Order Will be delivered in 40 Minutes\n";
        cout << "Thank you For Ordering From Tops Tech Fast Food\n";

        cout << "Would You like to order anything else? Y / N:";
        cin >> yes;
        if (yes == 'Y' || yes == 'y')
        {
        }
        else
        {
            i = 0; // stop loop
        }
    } while (i);
}
