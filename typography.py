# picks a random font and makes text styles for title, subtitle, description, callout and body

import random

FONTS = [
    {"name": "Inter", "category": "sans", "min_weight": 100, "max_weight": 900, "has_italic": True,
     "title_weights": [600, 700, 800], "body_weight": 400, "letter_spacing": -0.02, "size_boost": 1.0},
    {"name": "Montserrat", "category": "sans", "min_weight": 100, "max_weight": 900, "has_italic": True,
     "title_weights": [600, 700, 800], "body_weight": 400, "letter_spacing": -0.01, "size_boost": 1.0},
    {"name": "Raleway", "category": "sans", "min_weight": 100, "max_weight": 900, "has_italic": True,
     "title_weights": [600, 700, 800], "body_weight": 400, "letter_spacing": 0.0, "size_boost": 1.0},
    {"name": "Work Sans", "category": "sans", "min_weight": 100, "max_weight": 900, "has_italic": True,
     "title_weights": [500, 600, 700], "body_weight": 400, "letter_spacing": -0.01, "size_boost": 1.0},
    {"name": "DM Sans", "category": "sans", "min_weight": 100, "max_weight": 900, "has_italic": True,
     "title_weights": [500, 600, 700], "body_weight": 400, "letter_spacing": -0.02, "size_boost": 1.0},
    {"name": "Manrope", "category": "sans", "min_weight": 200, "max_weight": 800, "has_italic": False,
     "title_weights": [600, 700, 800], "body_weight": 400, "letter_spacing": -0.02, "size_boost": 1.0},
    {"name": "Space Grotesk", "category": "sans", "min_weight": 300, "max_weight": 700, "has_italic": False,
     "title_weights": [500, 600, 700], "body_weight": 400, "letter_spacing": -0.02, "size_boost": 1.0},
    {"name": "Plus Jakarta Sans", "category": "sans", "min_weight": 200, "max_weight": 800, "has_italic": True,
     "title_weights": [600, 700, 800], "body_weight": 400, "letter_spacing": -0.02, "size_boost": 1.0},
    {"name": "Outfit", "category": "sans", "min_weight": 100, "max_weight": 900, "has_italic": False,
     "title_weights": [500, 600, 700], "body_weight": 400, "letter_spacing": -0.01, "size_boost": 1.0},
    {"name": "Sora", "category": "sans", "min_weight": 100, "max_weight": 800, "has_italic": False,
     "title_weights": [600, 700], "body_weight": 300, "letter_spacing": -0.02, "size_boost": 1.0},
    {"name": "Lexend", "category": "sans", "min_weight": 100, "max_weight": 900, "has_italic": False,
     "title_weights": [500, 600, 700], "body_weight": 300, "letter_spacing": -0.01, "size_boost": 1.0},
    {"name": "Archivo", "category": "sans", "min_weight": 100, "max_weight": 900, "has_italic": True,
     "title_weights": [700, 800, 900], "body_weight": 400, "letter_spacing": -0.01, "size_boost": 1.0},
    {"name": "Rubik", "category": "sans", "min_weight": 300, "max_weight": 900, "has_italic": True,
     "title_weights": [500, 600, 700], "body_weight": 400, "letter_spacing": 0.0, "size_boost": 1.0},
    {"name": "Figtree", "category": "sans", "min_weight": 300, "max_weight": 900, "has_italic": True,
     "title_weights": [600, 700, 800], "body_weight": 400, "letter_spacing": -0.01, "size_boost": 1.0},
    {"name": "Nunito", "category": "sans", "min_weight": 200, "max_weight": 900, "has_italic": True,
     "title_weights": [700, 800, 900], "body_weight": 400, "letter_spacing": 0.0, "size_boost": 1.0},
    {"name": "Bricolage Grotesque", "category": "sans", "min_weight": 200, "max_weight": 800, "has_italic": False,
     "title_weights": [600, 700, 800], "body_weight": 400, "letter_spacing": -0.03, "size_boost": 1.0},
    {"name": "Instrument Sans", "category": "sans", "min_weight": 400, "max_weight": 700, "has_italic": True,
     "title_weights": [600, 700], "body_weight": 400, "letter_spacing": -0.02, "size_boost": 1.0},
    {"name": "Open Sans", "category": "sans", "min_weight": 300, "max_weight": 800, "has_italic": True,
     "title_weights": [600, 700, 800], "body_weight": 400, "letter_spacing": -0.01, "size_boost": 1.0},

    {"name": "Lora", "category": "serif", "min_weight": 400, "max_weight": 700, "has_italic": True,
     "title_weights": [600, 700], "body_weight": 400, "letter_spacing": 0.0, "size_boost": 1.0},
    {"name": "Bitter", "category": "serif", "min_weight": 100, "max_weight": 900, "has_italic": True,
     "title_weights": [600, 700, 800], "body_weight": 400, "letter_spacing": -0.01, "size_boost": 1.0},
    {"name": "Fraunces", "category": "serif", "min_weight": 100, "max_weight": 900, "has_italic": True,
     "title_weights": [600, 700, 800, 900], "body_weight": 400, "letter_spacing": -0.02, "size_boost": 1.0},
    {"name": "EB Garamond", "category": "serif", "min_weight": 400, "max_weight": 800, "has_italic": True,
     "title_weights": [500, 600, 700], "body_weight": 400, "letter_spacing": 0.0, "size_boost": 1.1},
    {"name": "Source Serif 4", "category": "serif", "min_weight": 200, "max_weight": 900, "has_italic": True,
     "title_weights": [600, 700], "body_weight": 400, "letter_spacing": -0.01, "size_boost": 1.0},
    {"name": "Crimson Pro", "category": "serif", "min_weight": 200, "max_weight": 900, "has_italic": True,
     "title_weights": [500, 600, 700], "body_weight": 400, "letter_spacing": 0.0, "size_boost": 1.12},
    {"name": "Literata", "category": "serif", "min_weight": 200, "max_weight": 900, "has_italic": True,
     "title_weights": [600, 700], "body_weight": 400, "letter_spacing": -0.01, "size_boost": 1.0},
    {"name": "Newsreader", "category": "serif", "min_weight": 200, "max_weight": 800, "has_italic": True,
     "title_weights": [500, 600, 700], "body_weight": 400, "letter_spacing": -0.01, "size_boost": 1.05},
    {"name": "Alegreya", "category": "serif", "min_weight": 400, "max_weight": 900, "has_italic": True,
     "title_weights": [700, 800], "body_weight": 400, "letter_spacing": 0.0, "size_boost": 1.08},
    {"name": "Roboto Slab", "category": "serif", "min_weight": 100, "max_weight": 900, "has_italic": False,
     "title_weights": [600, 700], "body_weight": 400, "letter_spacing": -0.01, "size_boost": 1.0},

    {"name": "JetBrains Mono", "category": "mono", "min_weight": 100, "max_weight": 800, "has_italic": True,
     "title_weights": [700, 800], "body_weight": 400, "letter_spacing": -0.02, "size_boost": 0.95},
    {"name": "Fira Code", "category": "mono", "min_weight": 300, "max_weight": 700, "has_italic": False,
     "title_weights": [600, 700], "body_weight": 400, "letter_spacing": -0.02, "size_boost": 0.95},
]

BACKUP_FONTS = {
    "sans": "system-ui, sans-serif",
    "serif": "Georgia, serif",
    "mono": "ui-monospace, monospace",
}

SCALE_RATIOS = [1.2, 1.25, 1.333, 1.414, 1.5]

BASE_SIZES = [15, 16, 17, 18]

ROLES = ["title", "subtitle", "description", "callout", "body"]

PROPERTIES = ["font_family", "font_size", "font_weight", "line_height",
              "letter_spacing", "font_style", "text_transform"]


# keeps the weight inside the range the font supports
def fit_weight(weight, font):
    if weight < font["min_weight"]:
        return font["min_weight"]
    if weight > font["max_weight"]:
        return font["max_weight"]
    return weight


# rounds a number to the nearest hundred
def round_to_hundred(number):
    return int(number / 100 + 0.5) * 100


# turns a number into short text like 1.25 or 2
def number_to_text(number):
    text = str(round(number, 3))
    if text.endswith(".0"):
        text = text[:-2]
    return text


# makes the css style for one text role
def make_style(font, size, weight, line_height, spacing=0.0, italic=False, uppercase=False):
    style = {}
    style["font_family"] = f'"{font["name"]}", {BACKUP_FONTS[font["category"]]}'
    style["font_size"] = number_to_text(size / 16) + "rem"
    style["font_weight"] = str(fit_weight(weight, font))
    style["line_height"] = number_to_text(line_height)

    if spacing == 0:
        style["letter_spacing"] = "0"
    else:
        style["letter_spacing"] = number_to_text(spacing) + "em"

    if italic:
        style["font_style"] = "italic"
    else:
        style["font_style"] = "normal"

    if uppercase:
        style["text_transform"] = "uppercase"
    else:
        style["text_transform"] = "none"

    return style


# picks a random font and makes styles for all text roles
def generate_typography():
    font = random.choice(FONTS)
    ratio = random.choice(SCALE_RATIOS)
    base = random.choice(BASE_SIZES) * font["size_boost"]
    spacing = font["letter_spacing"]

    if ratio < 1.3:
        title_steps = 4
    else:
        title_steps = 3

    title_weight = random.choice(font["title_weights"])
    body_weight = font["body_weight"]
    subtitle_weight = round_to_hundred((title_weight + body_weight) / 2)

    if font["has_italic"]:
        callout_type = random.choice(["label", "emphasis", "italic"])
    else:
        callout_type = random.choice(["label", "emphasis"])

    if callout_type == "label":
        callout_weight = max(600, body_weight + 200)
        callout = make_style(font, base * 0.875, callout_weight, 1.4, 0.08, False, True)
    elif callout_type == "emphasis":
        callout = make_style(font, base * ratio, subtitle_weight, 1.4)
    else:
        callout = make_style(font, base * ratio, body_weight, 1.4, 0.0, True)

    body_line_height = random.choice([1.5, 1.6, 1.7])

    roles = {}
    roles["title"] = make_style(font, base * ratio ** title_steps, title_weight, 1.1, spacing)
    roles["subtitle"] = make_style(font, base * ratio ** 2, subtitle_weight, 1.25, spacing / 2)
    roles["description"] = make_style(font, base * ratio, body_weight, 1.5)
    roles["callout"] = callout
    roles["body"] = make_style(font, base, body_weight, body_line_height)

    typography = {}
    typography["font"] = font
    typography["ratio"] = ratio
    typography["callout_type"] = callout_type
    typography["roles"] = roles
    return typography


# makes the google fonts link that loads the chosen font
def google_fonts_link(font):
    name = font["name"].replace(" ", "+")
    weights = f'{font["min_weight"]}..{font["max_weight"]}'

    if font["has_italic"]:
        settings = f"ital,wght@0,{weights};1,{weights}"
    else:
        settings = f"wght@{weights}"

    return f"https://fonts.googleapis.com/css2?family={name}:{settings}&display=swap"


# turns the styles into css variables like --title-font-size
def css_variables(typography):
    variables = {}
    for role in ROLES:
        style = typography["roles"][role]
        for prop in PROPERTIES:
            name = "--" + role + "-" + prop.replace("_", "-")
            variables[name] = style[prop]
    return variables


# makes the css text that the user can copy
def to_css(typography):
    variables = css_variables(typography)
    text = ":root {\n"
    for role in ROLES:
        for prop in PROPERTIES:
            name = "--" + role + "-" + prop.replace("_", "-")
            text = text + f"  {name}: {variables[name]};\n"
    text = text + "}"
    return text


if __name__ == "__main__":
    result = generate_typography()
    print("font:", result["font"]["name"])
    print("ratio:", result["ratio"])
    print("callout:", result["callout_type"])
    print(google_fonts_link(result["font"]))
    print(to_css(result))
