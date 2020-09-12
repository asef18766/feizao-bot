import logging
from database.handler import cursor


def add_rem(item: str):
    logging.info(f"try to insert item {item}")
    cmd = """
    INSERT INTO sticky_note (ctx) VALUES (%s);
    """
    cursor.execute(cmd, (item, ))


def remove_rem(idx: int) -> bool:
    cmd = """
    DELETE FROM sticky_note WHERE id = (%s);
    """
    cursor.execute(cmd, (idx, ))


def list_rem() -> str:
    cmd = """
    SELECT ctx FROM sticky_note;
    """
    cursor.execute(cmd)
    rem_items = cursor.fetchall()
    if len(rem_items) == 0:
        return "沒東西啦 臭ㄐㄐ"
    else:
        s = "剩下這些(OuO):\n"
        for i, item in enumerate(rem_items):
            s += f"{i}: {item[0]}\n"
        return s