#this script demonstrates the use of keyword arguments in a function 
#keyword arguments allow you to pass arguments to a functiob by explicitily
def show_profile(**info):
    for key, value in info.items():
        print(f"{key}: {value}")


show_profile(name="john", age=28, location="nyc")
show_profile(name="amice", age=30,location="la",occupation="engineer")\
