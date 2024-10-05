CN_mobile = [134,135,136,137,138,139,150]
CN_union=[130,131,132,155,156,185,186]
CN_telecom=[133,153,180,181,189,177,170]

def check_number(phone_number):
    phone_number=''.join(filter(str.isdigit,phone_number))
    if len(phone_number) != 11:
        print("invalid length,again")
        return
    prefix = int(phone_number[:3])
    if prefix in CN_mobile:
        print("Operator : CN mobile")
    elif prefix in CN_telecom:
        print("Operator : CN telecom")
    elif prefix in CN_union:
        print("Operator : CN union")
    else:
        print("wrong operator")
        return
    print(f"we are sening ver code text to your phone:{phone_number}")
if __name__=="__main__":
    phone_number = input("enter your numer:")
    check_number(phone_number)