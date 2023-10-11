pirveli=10
meore=9
mesame=4
meotxe=10
mexute=2
all=pirveli+meore+mesame+meotxe+mexute
sashualo_aritmetikuli=all/5
if sashualo_aritmetikuli>9:
    print("გილოცავ მატრიცელო შენ გადმოგეცა 300 ლარიანი ბანძი ტოსტერი რასაც შეალიე შენი ცხოვრების წლები")
elif sashualo_aritmetikuli<5:
    print("დაუპრინტე გილოცავ გაექეცი მატრიცას")
elif sashualo_aritmetikuli>5:
    if sashualo_aritmetikuli<9:
        print("you are mid")
    elif sashualo_aritmetikuli>10:
        print("theres wrong")
    elif sashualo_aritmetikuli<0:
        print("theres wrong")

