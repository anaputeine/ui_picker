# makes a random color palette for a website

import math
import random

HARMONIES = {
    "complementary": [180],
    "analogous": [30, -30],
    "triadic": [120, 240],
    "split-complementary": [150, 210],
    "monochromatic": [0],
}

MOODS = {
    "muted": [0.07, 0.10],
    "balanced": [0.12, 0.16],
    "vivid": [0.17, 0.22],
}

STATUS_HUES = {"error": [15, 35], "warning": [55, 80], "success": [135, 165]}

TEXT_GOOD = 4.5
TEXT_BEST = 7.0
SHAPE_GOOD = 3.0

HEX_DIGITS = "0123456789abcdef"

ROLES = [
    "background", "surface", "border", "border-strong",
    "text", "text-muted",
    "primary", "primary-hover", "primary-pressed", "on-primary",
    "secondary", "secondary-hover", "secondary-pressed", "on-secondary",
    "disabled", "on-disabled",
    "accent", "icon", "focus",
    "error", "warning", "success",
]

CONTRAST_PAIRS = [
    ["text", "background", TEXT_BEST],
    ["text", "surface", TEXT_BEST],
    ["text-muted", "background", TEXT_GOOD],
    ["text-muted", "surface", TEXT_GOOD],
    ["on-primary", "primary", TEXT_GOOD],
    ["on-primary", "primary-hover", TEXT_GOOD],
    ["on-primary", "primary-pressed", TEXT_GOOD],
    ["on-secondary", "secondary", TEXT_GOOD],
    ["on-secondary", "secondary-pressed", TEXT_GOOD],
    ["primary", "background", SHAPE_GOOD],
    ["border-strong", "background", SHAPE_GOOD],
    ["border-strong", "surface", SHAPE_GOOD],
    ["accent", "background", SHAPE_GOOD],
    ["icon", "background", SHAPE_GOOD],
    ["focus", "background", SHAPE_GOOD],
    ["error", "background", TEXT_GOOD],
    ["warning", "background", TEXT_GOOD],
    ["success", "background", TEXT_GOOD],
]


# returns a random number between low and high
def random_between(low, high):
    return low + (high - low) * random.random()


# keeps a number between 0 and 1
def keep_in_range(number):
    if number < 0:
        return 0.0
    if number > 1:
        return 1.0
    return number


# turns an oklch color into red, green and blue light amounts
def oklch_to_rgb(color):
    lightness, chroma, hue = color
    angle = hue * math.pi / 180
    a = chroma * math.cos(angle)
    b = chroma * math.sin(angle)

    l = lightness + 0.3963377774 * a + 0.2158037573 * b
    m = lightness - 0.1055613458 * a - 0.0638541728 * b
    s = lightness - 0.0894841775 * a - 1.2914855480 * b
    l = l * l * l
    m = m * m * m
    s = s * s * s

    red = 4.0767416621 * l - 3.3077115913 * m + 0.2309699292 * s
    green = -1.2684380046 * l + 2.6097574011 * m - 0.3413193965 * s
    blue = -0.0041960863 * l - 0.7034186147 * m + 1.7076147010 * s
    return [red, green, blue]


# checks if a screen can show this color
def can_show(color):
    for amount in oklch_to_rgb(color):
        if amount < -0.0001 or amount > 1.0001:
            return False
    return True


# lowers the chroma until the screen can show the color
def fit_to_screen(color):
    if can_show(color):
        return color

    lightness, chroma, hue = color
    low = 0.0
    high = chroma
    for step in range(20):
        middle = (low + high) / 2
        if can_show((lightness, middle, hue)):
            low = middle
        else:
            high = middle
    return (lightness, low, hue)


# turns a light amount into the number a screen uses
def screen_value(amount):
    amount = keep_in_range(amount)
    if amount <= 0.0031308:
        return 12.92 * amount
    return 1.055 * amount ** (1 / 2.4) - 0.055


# turns an oklch color into a hex color like #2f6fdf
def to_hex(color):
    rgb = oklch_to_rgb(fit_to_screen(color))
    text = "#"
    for amount in rgb:
        value = round(screen_value(amount) * 255)
        text = text + HEX_DIGITS[value // 16] + HEX_DIGITS[value % 16]
    return text


# measures how bright a hex color looks to the eye
def brightness(hex_color):
    red = int(hex_color[1:3], 16)
    green = int(hex_color[3:5], 16)
    blue = int(hex_color[5:7], 16)

    channels = [red, green, blue]
    weights = [0.2126, 0.7152, 0.0722]
    total = 0.0
    for i in range(3):
        channel = channels[i] / 255
        if channel <= 0.04045:
            channel = channel / 12.92
        else:
            channel = ((channel + 0.055) / 1.055) ** 2.4
        total = total + weights[i] * channel
    return total


# returns the contrast between two colors, from 1 (none) to 21 (black on white)
def contrast(hex_a, hex_b):
    bright_a = brightness(hex_a)
    bright_b = brightness(hex_b)
    lighter = max(bright_a, bright_b)
    darker = min(bright_a, bright_b)
    return (lighter + 0.05) / (darker + 0.05)


# makes a color darker or lighter until it has enough contrast with the other color
def fix_contrast(color, other_hex, target, direction):
    lightness, chroma, hue = color
    for step in range(100):
        if contrast(to_hex((lightness, chroma, hue)), other_hex) >= target:
            break
        lightness = keep_in_range(lightness + 0.01 * direction)
        if lightness == 0 or lightness == 1:
            break
    return (lightness, chroma, hue)


# makes a color lighter or darker by the given amount
def shift(color, amount):
    lightness, chroma, hue = color
    return (keep_in_range(lightness + amount), chroma, hue)


# returns how far apart two hues are on the color wheel, from 0 to 180
def hue_distance(hue_a, hue_b):
    distance = abs(hue_a - hue_b) % 360
    if distance > 180:
        distance = 360 - distance
    return distance


# picks a random hue, skipping yellows in light mode
def pick_hue(mode):
    while True:
        hue = random.random() * 360
        if mode == "dark":
            return hue
        if hue < 85 or hue > 115:
            return hue


# makes a full color palette for the website
def generate_palette():
    if random.random() < 0.6:
        mode = "light"
    else:
        mode = "dark"

    hue = pick_hue(mode)
    harmony = random.choice(list(HARMONIES.keys()))
    accent_hue = (hue + random.choice(HARMONIES[harmony])) % 360
    mood = random.choice(list(MOODS.keys()))
    chroma = random_between(MOODS[mood][0], MOODS[mood][1])
    tint = random_between(0.004, 0.015)

    if mode == "light":
        away_from_background = -1
        background = (0.985, tint, hue)
        surface = (random.choice([1.0, 0.955]), tint, hue)
        border = (0.89, tint, hue)
        secondary = (min(background[0], surface[0]) - 0.05, 0.06, hue)
        disabled = (0.92, 0, hue)
        on_disabled = (0.65, 0, hue)
        text_start = 0.2
        muted_start = 0.5
        primary_start = random_between(0.5, 0.65)
        on_secondary_start = 0.4
        accent_start = 0.55
        status_start = 0.5
    else:
        away_from_background = 1
        dark = random_between(0.16, 0.2)
        background = (dark, tint, hue)
        surface = (dark + 0.05, tint, hue)
        border = (dark + 0.12, tint, hue)
        secondary = (dark + 0.1, 0.06, hue)
        disabled = (dark + 0.08, 0, hue)
        on_disabled = (0.5, 0, hue)
        text_start = 0.95
        muted_start = 0.72
        primary_start = random_between(0.65, 0.78)
        on_secondary_start = 0.85
        accent_start = 0.75
        status_start = 0.75

    background_hex = to_hex(background)
    surface_hex = to_hex(surface)

    if mode == "light" and surface[0] < background[0]:
        hardest_hex = surface_hex
    elif mode == "dark":
        hardest_hex = surface_hex
    else:
        hardest_hex = background_hex

    border_strong = fix_contrast(border, hardest_hex, SHAPE_GOOD, away_from_background)
    text = fix_contrast((text_start, tint, hue), hardest_hex, TEXT_BEST, away_from_background)
    text_muted = fix_contrast((muted_start, tint * 2, hue), hardest_hex, TEXT_GOOD, away_from_background)

    primary = (primary_start, chroma, hue)
    primary = fix_contrast(primary, background_hex, SHAPE_GOOD, away_from_background)
    dark_ink = to_hex((0.18, tint, hue))
    with_white = fix_contrast(primary, "#ffffff", TEXT_GOOD, -1)

    if mode == "light" and primary[0] - with_white[0] <= 0.15:
        primary = with_white
        on_primary_hex = "#ffffff"
        away_from_ink = -1
    else:
        primary_hex = to_hex(primary)
        if contrast("#ffffff", primary_hex) >= contrast(dark_ink, primary_hex):
            on_primary_hex = "#ffffff"
            away_from_ink = -1
        else:
            on_primary_hex = dark_ink
            away_from_ink = 1
        primary = fix_contrast(primary, on_primary_hex, TEXT_GOOD, away_from_ink)

    primary_hover = shift(primary, 0.05 * away_from_ink)
    primary_pressed = shift(primary, 0.10 * away_from_ink)

    secondary_hover = shift(secondary, 0.05 * away_from_background)
    secondary_pressed = shift(secondary, 0.10 * away_from_background)
    on_secondary = (on_secondary_start, chroma, hue)
    on_secondary = fix_contrast(on_secondary, to_hex(secondary_pressed), TEXT_GOOD, away_from_background)

    if harmony == "monochromatic":
        accent_start = keep_in_range(primary[0] + 0.15 * away_from_background)

    accent = (accent_start, chroma, accent_hue)
    accent = fix_contrast(accent, background_hex, SHAPE_GOOD, away_from_background)
    icon = random.choice([text_muted, primary, accent])

    status_chroma = chroma
    if status_chroma < 0.10:
        status_chroma = 0.10
    if status_chroma > 0.18:
        status_chroma = 0.18

    status = {}
    for name in STATUS_HUES:
        low = STATUS_HUES[name][0]
        high = STATUS_HUES[name][1]
        status_hue = random_between(low, high)
        status_lightness = status_start

        if hue_distance(status_hue, hue) < 30:
            if hue_distance(low, hue) > hue_distance(high, hue):
                status_hue = low
            else:
                status_hue = high

        if hue_distance(status_hue, hue) < 30:
            status_lightness = keep_in_range(primary[0] + 0.15 * away_from_background)

        start = (status_lightness, status_chroma, status_hue)
        status[name] = fix_contrast(start, background_hex, TEXT_GOOD, away_from_background)

    colors = {}
    colors["background"] = background_hex
    colors["surface"] = surface_hex
    colors["border"] = to_hex(border)
    colors["border-strong"] = to_hex(border_strong)
    colors["text"] = to_hex(text)
    colors["text-muted"] = to_hex(text_muted)
    colors["primary"] = to_hex(primary)
    colors["primary-hover"] = to_hex(primary_hover)
    colors["primary-pressed"] = to_hex(primary_pressed)
    colors["on-primary"] = on_primary_hex
    colors["secondary"] = to_hex(secondary)
    colors["secondary-hover"] = to_hex(secondary_hover)
    colors["secondary-pressed"] = to_hex(secondary_pressed)
    colors["on-secondary"] = to_hex(on_secondary)
    colors["disabled"] = to_hex(disabled)
    colors["on-disabled"] = to_hex(on_disabled)
    colors["accent"] = to_hex(accent)
    colors["icon"] = to_hex(icon)
    colors["focus"] = to_hex(text)
    colors["error"] = to_hex(status["error"])
    colors["warning"] = to_hex(status["warning"])
    colors["success"] = to_hex(status["success"])

    palette = {}
    palette["mode"] = mode
    palette["base_hue"] = round(hue, 1)
    palette["harmony"] = harmony
    palette["mood"] = mood
    palette["colors"] = colors
    palette["checks"] = contrast_checks(colors)
    return palette


# checks the contrast of every text and background pair that matters
def contrast_checks(colors):
    checks = []
    for pair in CONTRAST_PAIRS:
        front = pair[0]
        back = pair[1]
        target = pair[2]
        ratio = round(contrast(colors[front], colors[back]), 2)
        checks.append([front, back, ratio, target])
    return checks


# turns the colors into css variables like --color-primary
def css_variables(palette):
    variables = {}
    for role in ROLES:
        variables["--color-" + role] = palette["colors"][role]
    return variables


# makes the css text that the user can copy
def to_css(palette):
    text = ":root {\n"
    for role in ROLES:
        text = text + f"  --color-{role}: {palette['colors'][role]};\n"
    text = text + "}"
    return text


if __name__ == "__main__":
    result = generate_palette()
    print("mode:", result["mode"])
    print("hue:", result["base_hue"])
    print("harmony:", result["harmony"])
    print("mood:", result["mood"])
    print(to_css(result))
    print()
    for check in result["checks"]:
        if check[2] >= check[3]:
            mark = "pass"
        else:
            mark = "FAIL"
        print(mark, check[0], "on", check[1], check[2], "needs", check[3])
