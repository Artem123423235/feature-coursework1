from src.api.aeroplanes_api import AeroplanesAPI
from src.models.aeroplane import Aeroplane
from src.storage.json_saver import JSONSaver


def filter_aeroplanes_by_country(aeroplanes, countries):
    countries = {c.lower() for c in countries}
    return [a for a in aeroplanes if a.country_of_origin.lower() in countries]


def get_aeroplanes_by_altitude(aeroplanes, min_altitude=None, max_altitude=None):
    result = aeroplanes
    if min_altitude is not None:
        result = [a for a in result if a.altitude >= min_altitude]
    if max_altitude is not None:
        result = [a for a in result if a.altitude <= max_altitude]
    return result


def sort_aeroplanes_by_altitude(aeroplanes, reverse=True):
    return sorted(aeroplanes, key=lambda x: x.altitude, reverse=reverse)


def get_top_aeroplanes(aeroplanes, n):
    return aeroplanes[:n]


def print_aeroplanes(aeroplanes):
    if not aeroplanes:
        print("Самолеты не найдены.")
        return

    for i, a in enumerate(aeroplanes, start=1):
        print(
            f"{i}. {a.callsign} | {a.country_of_origin} | "
            f"speed={a.velocity:.2f} | altitude={a.altitude:.2f}"
        )


def user_interaction():
    api = AeroplanesAPI()
    storage = JSONSaver()

    country = input("Введите название страны: ").strip()
    raw_states = api.get_aeroplanes(country)
    aeroplanes = Aeroplane.cast_to_object_list(raw_states)

    for plane in aeroplanes:
        storage.add_aeroplane(plane)

    print("\nПолучены самолеты:")
    print_aeroplanes(aeroplanes)

    top_n = int(input("\nВведите количество самолетов для топ N: ").strip())
    top_planes = get_top_aeroplanes(sort_aeroplanes_by_altitude(aeroplanes), top_n)

    print("\nТоп самолеты по высоте:")
    print_aeroplanes(top_planes)

    countries = input("\nВведите страны регистрации через пробел: ").split()
    filtered = filter_aeroplanes_by_country(aeroplanes, countries)

    print("\nОтфильтрованные самолеты:")
    print_aeroplanes(filtered)
