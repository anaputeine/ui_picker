# picks random corner roundness, shadows, spacing, border width and icon style

import random

RADIUS = {
    "sharp": {"small": 0, "large": 0},
    "subtle": {"small": 4, "large": 6},
    "soft": {"small": 8, "large": 12},
    "round": {"small": 12, "large": 20},
    "pill": {"small": 999, "large": 24},
}

SHADOWS = {
    "none": {
        "small": "none",
        "large": "none",
    },
    "subtle": {
        "small": "0 1px 2px rgba(0, 0, 0, ALPHA)",
        "large": "0 2px 8px rgba(0, 0, 0, ALPHA)",
    },
    "soft": {
        "small": "0 2px 8px rgba(0, 0, 0, ALPHA)",
        "large": "0 12px 32px rgba(0, 0, 0, ALPHA)",
    },
    "layered": {
        "small": "0 1px 2px rgba(0, 0, 0, ALPHA), 0 4px 12px rgba(0, 0, 0, ALPHA)",
        "large": "0 2px 4px rgba(0, 0, 0, ALPHA), 0 16px 40px rgba(0, 0, 0, ALPHA)",
    },
    "crisp": {
        "small": "3px 3px 0 var(--color-text)",
        "large": "6px 6px 0 var(--color-text)",
    },
}

SHADOW_ALPHA = {"light": "0.08", "dark": "0.4"}

SPACING_STEPS = [["xs", 1], ["sm", 2], ["md", 3], ["lg", 4], ["xl", 6], ["2xl", 8]]

DENSITY = {"compact": 0.875, "normal": 1.0, "airy": 1.25}

BASE_UNIT = 4

BORDER_WIDTHS = [1, 1, 1.5, 2]

ICON_WEIGHTS = ["light", "regular", "bold", "fill", "duotone"]

ICON_SIZES = [20, 24]

VALUE_NAMES = [
    "radius-small", "radius-large",
    "shadow-small", "shadow-large",
    "border-width", "icon-size",
    "space-xs", "space-sm", "space-md", "space-lg", "space-xl", "space-2xl",
    "button-padding-y", "button-padding-x", "button-min-height",
]


# turns a number into short text like 1.5 or 2
def number_to_text(number):
    text = str(round(number, 3))
    if text.endswith(".0"):
        text = text[:-2]
    return text


# turns pixels into rem text like 0.75rem
def px_to_rem(px):
    return number_to_text(px / 16) + "rem"


# picks shape, shadow, spacing and icon style, mode must match the palette
def generate_presets(mode):
    radius_name = random.choice(list(RADIUS.keys()))
    shadow_name = random.choice(list(SHADOWS.keys()))
    density_name = random.choice(list(DENSITY.keys()))
    icon_weight = random.choice(ICON_WEIGHTS)
    icon_size = random.choice(ICON_SIZES)

    if shadow_name == "crisp":
        border_width = 2
    else:
        border_width = random.choice(BORDER_WIDTHS)

    radius = RADIUS[radius_name]
    shadow = SHADOWS[shadow_name]
    alpha = SHADOW_ALPHA[mode]
    density = DENSITY[density_name]

    values = {}
    values["radius-small"] = str(radius["small"]) + "px"
    values["radius-large"] = str(radius["large"]) + "px"
    values["shadow-small"] = shadow["small"].replace("ALPHA", alpha)
    values["shadow-large"] = shadow["large"].replace("ALPHA", alpha)
    values["border-width"] = number_to_text(border_width) + "px"
    values["icon-size"] = str(icon_size) + "px"

    for step in SPACING_STEPS:
        name = step[0]
        times = step[1]
        values["space-" + name] = px_to_rem(BASE_UNIT * times * density)

    values["button-padding-y"] = px_to_rem(BASE_UNIT * 2.5 * density)
    values["button-padding-x"] = px_to_rem(BASE_UNIT * 5 * density)
    values["button-min-height"] = "2.75rem"

    presets = {}
    presets["radius"] = radius_name
    presets["shadow"] = shadow_name
    presets["density"] = density_name
    presets["border_width"] = border_width
    presets["icon_weight"] = icon_weight
    presets["icon_size"] = icon_size
    presets["values"] = values
    return presets


# returns the css classes for a phosphor icon like "ph-bold ph-house"
def icon_class(presets, icon_name):
    weight = presets["icon_weight"]
    if weight == "regular":
        start = "ph"
    else:
        start = "ph-" + weight
    return start + " ph-" + icon_name


# turns the values into css variables like --radius-small
def css_variables(presets):
    variables = {}
    for name in VALUE_NAMES:
        variables["--" + name] = presets["values"][name]
    return variables


# makes the css text that the user can copy
def to_css(presets):
    text = ":root {\n"
    for name in VALUE_NAMES:
        text = text + f"  --{name}: {presets['values'][name]};\n"
    text = text + "}"
    return text


if __name__ == "__main__":
    result = generate_presets("light")
    print("radius:", result["radius"])
    print("shadow:", result["shadow"])
    print("density:", result["density"])
    print("icons:", result["icon_weight"], result["icon_size"])
    print("example icon:", icon_class(result, "house"))
    print(to_css(result))
