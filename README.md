# 🇪🇺 Renewable Energy Transition in Europe

An interactive data visualization dashboard exploring the **renewable energy transition across European countries** using renewable energy share data from **Eurostat**.

The project provides an interactive way to compare countries, analyze historical trends, identify leading countries, and visualize the geographical distribution of renewable energy adoption across Europe.

## 📊 Project Overview

The **Renewable Energy Transition in Europe** project analyzes how the share of renewable energy has evolved across European countries over time.

The project includes:

* 📈 Historical renewable energy trend analysis
* 🌍 Country-level comparisons
* 🏆 Top renewable-energy-performing countries
* 🗺️ Interactive geographical visualization
* 🎛️ Interactive country and year filters
* 📌 Key performance indicators
* 📊 Interactive Plotly visualizations

The dashboard is built with **Streamlit**, while **Pandas** is used for data processing and **Plotly** for interactive visualizations.

## 🚀 Live Dashboard

Run the application locally using Streamlit:

```bash
streamlit run app.py
```

After starting the application, Streamlit will provide a local URL, typically:

```text
http://localhost:8501
```

## 🖼️ Dashboard Features

### 1. Country Selection

Users can select multiple European countries from the sidebar to compare their renewable energy shares over time.

The dashboard provides default comparisons for:

* Germany
* France
* Sweden

### 2. Year Range Filter

An interactive year-range slider allows users to restrict the analysis to a specific period.

### 3. KPI Cards

The dashboard displays three key metrics:

* **EU Average (Latest)** – Renewable energy share for the European Union in the latest available year.
* **Top Performer** – Country with the highest renewable energy share in the latest selected year.
* **Reporting Countries** – Number of countries represented in the dataset.

### 4. Historical Growth Comparison

An interactive line chart shows renewable energy shares over time for the selected countries.

This makes it possible to compare the development of renewable energy adoption across countries.

### 5. Top 10 Renewable Energy Leaders

A horizontal bar chart displays the ten countries with the highest renewable energy share in the selected end year.

### 6. Geographical Distribution

An interactive choropleth map shows renewable energy shares across Europe.

Countries are colored according to their renewable energy share, allowing geographical patterns to be explored quickly.

## 🗂️ Project Structure

```text
Renewable-Energy-Transition-in-Europe/
│
├── Renewable Energy Transition in Europe.ipynb
├── app.py
├── cleaned_renewable_data.csv
├── requirements.txt
└── README.md
```

### File Description

| File                                          | Description                                                |
| --------------------------------------------- | ---------------------------------------------------------- |
| `app.py`                                      | Streamlit application containing the interactive dashboard |
| `Renewable Energy Transition in Europe.ipynb` | Jupyter Notebook containing the project analysis           |
| `cleaned_renewable_data.csv`                  | Cleaned renewable energy dataset                           |
| `requirements.txt`                            | Python dependencies required to run the project            |
| `README.md`                                   | Project documentation                                      |

## 🛠️ Technologies Used

* **Python**
* **Streamlit** – Interactive dashboard development
* **Pandas** – Data loading and manipulation
* **Plotly Express** – Interactive charts and geographical visualization
* **Jupyter Notebook** – Exploratory data analysis
* **CSV** – Data storage

## 📦 Installation

### 1. Clone the Repository

```bash
git clone https://github.com/rautbishow4/Renewable-Energy-Transition-in-Europe.git
```

### 2. Navigate to the Project Directory

```bash
cd Renewable-Energy-Transition-in-Europe
```

### 3. Create a Virtual Environment

#### Windows

```bash
python -m venv venv
venv\Scripts\activate
```

#### macOS / Linux

```bash
python3 -m venv venv
source venv/bin/activate
```

### 4. Install Dependencies

```bash
pip install -r requirements.txt
```

### 5. Run the Dashboard

```bash
streamlit run app.py
```

## 📚 Data Source

The dashboard uses **Eurostat** renewable energy data, specifically the indicator:

**SDG 07_40 – Share of renewable energy in gross final energy consumption**

The cleaned dataset included in this repository contains the following primary fields:

```text
Year
Country
Renewable_Share
```

The dashboard also distinguishes between individual countries and aggregate entries such as:

* European Union – 27 countries
* Euro area – 20 countries

The aggregate entries are excluded from country-level comparisons.

For more information about renewable energy targets and EU renewable-energy statistics, see the European Commission's Renewable Energy Directive resources.

## 🔄 Data Processing Workflow

The project follows a simple data-analysis workflow:

```text
Raw / Source Data
       │
       ▼
Data Cleaning
       │
       ▼
cleaned_renewable_data.csv
       │
       ▼
Pandas DataFrame
       │
       ▼
Streamlit Dashboard
       │
       ├── KPI Metrics
       ├── Line Chart
       ├── Top 10 Bar Chart
       └── Europe Map
```

## 📈 Example Analysis Questions

The dashboard can be used to explore questions such as:

* How has renewable energy adoption changed over time?
* How do different European countries compare?
* Which countries have the highest renewable energy shares?
* How has a country's renewable energy share changed over a selected period?
* What geographical patterns can be observed across Europe?
* How does the renewable energy transition differ between countries?

## 💡 Key Insights

The project is designed to make differences in renewable energy adoption across Europe easier to explore through interactive visualizations.

Rather than relying only on an EU-wide average, the dashboard allows users to investigate individual countries and compare their historical trajectories.

The European Union has continued to increase renewable energy deployment, with the EU's revised Renewable Energy Directive setting a binding target of at least **42.5% renewable energy in gross final energy consumption by 2030**, while aiming for 45%.

## 🔍 Notebook

The repository also contains a Jupyter Notebook:

```text
Renewable Energy Transition in Europe.ipynb
```

The notebook can be opened using Jupyter Notebook or JupyterLab:

```bash
jupyter notebook
```

or:

```bash
jupyter lab
```

## ⚠️ Limitations

* The dashboard depends on the available data in the included CSV file.
* Results are limited to the countries and years represented in the dataset.
* Renewable energy share is an indicator of the proportion of energy consumption supplied by renewable sources; it does not by itself describe total renewable energy production.
* The dashboard is intended primarily for exploratory analysis and visualization.

## 🔮 Future Improvements

Potential improvements include:

* [ ] Add more renewable energy indicators
* [ ] Add solar, wind, hydro, and biomass breakdowns
* [ ] Add country ranking over multiple years
* [ ] Add downloadable filtered datasets
* [ ] Add additional interactive charts
* [ ] Add renewable energy targets and progress indicators
* [ ] Deploy the Streamlit application publicly
* [ ] Add automated data updates from Eurostat
* [ ] Add more detailed documentation of the data-cleaning process

## 🤝 Contributing

Contributions are welcome.

1. Fork the repository
2. Create a new branch

```bash
git checkout -b feature/your-feature
```

3. Make your changes
4. Commit your changes

```bash
git commit -m "Add your feature"
```

5. Push the branch

```bash
git push origin feature/your-feature
```

6. Open a Pull Request

## 📄 License

No license is currently specified in the repository. If you intend to distribute or reuse this project, consider adding an appropriate open-source license such as MIT.

## 👤 Author

**rautbishow4**

GitHub Repository:

https://github.com/rautbishow4/Renewable-Energy-Transition-in-Europe

---

⭐ If you find this project useful, consider starring the repository!
