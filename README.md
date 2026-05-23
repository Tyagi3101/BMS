# Bakery Management System (BMS)

A Streamlit-based dashboard for bakery sales analytics and visualization.

## Overview

BMS is a data-driven dashboard application that provides real-time insights into bakery operations, including sales trends, revenue analysis, and product performance metrics.

## Features

- **KPI Dashboard**: Display key metrics including total revenue, order count, and top-selling items
- **Sales Analysis**: Visualize top-selling products with bar charts
- **Trend Analysis**: Track daily sales trends over time
- **Revenue Distribution**: Pie chart showing revenue breakdown by item

## Project Structure

```
BMS/
├── app.py                          # Main Streamlit application
├── datageneration.py               # Data generation script for testing
├── requirements.txt                # Python dependencies
├── data/
│   └── bakery_sales_2000.csv      # Sample sales data
└── README.md                       # This file
```

## Requirements

- Python 3.7+
- pandas
- streamlit
- matplotlib
- seaborn

## Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/Tyagi3101/BMS.git
   cd BMS
   ```

2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

## Usage

### Generate Sample Data

```bash
python datageneration.py
```

This creates `data/bakery_sales_2000.csv` with sample bakery sales records.

### Run the Dashboard

```bash
streamlit run app.py
```

The application will open in your browser at `http://localhost:8501`

## Data Format

The CSV file should contain the following columns:

| Column | Type | Description |
|--------|------|-------------|
| sale_date | datetime | Date and time of the sale |
| item_name | string | Name of the bakery item sold |
| item_price | float | Price of the item sold |

## Dashboard Components

### KPI Cards
- **Total Revenue**: Sum of all item prices
- **Total Orders**: Total number of sales transactions
- **Top Item**: Most frequently sold item

### Charts

1. **Top Selling Items**: Bar chart showing sales frequency by item
2. **Daily Sales Trend**: Line chart showing revenue trends over time
3. **Revenue by Item**: Pie chart showing revenue distribution across products

## Development

To customize the dashboard:

1. Edit `app.py` to modify visualizations or add new metrics
2. Update `datageneration.py` to change sample data generation logic
3. Modify `requirements.txt` if adding new dependencies

## Troubleshooting

### Issue: "EmptyDataError: No columns to parse from file"
**Solution**: Run `python datageneration.py` to generate sample data

### Issue: ModuleNotFoundError
**Solution**: Ensure all dependencies are installed: `pip install -r requirements.txt`

### Issue: File not found error
**Solution**: Run the application from the project root directory: `streamlit run app.py`

## License

MIT License

## Author

Tyagi3101
