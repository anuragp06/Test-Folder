import UserModule



print("welcome to user information system")
print("1. add user information")
print("2. display all user information")
print("3. exit")

while True:
    choice = int(input("enter your choice:"))
    if choice == 1:
        user_id = int(input("enter user id:"))
        user_name = input("enter user name:")
        user_email = input("enter user email:")
        UserModule.add_user_info(user_id, user_name, user_email)
        print("user information added successfully")
    elif choice ==2:
        all_user_info = UserModule.get_all_user_info()
        print("all user information:")
        for user_id, info in all_user_info.items():
            print(f"user id: {user_id},name: {info['user_name']},email:{info['user_email']}")
    elif choice == 3:
        print("exiting the programm")
        break
    else:
        print("invalid choice")