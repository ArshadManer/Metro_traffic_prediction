# Metro Traffic Monitoring

## Introduction

The goal of this project is to build a prediction model using multiple machine learning
techniques and to use a template to document the end-to-end stages. We're trying to
forecast the value of a continuous variable with the Metro Interstate Traffic Volume
dataset, which is a regression issue.

## Dataset
Hourly traffic volume on Interstate 94 westbound for MN DoT ATR station 301, located
around halfway between Minneapolis and St Paul, MN. For the impact on traffic volume,
hourly weather features and holidays are incorporated.
## Requirements

The following packages are required to run the code:

- NumPy
- Pandas
- Scikit-learn
- Seaborn
- Matplotlib (optional, for visualizing results)
- Pickle

## Setup

To set up the environment, you need to install the required packages. You can use the following command to install them using `pip`: pip install numpy pandas scikit-learn matplotlib pickle


## Usage

The code is written in Python and can be executed using a terminal, Jupyter Notebook or any other Python environment.
The dataset used for training and testing the model is included in the `data` folder. To train the model, simply execute the script `main.py`.or run the cells in the model_traning.ipynb Notebook.

## File Directory

- `main.py`: The main script that tra predicts traffic volume.
- `notebook`: EDA, data preprocessing and model traning. 
- `saved_models`: The folder to save the trained model.

## Model
The model used in this project is a RandomForestRegressor model. However, you can experiment with other regression algorithms or try to improve the performance of the model by fine-tuning the hyperparameters or using a more complex model.

## Results
The performance of the model is evaluated using mean squared error (MSE) and R-squared (R^2) metrics. The results show that the model is able to make accurate predictions with a low MSE and a high R^2 value.

## Conclusion

This project provides a implementation of regressiong algorithms for an traffic volume prediction. The code and methodology can be used as a starting point for building more advanced models or for exploring different regression algorithms.

