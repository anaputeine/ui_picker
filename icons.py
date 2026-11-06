# picks a random icon set and style, shown on the page with iconify

import random

CONCEPTS = ["home", "search", "bell", "user", "heart", "star", "settings", "plus", "edit", "trash", "share", "download", "check", "warning", "info", "close"]

ICON_SETS = [
    {"name": "Phosphor", "prefix": "ph", "character": "friendly and flexible",
     "styles": {
        "bold": ["house-bold", "magnifying-glass-bold", "bell-bold", "user-bold", "heart-bold", "star-bold", "gear-bold", "plus-bold", "pencil-simple-bold", "trash-bold", "share-network-bold", "download-simple-bold", "check-circle-bold", "warning-circle-bold", "info-bold", "x-bold"],
        "duotone": ["house-duotone", "magnifying-glass-duotone", "bell-duotone", "user-duotone", "heart-duotone", "star-duotone", "gear-duotone", "plus", "pencil-simple-duotone", "trash-duotone", "share-network-duotone", "download-simple-duotone", "check-circle-duotone", "warning-circle-duotone", "info-duotone", "x"],
     }},
    {"name": "Lucide", "prefix": "lucide", "character": "clean and minimal",
     "styles": {
        "outline": ["house", "search", "bell", "user", "heart", "star", "settings", "plus", "pencil", "trash-2", "share-2", "download", "circle-check", "circle-alert", "info", "x"],
     }},
    {"name": "Tabler", "prefix": "tabler", "character": "light and geometric",
     "styles": {
        "outline": ["home", "search", "bell", "user", "heart", "star", "settings", "plus", "pencil", "trash", "share", "download", "circle-check", "alert-circle", "info-circle", "x"],
     }},
    {"name": "Material Symbols", "prefix": "material-symbols", "character": "Google's familiar style",
     "styles": {
        "rounded-filled": ["home-rounded", "search-rounded", "notifications-rounded", "person-rounded", "favorite-rounded", "star-rounded", "settings-rounded", "add-rounded", "edit-rounded", "delete-rounded", "share-rounded", "download-rounded", "check-circle-rounded", "error-rounded", "info-rounded", "close-rounded"],
        "sharp": ["home-outline-sharp", "search-outline-sharp", "notifications-outline-sharp", "person-outline-sharp", "favorite-outline-sharp", "star-outline-sharp", "settings-outline-sharp", "add-outline-sharp", "edit-outline-sharp", "delete-outline-sharp", "share-outline-sharp", "download-outline-sharp", "check-circle-outline-sharp", "error-outline-sharp", "info-outline-sharp", "close-outline-sharp"],
     }},
    {"name": "Heroicons", "prefix": "heroicons", "character": "neat and modern",
     "styles": {
        "outline": ["home", "magnifying-glass", "bell", "user", "heart", "star", "cog-6-tooth", "plus", "pencil", "trash", "share", "arrow-down-tray", "check-circle", "exclamation-circle", "information-circle", "x-mark"],
        "solid": ["home-solid", "magnifying-glass-solid", "bell-solid", "user-solid", "heart-solid", "star-solid", "cog-6-tooth-solid", "plus-solid", "pencil-solid", "trash-solid", "share-solid", "arrow-down-tray-solid", "check-circle-solid", "exclamation-circle-solid", "information-circle-solid", "x-mark-solid"],
     }},
    {"name": "Remix Icon", "prefix": "ri", "character": "sturdy and neutral",
     "styles": {
        "line": ["home-line", "search-line", "notification-3-line", "user-line", "heart-line", "star-line", "settings-3-line", "add-line", "pencil-line", "delete-bin-line", "share-line", "download-line", "checkbox-circle-line", "error-warning-line", "information-line", "close-line"],
        "fill": ["home-fill", "search-fill", "notification-3-fill", "user-fill", "heart-fill", "star-fill", "settings-3-fill", "add-fill", "pencil-fill", "delete-bin-fill", "share-fill", "download-fill", "checkbox-circle-fill", "error-warning-fill", "information-fill", "close-fill"],
     }},
    {"name": "Bootstrap Icons", "prefix": "bi", "character": "classic and compact",
     "styles": {
        "outline": ["house", "search", "bell", "person", "heart", "star", "gear", "plus-lg", "pencil", "trash", "share", "download", "check-circle", "exclamation-circle", "info-circle", "x-lg"],
        "fill": ["house-fill", "search", "bell-fill", "person-fill", "heart-fill", "star-fill", "gear-fill", "plus-lg", "pencil-fill", "trash-fill", "share-fill", "download", "check-circle-fill", "exclamation-circle-fill", "info-circle-fill", "x-lg"],
     }},
    {"name": "Fluent", "prefix": "fluent", "character": "Microsoft's soft rounded style",
     "styles": {
        "regular": ["home-24-regular", "search-24-regular", "alert-24-regular", "person-24-regular", "heart-24-regular", "star-24-regular", "settings-24-regular", "add-24-regular", "edit-24-regular", "delete-24-regular", "share-24-regular", "arrow-download-24-regular", "checkmark-circle-24-regular", "error-circle-24-regular", "info-24-regular", "dismiss-24-regular"],
        "filled": ["home-24-filled", "search-24-filled", "alert-24-filled", "person-24-filled", "heart-24-filled", "star-24-filled", "settings-24-filled", "add-24-filled", "edit-24-filled", "delete-24-filled", "share-24-filled", "arrow-download-24-filled", "checkmark-circle-24-filled", "error-circle-24-filled", "info-24-filled", "dismiss-24-filled"],
     }},
    {"name": "Carbon", "prefix": "carbon", "character": "IBM's precise technical style",
     "styles": {
        "outline": ["home", "search", "notification", "user", "favorite", "star", "settings", "add", "edit", "trash-can", "share", "download", "checkmark-outline", "warning", "information", "close"],
     }},
    {"name": "Iconoir", "prefix": "iconoir", "character": "simple and airy",
     "styles": {
        "regular": ["home", "search", "bell", "user", "heart", "star", "settings", "plus", "edit-pencil", "trash", "share-android", "download", "check-circle", "warning-circle", "info-circle", "xmark"],
     }},
    {"name": "MingCute", "prefix": "mingcute", "character": "rounded and cute",
     "styles": {
        "line": ["home-1-line", "search-line", "notification-line", "user-3-line", "heart-line", "star-line", "settings-3-line", "add-line", "edit-line", "delete-2-line", "share-2-line", "download-2-line", "check-circle-line", "warning-line", "information-line", "close-line"],
        "fill": ["home-1-fill", "search-fill", "notification-fill", "user-3-fill", "heart-fill", "star-fill", "settings-3-fill", "add-fill", "edit-fill", "delete-2-fill", "share-2-fill", "download-2-fill", "check-circle-fill", "warning-fill", "information-fill", "close-fill"],
     }},
    {"name": "Solar", "prefix": "solar", "character": "soft, with many styles",
     "styles": {
        "bold-duotone": ["home-2-bold-duotone", "magnifer-bold-duotone", "bell-bold-duotone", "user-bold-duotone", "heart-bold-duotone", "star-bold-duotone", "settings-bold-duotone", "add-circle-bold-duotone", "pen-bold-duotone", "trash-bin-trash-bold-duotone", "share-bold-duotone", "download-bold-duotone", "check-circle-bold-duotone", "danger-circle-bold-duotone", "info-circle-bold-duotone", "close-circle-bold-duotone"],
        "broken": ["home-2-broken", "magnifer-broken", "bell-broken", "user-broken", "heart-broken", "star-broken", "settings-broken", "add-circle-broken", "pen-broken", "trash-bin-trash-broken", "share-broken", "download-broken", "check-circle-broken", "danger-circle-broken", "info-circle-broken", "close-circle-broken"],
     }},
    {"name": "Hugeicons", "prefix": "hugeicons", "character": "rounded and detailed",
     "styles": {
        "stroke": ["home-01", "search-01", "notification-01", "user", "favourite", "star", "settings-01", "add-01", "pencil-edit-01", "delete-02", "share-08", "download-01", "checkmark-circle-01", "alert-circle", "information-circle", "cancel-01"],
     }},
    {"name": "Material Design Icons", "prefix": "mdi", "character": "bold and recognizable",
     "styles": {
        "filled": ["home", "magnify", "bell", "account", "heart", "star", "cog", "plus", "pencil", "delete", "share-variant", "download", "check-circle", "alert-circle", "information", "close"],
        "outline": ["home-outline", "magnify-outline", "bell-outline", "account-outline", "heart-outline", "star-outline", "cog-outline", "plus", "pencil-outline", "delete-outline", "share-variant-outline", "download-outline", "check-circle-outline", "alert-circle-outline", "information-outline", "close"],
     }},
    {"name": "Akar Icons", "prefix": "akar-icons", "character": "rounded and playful",
     "styles": {
        "outline": ["home", "search", "bell", "person", "heart", "star", "gear", "plus", "pencil", "trash-can", "share-arrow", "download", "circle-check", "circle-alert", "info", "cross"],
     }},
]

CREDITS = "Icons via Iconify. Solar icons by 480 Design, CC BY 4.0."


# picks a random icon set and one of its styles
def generate_icons():
    icon_set = random.choice(ICON_SETS)
    style = random.choice(list(icon_set["styles"].keys()))
    names = icon_set["styles"][style]

    icons = {}
    for i in range(len(CONCEPTS)):
        icons[CONCEPTS[i]] = icon_set["prefix"] + ":" + names[i]

    result = {}
    result["set"] = icon_set
    result["style"] = style
    result["icons"] = icons
    return result


# returns the full iconify name of one icon like "ph:house-bold"
def icon_id(result, concept):
    return result["icons"][concept]


if __name__ == "__main__":
    result = generate_icons()
    print("picked:", result["set"]["name"], "-", result["style"])
    for concept in CONCEPTS:
        print(concept, icon_id(result, concept))
