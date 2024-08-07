number_user_card = input("Введите номер карты или счета ")


def get_mask_card_number(full_number_card: str) -> str | None:
    """Функция, которая маскирует 6 цифр номера карты"""
    return f"{full_number_card[-16:-12]} {full_number_card[-12:-10]}{"*" * 2} {"*" * 4} {full_number_card[-4:]}"


def get_mask_account(full_number_card: str) -> str | None:
    """Функция, которая оставляет только 4 последние цифры карты и 2 звездочки перед ними"""
    return f"{full_number_card[:4]} {"*" * 2}{full_number_card[-4:]}"
