# Supermarkt Prijzen Analysis

This project analyzes price data from Dutch supermarkets, with a focus on Albert Heijn (AH) products. The project tracks price changes over time and can be used for price analysis and prediction.

## Project Structure

```
supermarkt-prijzen/
├── data/
│   ├── raw/              # Original JSON files with supermarket data
│   └── processed/        # Processed CSV files
├── src/
│   ├── data/            # Data processing scripts
│   └── models/          # Machine learning model code
├── notebooks/           # Jupyter notebooks for analysis
├── README.md           # Project documentation
└── requirements.txt    # Project dependencies
```

## Setup

1. Install dependencies:
```bash
pip install -r requirements.txt
```

2. Place raw JSON files in `data/raw/` directory

3. Run data processing:
```bash
python src/data/process_data.py
```

## Data Processing

The project includes scripts to:
- Process raw JSON files from multiple supermarkets
- Extract Albert Heijn product data
- Track price changes over time
- Generate historical price datasets

## Future Development

- Price prediction models
- Price trend analysis
- Product category analysis
- Price comparison across supermarkets 