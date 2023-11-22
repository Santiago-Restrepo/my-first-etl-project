# My First ETL Project

This is my first ETL (Extract, Transform, Load) project, where I am building a data pipeline to extract data from Trip Advisor reviews and offerings using [this Kaggle dataset in CSV format](https://www.kaggle.com/datasets/joebeachcapital/hotel-reviews?select=reviews.csv). The project processes and transforms data using Pandas and brings data into a PostgreSQL database using SqlAlchemy.

## Table of Contents

- [Installation](#installation)
- [Database Setup](#database-setup)
- [Running the Project](#running-the-project)

## Installation

To get started with the project, follow these steps:

1. Clone the repository to your local machine:

    ```bash
    git clone https://github.com/Santiago-Restrepo/my-first-etl-project.git
    ```

2. Navigate to the project directory:

    ```bash
    cd my-first-etl-project
    ```

3. Create a virtual environment using `venv`:

    ```bash
    python3 -m venv venv
    ```

4. Activate the virtual environment:

    On Windows:
    ```bash
    .\venv\Scripts\activate
    ```

    On macOS/Linux:
    ```bash
    source venv/bin/activate
    ```

5. Install project dependencies:

    ```bash
    pip install -r requirements.txt
    ```

## Database Setup

For the project, I use Docker and Docker Compose to set up the PostgreSQL database. Follow these steps to run the database:

1. Install Docker and Docker Compose if you haven't already. You can download them from [Docker's official website](https://www.docker.com/get-started).

2. In the project directory, create a `.env` file with the following database configuration:

    ```env
    POSTGRES_USER=postgres
    POSTGRES_PASSWORD=postgres123
    POSTGRES_DB=mydatabase
    POSTGRES_PORT=5434
    ```

3. Run the PostgreSQL database using Docker Compose:

    ```bash
    docker-compose up -d
    ```

## Running the Project

Now that the database is set up, you can run the ETL project:

1. Ensure the virtual environment is activated (see [Installation](#installation)).

2. Execute the main script:

    ```bash
    python main.py
    ```

This will start the ETL process and populate the PostgreSQL database with the extracted and transformed data.

Feel free to explore the code in the `main.py` and other relevant files for more details on the ETL process.

Happy ninja coding!
