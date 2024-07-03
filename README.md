
# Numbeo City Cost of Living Data Fetcher

This Python script retrieves cost of living data for cities using the Numbeo API. It allows users to fetch rent data for apartments, count cities by state in the US, and count cities by country. The results can be output to a CSV file.

## Features

- Retrieve cost of living data for US cities or all cities.
- Perform a dry run with a limited number of cities.
- Count cities by state in the US.
- Count cities by country.
- Output results to a CSV file.

## Prerequisites

- Python 3.x
- Numbeo API key
- Required Python packages:
  - `requests`
  - `python-dotenv`
  - `csv`

## Installation

1. Clone the repository:

   ```bash
   git clone https://github.com/yourusername/your-repo-name.git
   cd your-repo-name
   ```

2. Create and activate a virtual environment (optional but recommended):

   ```bash
   python -m venv env
   source env/bin/activate  # On Windows use `env\Scriptsctivate`
   ```

3. Install the required packages:

   ```bash
   pip install -r requirements.txt
   ```

4. Create a `.env` file in the project directory and add your Numbeo API key:

   ```env
   NUMBEO_API_KEY=your_numbeo_api_key_here
   ```

