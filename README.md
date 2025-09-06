# COVID Data

## Description
This project is a COVID-19 data visualization dashboard for Brazil, which retrieves real-time information from the official website of the Ministry of Health. It includes scripts for automatic data collection and an API for retrieving the obtained data.

## Prerequisites
- Python 3.11
- Python libraries (installed via pip install -r requirements.txt)
- Docker installed
- Google Chrome installed
- ChromeWebDriver installed

## Installation

1. **Clone this repository:**

   ```bash
   git clone https://github.com/guibedan/covid-data.git
   cd covid-data
   ```
2. **Install the dependencies:**

   ```bash
   pip install -r requirements.txt
   ```

## Execution

1. **Run the docker compose:**

   ```bash
   docker-compose up
   ```
2. **Run the main script:**

   ```bash
   python main.py
   ```

## Endpoints da API
- **/v1/world:** Obtains data from all countrys in world.
- **/v2/regions:** Obtains data from all regions of Brazil.
- **/v2/states:** Obtains data from all states in Brazil.
- **/v2/cities/{page}:** Obtains data from all cities in Brazil formatted in pages.
- **/v2/cities/all:** Obtains data from all cities in Brazil formatted in list.
- **/v2/cities/top:** Obtains data from the top 10 cities with the most cases
