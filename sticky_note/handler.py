rem_item = []
def add_rem(item:str):
    global rem_item
    rem_item.append(item)

def remove_rem(idx:int)->bool:
    global rem_item
    if len(rem_item) < idx:
        return False
    rem_item.pop(index=idx)
    return True

def list_rem()->str:
    if  len(rem_item) == 0:
        return "沒東西啦 臭ㄐㄐ"
    else:
        s = "剩下這些(OuO):\n"
        for i in range(len(rem_item)):
            s += f"{i}:{rem_item[i]}\n"
        return s