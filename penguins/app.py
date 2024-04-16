# ALWAYS familiarize yourself with the dataset you are working with first

import seaborn as sns
from faicons import icon_svg

from shiny import reactive
from shiny.express import input, render, ui
import palmerpenguins
import importlib
import plotly.express as px
from shinywidgets import render_plotly

df = palmerpenguins.load_penguins()

# This is where it can get tricky

ui.page_opts(title="Alvaro King Penguins", fillable=True)

#make sure punctuation marks and indentions are correct

with ui.sidebar(title="Penguin Dashboard Filters"):
    ui.input_slider("mass", "Mass", 2000, 6000, 6000)
    ui.input_checkbox_group(
        "species",
        "Species",
        ["Adelie", "Gentoo", "Chinstrap"],
        selected=["Adelie", "Gentoo", "Chinstrap"],
    )
    ui.hr()
    ui.h6("Links")
    ui.a(
        "GitHub Source",
        href="https://alvaroquintero28.github.io/cintel-07/",
        target="_blank",
    )
    ui.a(
        "GitHub App",
        href="https://alvaroquintero28.github.io/cintel-07/",
        target="_blank",
    )
    ui.a(
        "GitHub Issues",
        href="https://github.com/alvaroquintero28/cintel-07/issues/2",
        target="_blank",
    )
    ui.a("PyShiny", href="https://shiny.posit.co/py/", target="_blank")
    ui.a(
        "Template: Basic Dashboard",
        href="https://shiny.posit.co/py/templates/dashboard/",
        target="_blank",
    )
    ui.input_radio_buttons("dark_mode", "Dark Mode:", ["Yes", "No"], selected="No")
    
    ui.a(
        "See also",
        href="https://github.com/denisecase/pyshiny-penguins-dashboard-express",
        target="_blank",
    )
    

# Hang in there you can do it
with ui.layout_column_wrap(fill=False):
    with ui.value_box(showcase=icon_svg("earlybirds")):
        "Number of penguins"

        @render.text
        def count():
            return filtered_df().shape[0]

    with ui.value_box(showcase=icon_svg("earlybirds")):
        "Average bill length"

        @render.text
        def bill_length():
            return f"{filtered_df()['bill_length_mm'].mean():.1f} mm"

    with ui.value_box(showcase=icon_svg("earlybirds")):
        "Average bill depth"

        @render.text
        def bill_depth():
            return f"{filtered_df()['bill_depth_mm'].mean():.1f} mm"


with ui.layout_columns():
    with ui.card(full_screen=True):
        ui.card_header("Bill Length vs. Bill Depth")

        @render_plotly
        def length_depth_plotly():
            return px.histogram(
                data_frame=filtered_df(),
                x="bill_length_mm",
                y="bill_depth_mm",
                color="species",
            )

    with ui.card(full_screen=True):
        ui.card_header("Penguin Data")

        @render.data_frame
        def summary_statistics():
            cols = [
                "species",
                "island",
                "bill_length_mm",
                "bill_depth_mm",
                "body_mass_g",
            ]
            return render.DataGrid(filtered_df()[cols], filters=True)


# It is starting to become reality

@reactive.calc
def filtered_df():
    filt_df = df[df["species"].isin(input.species())]
    filt_df = filt_df.loc[filt_df["body_mass_g"] < input.mass()]
    return filt_df

@reactive.effect
def _():
    if input.dark_mode() == "Yes":
        ui.update_dark_mode("dark")
    else:
        ui.update_dark_mode("light")

# Run it and see what happens
# Hope for the best
    
