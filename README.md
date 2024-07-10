# Address Similarity Analysis

## Overview

This project focuses on detecting similar addresses that have different spellings using TF-IDF vectorization and cosine similarity. It demonstrates the application of natural language processing techniques in address matching, which is crucial for data cleaning and integration tasks.

## Project Structure

- `data/`: Contains raw and processed data.
- `notebooks/`: Jupyter notebook for similarity analysis.
- `scripts/`: Python script for creating a test set containing modified addresses.
- `requirements.txt`: List of dependencies.
- `environment.yml`: Conda environment configuration.

## Running on Google Colab

You can run this notebook in Google Colab by clicking the link below:

[![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/aleereza/address-similarity-analysis/blob/master/notebooks/address-similarity-analysis.ipynb)

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

Open and run the notebooks in the notebooks/ directory to perform data exploration and similarity analysis.

## Data Sources

The primary dataset used in this project is sourced from the Real, Random Address Data (RRAD) project:

[addresses-us-all.json](https://github.com/EthanRBrown/rrad/blob/master/addresses-us-all.json)

This dataset comprises real, random addresses from the [OpenAddresses](https://openaddresses.io/) project, and all the addresses are in the public domain.

## Methodology

This project uses TF-IDF vectorization and cosine similarity to identify and match similar addresses with variations in spelling. The steps include:

1. Vectorization: Applying TF-IDF to convert address text into numerical vectors.
2. Similarity Calculation: Using cosine similarity to measure the similarity between address vectors.
3. Evaluation: Assessing the performance of the similarity detection.

## License

This project is licensed under the MIT License.

## Contact

If you have any questions or feedback, please feel free to contact me at [alireza.barkhordari@gmail.com](mailto:alireza.barkhordari@gmail.com).
