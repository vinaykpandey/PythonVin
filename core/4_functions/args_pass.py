def create_profile(name, age):
    print(name, age)


print(create_profile("Vinay", 35))

print(create_profile(name="Dev", age=30))

print(create_profile(age=30, name="Dev"))


def build_profile(*args, **kwargs):
    print("args: ", args)  # tuple
    print(kwargs)  # dict


build_profile(age=30, name="Dev")

d = dict(age=30, name="Dev")
build_profile(**d)
