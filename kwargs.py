
def buscar_datos(*args, **kwargs):
    for arg in args:
        print(arg)
    for key, value in kwargs.items():
        print("key", key, "value", value)
        for k, v in value.items():
            print("k", k, "v", v)

database = {
    "per1": {
        "prim_nombre": "Chachi",
        "seg_nombre": "Manolo",
        "prim_apellido": "Rupich",
        "seg_apellido": "Yuca"
    }
}
buscar_datos("Chachi", "Manolo", "Rupich", "Yuca", **database)


