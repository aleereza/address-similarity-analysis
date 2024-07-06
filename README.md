# Address Similarity Analysis

## Overview

This project focuses on detecting similar addresses that have different spellings using TF-IDF vectorization and cosine similarity.

## Project Structure

- `data/`: Contains raw and processed data.
- `notebooks/`: Jupyter notebooks for data exploration, cleaning, and similarity analysis.
- `scripts/`: Python scripts for data cleaning and similarity detection.
- `requirements.txt`: List of dependencies.
- `environment.yml`: Conda environment configuration.

## Running on Google Colab

colab link

## Getting Started

1. Clone the repository:

```bash
git clone https://github.com/your-username/address-similarity-analysis.git
cd address-similarity-analysis

```

2. Set up the environment:

Using Conda (recommended):

```bash
conda env create -f environment.yml
conda activate address-similarity
```

Using virtualenv:

```bash
python -m venv venv
source venv/bin/activate  # On Windows use `venv\Scripts\activate`
pip install -r requirements.txt
```

3. Run the notebooks:

Open and run the notebooks in the notebooks/ directory to perform data exploration, cleaning, and similarity analysis.

## Data Sources

addresses-us-all.json
https://github.com/EthanRBrown/rrad/blob/master/addresses-us-all.json

## Usage

Use the data_cleaning.py script to preprocess the address data.
Use the similarity_detection.py script to find similar addresses based on TF-IDF vectorization and cosine similarity.

## License

This project is licensed under the MIT License.

```

```
