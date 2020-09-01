import logging
from database.handler import cursor,query_single_col
def add_rem(item:str):
    cmd = '''
    INSERT sticky_note ctx VALUES (%s)
    '''
    cursor.execute(cmd,(item))

def remove_rem(idx:int)->bool:
    cmd = '''
    DELETE FROM sticky_note WHRER idx == (%s)
    '''
    cursor.execute(cmd,(idx))

def list_rem()->str:
    rem_item=query_single_col("sticky_note" , "ctx")
    if  len(rem_item) == 0:
        return "沒東西啦 臭ㄐㄐ"
    else:
        s = "剩下這些(OuO):\n"
        for i in range(len(rem_item)):
            s += f"{i}:{rem_item[i]}\n"
        return s