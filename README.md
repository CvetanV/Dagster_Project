# Dagster_Project
This repository contains the steps for setting up Dagster and the files regarding building an ETL process on Dagster.


# Dagster setup on local machine
1. Install virtualenv package: pip install virtualenv
2. Create a virtual environment: python -m venv env
3. Activate virtual environment: env\Scripts\activate
4. Install the Dagster packages: pip install dagster dagit
5. Create new project: dagster project scaffold --name etl (etl is a project name you can put anything there)
6. Navigate to the etl folder
7. Install project dependencies: pip install -e ".[dev]"
8. To run the dagster UI: dagster dev
9. Once you see wellcome to dagster in the black window, open a browser and navigate to localhost:3000 and you will have the dagster UI.

# Developing on Dagster
1. Follow the official tutorial on this link: https://docs.dagster.io/tutorial/introduction
