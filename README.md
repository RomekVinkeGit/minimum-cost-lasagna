# Minimum cost lasagne

A machine learning project that analyzes and forecasts prices for ingredients necessary to make a vegetable lasagna in the Netherlands, with a specific focus on lasagna products from Albert Heijn.

## Project Overview

This project analyzes historical price data from Albert Heijn to:
- Track price changes of various lasagna products over time
- Forecast future price trends using multiple machine learning models
- Compare different forecasting methods to find the most accurate predictions
- Help consumers make informed purchasing decisions

## Features

### Price Forecasting Models
The project implements several forecasting models with a simplified, maintainable architecture:

- **Holt-Winters Model**: For time series with seasonal patterns
- **KNN Model**: For pattern-based predictions
- **Autoregressive Model**: For time-dependent forecasting
- **ARIMA Model**: For complex time series patterns
- **Random Forest Model**: For non-linear relationships

### Model Evaluation
- Automated model comparison
- RMSE and MAE metrics
- Visual performance analysis
- Best model selection

### Data Processing
- Historical price data cleaning
- Feature engineering
- Time series preprocessing
- Missing value handling

## Project Structure

```
supermarkt-prijzen/
├── data/                    # Data directory
│   ├── raw/                # Raw scraped data
│   └── processed/          # Cleaned and preprocessed data
├── src/                    # Source code
│   ├── models/            # Forecasting models
│   │   ├── base_model.py
│   │   ├── holt_winters_model.py
│   │   ├── knn_model.py
│   │   ├── ar_model.py
│   │   ├── arima_model.py
│   │   ├── random_forest_model.py
│   │   ├── model_factory.py
│   │   └── model_evaluator.py
│   └── evaluate_models.py  # Model evaluation script
├── results/               # Output directory
│   └── model_evaluation/  # Evaluation results and plots
└── requirements.txt       # Project dependencies
```

## Installation

1. Clone the repository:
```bash
git clone https://github.com/yourusername/supermarkt-prijzen.git
cd supermarkt-prijzen
```

2. Install dependencies:
```bash
pip install -r requirements.txt
```

## Usage

1. Prepare the data:
```bash
python src/preprocess_data.py
```

2. Run model evaluation:
```bash
python src/evaluate_models.py
```

The evaluation script will:
- Load the processed price data
- Train and evaluate all models
- Generate performance comparisons
- Save results and visualizations

## Data Format

The project uses a CSV file with the following structure:
```
date,product1,product2,...
2023-01-01,2.99,3.99,...
2023-01-08,2.89,4.09,...
```

Each row represents a date, and columns represent different lasagna products and their prices.

## Development Status

The project is currently in active development. Recent updates include:
- Simplified model implementations for better maintainability
- Streamlined evaluation pipeline
- Focus on key lasagna products with complete price histories

## Contributing

1. Fork the repository
2. Create a feature branch
3. Make your changes
4. Submit a pull request

## License

This project is licensed under the MIT License.

## Acknowledgments

- Data source: Albert Heijn
- Built with Python, scikit-learn, statsmodels, and pandas 
