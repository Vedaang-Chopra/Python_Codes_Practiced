import numpy as np

def common_inputs():
    principal_amount=int(input())
    tenure=int(input())
    return principal_amount,tenure

def calculation(principal_amount,tenure,no_of_slabs,year,rate):
    emi=np.zeros(no_of_slabs)
    monthly_interest=np.zeros(no_of_slabs)
    for i in range(no_of_slabs):
        monthly_interest[i]=(rate[i]/(year[i]*12))

    for i in range(no_of_slabs):
        emi[i]=principal_amount*monthly_interest[i]
        temp=1-(1/((1+monthly_interest[i])**(year[i]*12)))
        emi[i]=emi[i]/temp

    return emi.sum()
def slabs_input():
    no_of_slabs = int(input())
    year=np.zeros(no_of_slabs)
    rate=np.zeros(no_of_slabs)
    for i in range(no_of_slabs):
        a=(input())
        a.strip()
        a1=a.split(" ")
        # print(a1)
        year[i]=(float(a1[0]))
        rate[i]=(float(a1[1]))
    # print(year)
    # print(rate)
    return year,rate,no_of_slabs
principal_amount,tenure=common_inputs()

# principal_amount,tenure=10000,10
# no_of_slabs_1=3
# no_of_slabs_2=3
# year_1=[5,10,5]
# rate_1=[9.5,9.6,9.5]
# year_2=[10,5,5]
# rate_2=[6.9,8.5,7.9]
year_1,rates_1,no_of_slabs_1=slabs_input()
year_2,rates_2,no_of_slabs_2=slabs_input()
emi_1=calculation(principal_amount,tenure,no_of_slabs_1,year_1,rates_1)
emi_2=calculation(principal_amount,tenure,no_of_slabs_2,year_2,rates_2)

if emi_1<emi_2:
    print("Bank A")
else:
    print("Bank B")