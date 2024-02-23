# PyShiny Express: Palmer Penguins Dashboard

- Repository: [pyshiny-penguins-dashboard-express](https://github.com/denisecase/pyshiny-penguins-dashboard-express)
- Live App: [Penguins Dashboard (Express)](https://denisecase.github.io/pyshiny-penguins-dashboard-express/)

Run and publish interactive apps using PyShiny Express and GitHub Pages.

## Data Description

This app uses the Palmer Penguins dataset which includes three penguin species observed on three islands in the Palmer Archipelago, Antarctica.
The data has been made available by Dr. Kristen Gorman and the Palmer Station, Antarctica LTER, a member of the Long Term Ecological Research Network.

Column names for the penguins dataset include:

- species: penguin species (Chinstrap, Adelie, or Gentoo)
- island: island name (Dream, Torgersen, or Biscoe) in the Palmer Archipelago
- bill_length_mm: length of the bill in millimeters
- bill_depth_mm: depth of the bill in millimeters
- flipper_length_mm: length of the flipper in millimeters
- body_mass_g: body mass in grams
- sex: MALE or FEMALE

See: <https://allisonhorst.github.io/palmerpenguins/>

## Data Cleaning and Transformation

The data includes some missing values.
We generally clean the data by removing rows with missing values and possibly transform the data to use columns that are more easily read (or use labels on charts and tables).

## Source

From <https://shiny.posit.co/py/docs/user-interfaces.html>.
This version has been modified slightly for hosting with GitHub Pages.

## Prerequisites

Before you start, have the following installed:

- **Python**: Install the most recent version from [python.org](https://www.python.org/downloads/).
- **Git**: Download and install Git from [git-scm.com](https://git-scm.com/downloads).
- **Visual Studio Code (VS Code)**: Download from [code.visualstudio.com](https://code.visualstudio.com/).
- **VS Code Extensions**: Install the Python extension for VS Code.

### Configurations

- **Configure Git**: Set up your user name and email with Git using the following commands in your terminal:

  ```shell
  git config --global user.name "Your Name"
  git config --global user.email "youremail@example.com"

## Set up the Project

### Commands

Commands are operating system-specific.
These commands are for Windows users.
On Mac/Linux, generally use `python3` instead of `py`.
Edit your README.md to reflect the commands that work on your machine.

### Verify Installations

1. Open project folder in VS Code.
2. Open a new terminal (on Windows, ensure the terminal type is PowerShell (not the old cmd)
3. Run the following commands in the terminal one at a time::

```shell
py --version
git --version
git config user.name
git config user.email
```

## Python Project Virtual Environment

Run the following commands in the terminal to set up a project virtual environment and install the necessary packages.
Run them from the root project folder (e.g. pyshiny-penguins-dashboard-express).
Use PowerShell on Windows or the terminal on macOS and Linux.

### Create a Project Virtual Environment (generally one-time setup)

Create a project virtual environment in the .venv folder of the project root directory.

  ```shell
  py -m venv .venv`
  ```

### Activate the Project Virtual Environment (when you work on the project)

Once the project virtual environment exists,
 we activate the virtual environment to work on the project - or when we open a new terminal.
We can verify our environment is active when (.venv) appears in the terminal prompt.

On Windows:

  ```shell
  .venv\Scripts\Activate
  ```

On macOS and Linux:

  ```shell
  source .venv/bin/activate
  ```

We also need to select this project virtual environment in VS Code.
To do this, open the command palette (Ctrl+Shift+P) and search for "Python: Select Interpreter". Then, select the .venv folder in the project root directory.

### Install Packages into the Active Project Virtual Environment

When the project virtual environment is active,
install packages into the project virtual environment so they are available for use in the Python code.

NOTE:

- We **install** packages into the project virtual environment.
- We **import** packages into Python code (after they have been installed).

First, upgrade pip and wheel for good measure.
Then, install the project-specific required packages:

```shell
py -m pip install --upgrade pip wheel
py -m pip install --upgrade -r requirements.txt
```

## Run the App

With your project virtual environment activated in the terminal
 and the necessary packages installed, run the app with live reloading and
 automatically open it in the browser:

```shell  
shiny run --reload --launch-browser penguins/app.py
```

While the app is running, that terminal is fully occupied.
Open a new terminal to run other commands.

## Build the App to Docs Folder and Test Locally

With your project virtual environment activated in the terminal
 and the necessary packages installed, remove any existing assets and use
 shinylive export to build the app in the penguins folder to the docs folder:

```shell
shiny static-assets remove
shinylive export penguins docs
```

After the app is built, serve the app locally from the docs folder to test before publishing to GitHub Pages.
In the terminal, run the following command from the root of the project folder:

```shell
py -m http.server --directory docs --bind localhost 8008
```

Open a browser (tested with Chrome) and navigate to [http://localhost:8008](http://localhost:8008) to view the app running locally.

## Publish the App with GitHub Pages

After editing project files, use Git add/commit/push changes to the main branch:

```shell
git add .
git commit -m "Your commit message"
git push -u origin main
```

1. Go to the repository on GitHub and navigate to the **Settings** tab.
2. Scroll down and click the **Pages** section.
3. Select branch **main** as the source for the site.
4. Select the **docs** folder to publish from.
5. Click Save and wait for the site to build.
6. Edit the "About" section of the repository to include a link to the live app.

## Resources

Example csv data from [penguins.csv](https://github.com/mwaskom/seaborn-data/blob/master/penguins.csv).
Used for review only. In the app, we import the data from the palmerpenguins package.

Palmer Penguins published in:

 Horst AM, Hill AP, Gorman KB (2020). palmerpenguins: Palmer
Archipelago (Antarctica) penguin data. R package version 0.1.0.
 <https://allisonhorst.github.io/palmerpenguins/>. doi:
10.5281/zenodo.3960218.

Data originally published in:

Gorman KB, Williams TD, Fraser WR (2014). Ecological sexual dimorphism and environmental variability within a community of Antarctic penguins (genus Pygoscelis). PLoS ONE 9(3):e90081. <https://doi.org/10.1371/journal.pone.0090081>
