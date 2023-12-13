# COVID Data Dashboard

## Description
This project is a COVID-19 data visualization dashboard for Brazil, which retrieves real-time information from the official website of the Ministry of Health. It includes scripts for automatic data collection and an API for retrieving the obtained data.

## Prerequisites
- Python 3.11
- Python libraries (installed via pip install -r requirements.txt)
- Google Chrome installed
- ChromeWebDriver installed

## Installation

1. **Clone this repository:**

   ```bash
   git clone https://github.com/seu-usuario/covid-data-dashboard.git
   cd covid-data-dashboard
   ```
2. **Install the dependencies:**

   ```bash
   pip install -r requirements.txt
   ```

## Execution

1. **Run the main script:**

   ```bash
   python main.py
   ```

## Endpoints da API
- **/v1/regions:** Obtains data from all regions of Brazil.
- **/v1/states:** Obtains data from all states in Brazil.
