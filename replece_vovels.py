
def replace_vovels(string, char):
    vovels = "aeiouAEIOU"
    for vovels in vovels:
        string = string.replace(vovels,char)
    return string

print(replace_vovels("the aayrjbklvzd","#"))
