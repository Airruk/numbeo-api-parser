
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

## Usage

Run the script with the desired arguments:

### Arguments

- `--us-cities`: Retrieve data for US cities only.
- `--all-cities`: Retrieve data for all cities.
- `--dry-run`: Perform a dry run with a limited number of cities.
- `--count-by-state`: Count cities by state in the US.
- `--count-by-country`: Count cities by country for all countries.
- `-o`, `--output`: Output the results to a CSV file with the specified filename.

### Examples

1. **Count cities by state in the US and output to a CSV:**

   ```bash
   python script.py --count-by-state -o state_counts.csv
   ```

2. **Count cities by country and output to a CSV:**

   ```bash
   python script.py --count-by-country -o country_counts.csv
   ```

3. **Perform a dry run (default or explicitly):**

   ```bash
   python script.py --dry-run
   ```

4. **Retrieve data for US cities:**

   ```bash
   python script.py --us-cities
   ```

5. **Retrieve data for all cities:**

   ```bash
   python script.py --all-cities
   ```

6. **Retrieve data and output to a CSV:**

   - For US cities:

     ```bash
     python script.py --us-cities -o rent_data.csv
     ```

   - For all cities:

     ```bash
     python script.py --all-cities -o rent_data.csv
     ```

## Contributing

Contributions are welcome! Please open an issue or submit a pull request for any improvements or bug fixes.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

## Acknowledgments

- [Numbeo API](https://www.numbeo.com/api/) for providing the cost of living data.
- [python-dotenv](https://pypi.org/project/python-dotenv/) for managing environment variables.
