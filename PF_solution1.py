def calculation(jewel_name,quantity):
    avail_jewel_price_per_gram_dict = {
        "Bentex": 20,
        "Silver": 50,
        "Gold": 2600,
        "Platinum": 3000
    }
    cost_of_jewel=0
    available_jewels = list(avail_jewel_price_per_gram_dict.keys())
    price_list=list(avail_jewel_price_per_gram_dict.values())
    for i in range(0,len(available_jewels)):
        if jewel_name==available_jewels[i]:
            cost_of_jewel=price_list[i]*quantity
            return cost_of_jewel
        else:
            continue
    return 0

def input_data():
    print("Enter the Quantity of the Jewels:")
    quantity=int(input())
    purchased_jewels_list=[]
    purchased_quantity_in_grams_list=[]
    for i in range(0,quantity):
        print("Enter the Jewel Name:")
        purchased_jewels_list.append(input())
        print("Enter the jewel quantity:")
        purchased_quantity_in_grams_list.append(int(input()))

    return purchased_jewels_list,purchased_quantity_in_grams_list

def cleaning(purchased_jewels_list,purchased_quantity_in_grams_list):
    avail_jewel_price_per_gram_dict = {
        "Bentex": 20,
        "Silver": 50,
        "Gold": 2600,
        "Platinum": 3000
    }
    available_jewels=list(avail_jewel_price_per_gram_dict.keys())
    # print(available_jewels)
    price_final=[]
    flag=0
    for i in range(0,len(purchased_jewels_list)):
        for j in range(0,len(available_jewels)):
            flag=0
            # print(purchased_jewels_list[i], available_jewels[j])
            if purchased_jewels_list[i]==available_jewels[j]:
                flag=1

                cost=calculation(purchased_jewels_list[i],purchased_quantity_in_grams_list[i])
                price_final.append(cost)
                break
            else:
                continue
    # print(price_final)
    return price_final






def main():
    purchased_jewels_list, purchased_quantity_in_grams_list=input_data()
    # purchased_jewels_list=["Silver","Gold","Platinum","ABC"]
    # purchased_quantity_in_grams_list=[20,7,3,5]
    price_val=cleaning(purchased_jewels_list,purchased_quantity_in_grams_list)
    total_cost=0
    for i in price_val:
        total_cost=total_cost+i
    if total_cost > 20000:
        total_cost = total_cost - total_cost * (0.03)
    print(total_cost)
main()