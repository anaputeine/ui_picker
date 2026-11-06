# makes a new design system and shows it on the page when it loads and on every generate click

from pyscript import document, when

import color
import icons
import presets
import typography

status = document.querySelector("#status")
summary = document.querySelector("#summary")
generate_button = document.querySelector("#generate")
font_link = document.querySelector("#font-link")
root = document.documentElement

copy_font_button = document.querySelector("#copy-font-css")
copy_colors_button = document.querySelector("#copy-colors-css")
copy_icons_button = document.querySelector("#copy-icons-css")
copy_shape_button = document.querySelector("#copy-shape-css")

font_info = document.querySelector("#font-info")
icon_info = document.querySelector("#icon-info")

current = {}


# puts css variables on the page so they replace the ones in style.css
def set_variables(variables):
    for name in variables:
        root.style.setProperty(name, variables[name])


# shows the hex code next to each color name
def show_hex_codes(colors):
    rows = document.querySelectorAll(".color")
    for i in range(rows.length):
        row = rows[i]
        role = row.getAttribute("data-role")
        if role in colors:
            row.querySelector(".hex").textContent = colors[role]


# changes every icon on the page to the picked icon set
def show_icons(icon_result):
    elements = document.querySelectorAll("[data-concept]")
    for i in range(elements.length):
        element = elements[i]
        concept = element.getAttribute("data-concept")
        element.setAttribute("icon", icons.icon_id(icon_result, concept))


# lists each icon concept with the icon name picked for it, one per line
def icons_text(icon_result):
    lines = []
    for concept in icons.CONCEPTS:
        lines.append(concept + ": " + icons.icon_id(icon_result, concept))
    return "\n".join(lines)


# puts the css text on each copy button so script.js can copy it
def set_copy_buttons(type_result, palette, shape, icon_result):
    copy_font_button.setAttribute("data-css", typography.to_css(type_result))
    copy_colors_button.setAttribute("data-css", color.to_css(palette))
    copy_shape_button.setAttribute("data-css", presets.to_css(shape))
    copy_icons_button.setAttribute("data-css", icons_text(icon_result))


# makes one sentence about what was picked
def describe(type_result, palette, shape, icon_result):
    font_text = f"Font: {type_result['font']['name']}, scale {type_result['ratio']}, callout as {type_result['callout_type']}. "
    color_text = f"Colors: {palette['mode']} mode, {palette['harmony']}, {palette['mood']}. "
    shape_text = f"Shape: {shape['radius']} corners, {shape['shadow']} shadow, {shape['density']} spacing. "
    icon_text = f"Icons: {icon_result['set']['name']}, {icon_result['style']}."
    return font_text + color_text + shape_text + icon_text


# makes a new design system and puts it on the page
def generate():
    type_result = typography.generate_typography()
    palette = color.generate_palette()
    shape = presets.generate_presets(palette["mode"])
    icon_result = icons.generate_icons()

    font_link.href = typography.google_fonts_link(type_result["font"])

    set_variables(typography.css_variables(type_result))
    set_variables(color.css_variables(palette))
    set_variables(presets.css_variables(shape))

    show_hex_codes(palette["colors"])
    show_icons(icon_result)
    set_copy_buttons(type_result, palette, shape, icon_result)
    summary.textContent = describe(type_result, palette, shape, icon_result)

    font_info.textContent = f"{type_result['font']['name']}, scale {type_result['ratio']}, callout as {type_result['callout_type']}"
    icon_info.textContent = f"{icon_result['set']['name']}, {icon_result['style']}"

    current["typography"] = type_result
    current["palette"] = palette
    current["presets"] = shape
    current["icons"] = icon_result


# runs when the generate button is clicked
@when("click", "#generate")
def on_generate(event):
    generate()


generate()
generate_button.disabled = False
status.textContent = "Ready. Click Generate for a new design system."
