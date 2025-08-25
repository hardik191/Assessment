#include <stdio.h>
int main()
{

    int qty, choice;
    char morOrder;
    float Amount = 0, Total = 0;
    do
    {
        printf("______________Menu_____________\n");
        
        printf("1.Pizaa       price = 180rs/pcs\n");
        printf("2.Burger      price = 100rs/pcs\n");
        printf("3.Dosa        price = 120rs/pcs\n");
        printf("4.Idali       price = 050rs/pcs\n");

        printf("Enter Your choice:: ");
        scanf("%d", &choice);
        switch (choice)
        {
        case 1:
            printf("You have selected Pizza.\n");
            printf("Enter the quantity :");
            scanf("%d", &qty);
            Amount = 180 * qty;
            break;
        case 2:
            printf("You have selected Burger.\n");
            printf("Enter the quantity :");
            scanf("%d", &qty);
            Amount = 100 * qty;
            break;
        case 3:
            printf("You have selected Dosa.\n");
            printf("Enter the quantity :");
            scanf("%d", &qty);
            Amount = 120 * qty;
            break;
        case 4:
            printf("You have selected Idail.\n");
            printf("Enter the quantity :");
            scanf("%d", &qty);
            Amount = 50 * qty;
            break;
        default:
            printf("Invalid Choice!\n");
            Amount = 0;
            break;
        }
        if (Amount > 0)
        {
            printf("Amount:%.2f\n", Amount);
            Total += Amount;
            printf("Total Amount:%.2f\n", Total);
        }

        printf("Do you want place more orders ? y & n :");
        scanf("%s", &morOrder);
    } while (morOrder == 'y' || morOrder == 'Y');
    printf("Your final Bill :%.2f", Total);
    return 0;
}
