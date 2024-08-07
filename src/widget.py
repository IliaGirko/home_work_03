from src.masks import get_mask_account, get_mask_card_number, number_user_card

user_input_date: str = input("Введите дату ")


def mask_account_card(number_card_or_check_client: str) -> str | None:
    """Функция обрабатывающая информацию о карте и счете"""
    if "Счет" in number_card_or_check_client:
        return f"{get_mask_account(number_card_or_check_client)}"
    elif "Visa Classic" in number_card_or_check_client:
        return f"Visa Classic {get_mask_card_number(number_card_or_check_client)}"
    elif "Visa Platinum" in number_card_or_check_client:
        return f"Visa Platinum {get_mask_card_number(number_card_or_check_client)}"
    elif "Visa Gold" in number_card_or_check_client:
        return f"Visa Gold {get_mask_card_number(number_card_or_check_client)}"
    elif "Maestro" in number_card_or_check_client:
        return f"Maestro {get_mask_card_number(number_card_or_check_client)}"
    elif "MasterCard" in number_card_or_check_client:
        return f"MasterCard {get_mask_card_number(number_card_or_check_client)}"
    else:
        return "Введен не корректный номер карты или счета"


def get_date(full_date: str) -> str | None:
    """Функция обрабатывающая дату и редактирующая ее"""
    return f"{full_date[8:10]}.{full_date[5:7]}.{full_date[:4]}"


print(mask_account_card(number_user_card))
print(get_date(user_input_date))
