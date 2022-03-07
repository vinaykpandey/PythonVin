def create_profile(name, age):
    print(name, age)


create_profile("Vinay", 35)
print("*"*100)
create_profile("Dev1", age=31)
create_profile(name="Dev", age=30)
print("#"*100)
create_profile(age=30, name="Dev")


def build_profile(*args, **kwargs):
    """
    @param args:
    @param kwargs:
    @return:
    """
    print("args: ", args)  # tuple
    print(kwargs)  # dict


build_profile(age=30, name="Dev")

d = dict(age=30, name="Dev")
build_profile(**d)
