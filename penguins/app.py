# IMPORT the packages we need (or might want to use) first.
# NOTE: Each package should be added to requirements.txt,
#       so the packages can be INSTALLED into the project virtual environment.

import faicons as fa  # For using font awesome in cards
import palmerpenguins  # This package provides the Palmer Penguins dataset
import pandas as pd  # Pandas for data manipulation, required by plotly.express
import plotly.express as px  # Plotly Express for making Plotly plots
import seaborn as sns  # Seaborn for making Seaborn plots
from shinywidgets import render_plotly  # For rendering Plotly plots
from shiny import reactive, render, req  # To define reactive calculations
from shiny.express import input, ui  # To define the user interface

# ALWAYS familiarize yourself with the dataset you are working with first.
# Column names for the penguins dataset include:
# - species: penguin species (Chinstrap, Adelie, or Gentoo)
# - island: island name (Dream, Torgersen, or Biscoe) in the Palmer Archipelago
# - bill_length_mm: length of the bill in millimeters
# - bill_depth_mm: depth of the bill in millimeters
# - flipper_length_mm: length of the flipper in millimeters
# - body_mass_g: body mass in grams
# - sex: MALE or FEMALE

# Load the dataset into a pandas DataFrame.
# Use the built-in function to load the Palmer Penguins dataset
penguins_df = palmerpenguins.load_penguins()


# Define the Shiny UI Page layout
# Call the ui.page_opts() function to set the page title and make the page fillable
ui.page_opts(title="PyShiny Express: Palmer Penguins Example", fillable=True)

# Add a Shiny UI sidebar for user interaction
# Use the ui.sidebar() function to create a sidebar
# Set the open parameter to "desktop" to make the sidebar open by default on a desktop
# Use a with block to add content to the sidebar
# Using Shiny Express there are no punctuation between ui elements
# Use the ui.h2() function to add a 2nd level header to the sidebar
#   pass in a string argument (in quotes) to set the header text
# Use ui.input_selectize() to create a dropdown input
#   pass in three arguments:
#   the name of the input (in quotes)
#   the label for the input (in quotes)
#   a list of options for the input (in square brackets)
# Use ui.input_numeric() to create a numeric input
#   pass in two arguments:
#   the name of the input (in quotes)
#   the label for the input (in quotes)
# Use ui.input_slider() to create a slider input
#   pass in four arguments:
#   the name of the input (in quotes)
#   the label for the input (in quotes)
#   the minimum value for the input (as an integer)
#   the maximum value for the input (as an integer)
#   the default value for the input (as an integer)
# Use ui.input_checkbox_group() to create a checkbox group input
#   pass in five arguments:
#   the name of the input (in quotes)
#   the label for the input (in quotes)
#   a list of options for the input (in square brackets)
#   a list of selected options for the input (in square brackets)
#   a boolean value (True or False) to set the input inline or not
# Use ui.hr() to add a horizontal rule to the sidebar
# Use ui.a() to add a hyperlink to the sidebar
#   pass in two arguments:
#   the text for the hyperlink (in quotes)
#   the URL for the hyperlink (in quotes)
#   set the target parameter to "_blank" to open the link in a new tab
# When passing in multiple arguments to a function, separate them with commas.

with ui.sidebar(open="desktop"):

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

# Everything not in the sidebar is in the main panel
# Tables and charts
# Use a with block to add content to the ui card

# The @ signs are decorators, which are used to modify the function that follows them.
# It's a concise way to wrap the following function in a function that will modify it.
# These decorators are part of the PyShiny package.
# They are used to render the Plotly and Seaborn plots in the UI.
# Everything in the function (after the colon) will appear in the card

with ui.card(full_screen=True):
    "Plotly Histogram"

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
    "Seaborn Histogram"

    @render.plot(alt="A Seaborn histogram on penguin body mass in grams.")
    def seaborn_histogram():
        # Create a histogram using Seaborn (which we aliased as sns)
        # Seaborn charts are a bit different
        # You can't just return the chart - instead, we create
        # a chart object, and call methods on it to set the title,
        # x-axis label, and y-axis label
        # Call sns.histplot() function
        # Pass in three arguments:
        # the data as a pandas DataFrame (first argument, unnamed)
        # a named argument named x set to the value returned from the input.selected_attribute() function
        # a named argument bins set to the user input bin count returned from the function input.seaborn_bin_count() function
        # Return the histplot object we created and customized
        histplot = sns.histplot(
            data=penguins_df, x="body_mass_g", bins=input.seaborn_bin_count()
        )
        histplot.set_title("Palmer Penguins")
        histplot.set_xlabel("Mass (g)")
        histplot.set_ylabel("Count")
        return histplot


with ui.card(full_screen=True):
    "Plotly Scatterplot: Species"

    @render_plotly
    def plotly_scatterplot():
        # Create a Plotly scatterplot using Plotly Express
        # Call px.scatter() function
        # Pass in six arguments:
        # the data as a pandas DataFrame (first argument, unnamed)
        # a named argument named x set to the value returned from the input.selected_attribute() function
        # a named argument named y set to the string "body_mass_g"
        # a named argument named color set to the string "species"
        # a named argument named title set to the string "Penguins Plot (Plotly Express)"
        # a named argument named labels set to a dictionary with two key-value pairs
        #    the first key is "bill_length_mm" and the value is "Bill Length (mm)"
        #    the second key is "body_mass_g" and the value is "Body Mass (g)"
        # a named argument named size_max set to the integer 8
        # Return the scatterplot created by the px.scatter() function
        return px.scatter(
            filtered_data(),
            x="bill_length_mm",
            y="body_mass_g",
            color="species",
            title="Penguins Plot (Plotly Express))",
            labels={
                "bill_length_mm": "Bill Length (mm)",
                "body_mass_g": "Body Mass (g)",
            },
            size_max=8,
        )


# --------------------------------------------------------
# Reactive calculations and effects
# --------------------------------------------------------

# Add a reactive calculation to filter the data
# By decorating the function with @reactive, we can use the function to filter the data
# The function will be called whenever an input functions used to generate that output changes.
# Any output that depends on the reactive function (e.g., filtered_data()) will be updated when the data changes.

# In this case, only the last chart uses the filtered data,
# so only the last chart will be updated when the data changes.


@reactive.calc
def filtered_data():

    # The required function req() is used to ensure that
    # the input.selected_species() function is not empty.
    req(input.selected_species())

    # If not empty, filter the data otherwise, just return the original data

    # Use the isin() method to filter the DataFrame
    # The method returns a boolean Series with the same index as the original DataFrame
    # Each row is:
    #   True if the species is in the input.selected_species() list
    #   False if the species is not
    isSpeciesMatch = penguins_df["species"].isin(input.selected_species())

    # Use the boolean filter mask in square brackets to filter the DataFrame
    # Return the filtered DataFrame when the function is triggered
    # Filter masks can be combined with the & operator for AND and the | operator for OR
    return penguins_df[isSpeciesMatch]


# Additional Python Notes
# ------------------------
# Capitalization matters in Python. Python is case-sensitive: min and Min are different.
# Spelling matters in Python. You must match the spelling of functions and variables exactly.
# Indentation matters in Python. Indentation is used to define code blocks and must be consistent.

# Functions
# ---------
# Functions are used to group code together and make it more readable and reusable.
# We define custom functions that can be called later in the code.
# Functions are blocks of logic that can take inputs, perform work, and return outputs.

# Defining Functions
# ------------------
# Define a function using the def keyword, followed by the function name, parentheses, and a colon. 
# The function name should describe what the function does.
# In the parentheses, specify the inputs needed as arguments the function takes.
# For example:
#    The function filtered_data() takes no arguments.
#    The function between(min, max) takes two arguments, a minimum and maximum value.
#    Arguments can be positional or keyword arguments, labeled with a parameter name.

# The function body is indented (consistently!) after the colon. 
# Use the return keyword to return a value from a function.
    
# Calling Functions
# -----------------
# Call a function by using its name followed by parentheses and any required arguments.
    
# Decorators
# ----------
# Use the @ symbol to decorate a function with a decorator.
# Decorators a concise way of calling a function on a function.
# We don't typically write decorators, but we often use them.
    