# COVID-19 Data Analysis Project

## 1. Project Description
This project analyzes global COVID-19 trends, including cases, deaths, and vaccinations, across different countries and time.

## 2. Data Source
* Our World in Data COVID-19 Dataset: [https://github.com/owid/covid-19-data/blob/master/public/data/owid-covid-data.csv](https://github.com/owid/covid-19-data/blob/master/public/data/owid-covid-data.csv)

## 3. Setup Instructions

### 3.1. Download the Data
* **Download the Dataset:**
    * Go to the Our World in Data COVID-19 dataset: [https://github.com/owid/covid-19-data/blob/master/public/data/owid-covid-data.csv](https://github.com/owid/covid-19-data/blob/master/public/data/owid-covid-data.csv)
    * Click on the "Download raw" button to download the CSV file.
    * Save the file as `owid-covid-data.csv` in the `data/` folder.

### 3.2. Create a Virtual Environment (Recommended)
* Open your terminal or command prompt.
* Navigate to the project directory: `cd covid19_project`
* Create a virtual environment:
    * macOS/Linux: `python3 -m venv venv`
    * Windows: `python -m venv venv`
* Activate the virtual environment:
    * macOS/Linux: `source venv/bin/activate`
    * Windows: `venv\Scripts\activate`

### 3.3. Install Dependencies
* Make sure your virtual environment is activated.
* Install the required Python libraries:
    ```bash
    pip install pandas matplotlib seaborn plotly
    ```

## 4. Project Structure


covid19_project/
│
├── data/
│   └── owid-covid-data.csv
│
├── notebooks/
│   └── covid19_analysis.ipynb
│
├── scripts/
│   └── data_processing.py
│
├── reports/
│   └── covid19_report.pdf
│
├── venv/
│   ├── ... (virtual environment files)
│
└── README.md


## 5. Running the Analysis
* Open the Jupyter Notebook:
    ```bash
    jupyter notebook
    ```
* Navigate to `notebooks/` and open `covid19_analysis.ipynb`.
* Run the cells in the notebook to perform the analysis and generate visualizations.

## 6. (Optional) Running the data processing script
* To run the data processing script
    ```bash
    python scripts/data_processing.py
    ```

## 7. (Optional) Exporting the report
* The notebook can be exported as a PDF.
