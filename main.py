
# One Stop Insurance Invoice Program.
# Written By : Noah Gillard
# Date Written: March, 23, 2023

# Import libraries.

import datetime

# Read constants from OSICDef.dat file.

f = open("OSICDef.dat", "r")
HEADING = (f.readline())
POLICY_NUM = int(f.readline())
BAS_PREM = float(f.readline())
ADD_INS_DIS = float(f.readline())
EXT_LIABIL_RATE = float(f.readline())
GLASS_COV_RATE = float(f.readline())
LOAN_COV_RATE = float(f.readline())
HST_RATE = float(f.readline())
PROC_FEE = float(f.readline())
f.close()


while True:
    # User inputs.

    today = datetime.datetime.now()

    NextPayDate = (today.replace(day=1) + datetime.timedelta(days=32)).replace(day=1)
    print(NextPayDate)

    InvoiceDate = today.strftime("%d %m, %Y")

    FirstName = input("Enter the customers first name: ").title()
    LastName = input("Enter the customers last name: ").title()
    Add = input("Enter the customers street address: ")
    City = input("Enter the customers city: ").title()

    while True:
        ValProv = ["NL", "PE", "NS", "NB", "QC", "ON", "MB", "SK", "AB", "BC", "YT", "NT", "NU"]
        Prov = input("Enter the customers province (LL): ").upper()
        if Prov in ValProv:
            break
        else:
            print("Province not valid. Please re enter.")
            continue

        PostCode = input("Enter your postal code: ").upper()

        PhoneNum = input("Enter your phone number: ")

    while True:
        CarsIns = int(input("Enter the number of vehicles being insured: "))
        if CarsIns == 1:
            print(BAS_PREM)
            break
        elif CarsIns >= 2:
            DiscountPrice = (CarsIns - 1) * ADD_INS_DIS * BAS_PREM
            break
        else:
            continue

    while True:
        ExtLiabil = input("Enter (Y)yes or (N)no for extra liability up to $1,000,000: ").upper()
        if ExtLiabil == "Y":
            ExtLiabil = EXT_LIABIL_RATE
            break
        elif ExtLiabil == "N":
            ExtLiabil = 0.00
            break
        else:
            print("Enter a valid character either Y or N")
            continue

    while True:
        GlassCov = input("Enter (Y)yes or (N)no for glass coverage: ").upper()
        if GlassCov == "Y":
            GlassCov = GLASS_COV_RATE
            break
        elif GlassCov == "N":
            GlassCov = 0.00
            break
        else:
            print("Enter a valid character either Y or N")
            continue

    while True:
        LoanCar = input("Enter (Y)yes or (N)no for loaner car coverage: ").upper()
        if LoanCar == "Y":
            LoanCar = LOAN_COV_RATE
            break
        elif LoanCar == "N":
            LoanCar = 0.00
            break
        else:
            print("Enter a valid character either Y or N")
            continue

    while True:
        FullMon = input("Enter weather the customer will pay in (F)full or (M)monthly: ").upper()
        if FullMon == "F":
            break
        elif FullMon == "M":
            break
        else:
            print("Enter a valid character either F or M")

    # Perform program calculations.

    TotExtCost = ExtLiabil + GlassCov + LoanCar
    TotInsPrem = BAS_PREM + DiscountPrice + TotExtCost
    HST = HST_RATE * TotInsPrem
    TotCost = HST + TotInsPrem
    MonPay = (TotCost + PROC_FEE) / 8
    # Display required invoice.

    print()
    print(f"                                  {HEADING}")
    print(u"\u2500" * 95)
    print(f" Policy No.                                                                               {POLICY_NUM}")
    print(f" Invoice Date:                                                                     {InvoiceDate}")
    print()
    print(f" {FirstName}, {LastName}")
    print(f" {Add} , {City}, {Prov}, {PostCode}")
    print(f" {PhoneNum}")
    print(u"\u2500" * 95)
    print(f" Vehicles Insured:                                                                           {CarsIns}")
    DiscountPriceDsp = "${:,.2f}".format(DiscountPrice)
    print(f" Discount Price:                                                                       {DiscountPriceDsp}")
    print(u"\u2500" * 95)
    ExtLiabilDsp = "${:,.2f}".format(ExtLiabil)
    print(f" Extra Liability Charge:                                                               {ExtLiabilDsp}")
    GlassCovDsp = "${:,.2f}".format(GlassCov)
    print(f" Glass Coverage Charge:                                                                 {GlassCovDsp}")
    LoanCarDsp = "${:,.2f}".format(LoanCar)
    print(f" Loaner Car Charge:                                                                     {LoanCarDsp}")
    print(u"\u2500" * 95)
    TotExtCostDsp = "${:,.2f}".format(TotExtCost)
    print(f" Total Extra Costs:                                                                    {TotExtCostDsp}")
    TotInsPremDsp = "${:,.2f}".format(TotInsPrem)
    print(f" Total Insurance Premium:                                                            {TotInsPremDsp}")
    HSTDsp = "${:,.2f}".format(HST)
    print(f" HST:                                                                                  {HSTDsp}")
    TotCostDsp = "${:,.2f}".format(TotCost)
    print(f" Total Cost:                                                                         {TotCostDsp}")
    print(u"\u2500" * 95)
    print(f" Payment Type:                                                                               {FullMon}")
    MonPayDsp = "${:,.2f}".format(MonPay)
    print(f" Monthly Payment:                                                                      {MonPayDsp}")
    print(f" Next Payment Date:                                                 {NextPayDate}")

    # Save the data to a data file.
    f = open("Policies.dat", "a")

    f.write("{}, ".format(str(POLICY_NUM)))
    f.write("{}, ".format(InvoiceDate))
    f.write("{}, ".format(FirstName))
    f.write("{}, ".format(LastName))
    f.write("{}, ".format(Add))
    f.write("{}, ".format(City))
    f.write("{}, ".format(Prov))
    f.write("{}, ".format(PostCode))
    f.write("{}, ".format(PhoneNum))
    f.write("{}, ".format(CarsIns))
    f.write("{}, ".format(ExtLiabil))
    f.write("{}, ".format(GlassCov))
    f.write("{}, ".format(LoanCar))
    f.write("{}, ".format(FullMon))
    f.write("{}\n".format(TotInsPremDsp))

    f.close()

    print()
    print("Policy Information Processed and Saved")

    POLICY_NUM += 1

