# ALWAYS familiarize yourself with the dataset you are working with first.

import faicons as fa  # For using font awesome in cards
import palmerpenguins  # This package provides the Palmer Penguins dataset
import pandas as pd  # Pandas for data manipulation, required by plotly.express
import plotly.express as px  # Plotly Express for making Plotly plots
import seaborn as sns  # Seaborn for making Seaborn plots
from shinywidgets import render_plotly  # For rendering Plotly plots
from shiny import reactive, render, req  # To define reactive calculations
from shiny.express import input, ui  # To define the user interface



penguins_df = palmerpenguins.load_penguins()

# This is where it can get tricky
ui.page_opts(
    title="PyShiny Express: Palmer Penguins Example", 
    fillable=True
    )

#make sure punctuation marks and indentions are correct

with ui.sidebar(open="open"):

    ui.h2("Sidebar")

    ui.input_selectize(
        "selected_attribute",
        "Select Plotly Attribute",
        ["bill_length_mm", "bill_depth_mm", "flipper_length_mm", "body_mass_g", "year"],
    )

    ui.input_numeric("plotly_bin_count", "Number of Plotly bins", 30)

    ui.input_slider("seaborn_bin_count", "Number of Seaborn bins", 1, 100, 20)

    ui.hr()

    ui.input_checkbox_group(
        "selected_species",
        "Species in Scatterplot",
        ["Adelie", "Gentoo", "Chinstrap"],
        selected=["Adelie", "Gentoo", "Chinstrap"],
        inline=True,
    )

    ui.hr()
    ui.h6("Links:")
    ui.a(
        "GitHub Source",
        href="https://github.com/denisecase/pyshiny-penguins-dashboard-express",
        target="_blank",
    )
    ui.a(
        "GitHub App",
        href="https://denisecase.github.io/pyshiny-penguins-dashboard-express/",
        target="_blank",
    )
    ui.a("PyShiny", href="https://shiny.posit.co/py/", target="_blank")
    ui.a(
        "PyShiny Express",
        href="hhttps://shiny.posit.co/blog/posts/shiny-express/",
        target="_blank",
    )
    ui.a(
        "See the Code",
        href="https://shiny.posit.co/py/docs/user-interfaces.html#basic-dashboard",
        target="_blank",
    )
    ui.a(
        "Output: DataGrid",
        href="https://shiny.posit.co/py/components/outputs/datatable/",
        target="_blank",
    )
    ui.a(
        "Output: DataTable",
        href="https://shiny.posit.co/py/components/outputs/datatable/",
        target="_blank",
    )
    ui.a(
        "Output: Plotly Scatterplot",
        href="https://shiny.posit.co/py/components/outputs/plot-plotly/",
        target="_blank",
    )
    ui.a(
        "Output: Seaborn Histogram",
        href="https://shiny.posit.co/py/components/outputs/plot-seaborn/",
        target="_blank",
    )

# Hang in there you can do it

with ui.layout_columns():

    with ui.card(full_screen=True):
        ui.card_header("Plotly Histogram")

        @render_plotly
        def plotly_histogram():
            # Create a histogram using Plotly Express (aliased as px)
            # Call px.histogram() function
            # Pass in three arguments:
            # the data as a pandas DataFrame (first argument, unnamed)
            # a named argument named x set to the value returned from the input.selected_attribute() function
            # a named argument nbins set to the user input bin count returned from the function input.plotly_bin_count() function
            # Return the histogram created by the px.histogram() function
            return px.histogram(
                penguins_df, x=input.selected_attribute(), nbins=input.plotly_bin_count()
            )


    with ui.card(full_screen=True):
        ui.card_header("Seaborn Histogram")

        @render.plot(alt="A Seaborn histogram on penguin body mass in grams.")
        def seaborn_histogram():

            
            histplot = sns.histplot(
                data=penguins_df, x="body_mass_g", bins=input.seaborn_bin_count()
            )
            histplot.set_title("Palmer Penguins")
            histplot.set_xlabel("Mass (g)")
            histplot.set_ylabel("Count")
            return histplot


with ui.card(full_screen=True):
    ui.card_header("Plotly Scatterplot: Species")

    @render_plotly
    def plotly_scatterplot():
        # Almost got it 
        
        return px.scatter(
            filtered_data(),
            x="bill_length_mm",
            y="body_mass_g",
            color="species",
            title="Penguins Plot (Plotly Express)",
            labels={
                "bill_length_mm": "Bill Length (mm)",
                "body_mass_g": "Body Mass (g)",
            },
            size_max=8, # set the maximum marker size
        )


# It is starting to become reality


@reactive.calc
def filtered_data():

    # The required function req() is used to ensure that
    # the input.selected_species() function is not empty.
    req(input.selected_species())

   
    isSpeciesMatch = penguins_df["species"].isin(input.selected_species())

    # Use the boolean filter mask in square brackets to filter the DataFrame
    # Return the filtered DataFrame when the function is triggered
    # Filter masks can be combined with the & operator for AND and the | operator for OR
    return penguins_df[isSpeciesMatch]


# Run it and see what happens
    
