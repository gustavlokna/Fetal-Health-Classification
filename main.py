import argparse
from typing import Any
from utils.config import read_config
from Visualization.visualize import correlation_matrix_make_png
from Preprocessor.preprocessor import data_preprocessing
from model.linearRegression import train_model, predict_model, eval_plot

def main(args: argparse.Namespace) -> None:
    """
    Main function for the fetal health classification pipeline.

    This function coordinates the execution of various stages in the classification
    pipeline, including data preprocessing, feature enhancement, model training, prediction,
    and evaluation. Each step is activated based on the provided command line arguments.

    Parameters
    ----------
    args : argparse.Namespace
        Command line arguments parsed by argparse that determine which parts of the pipeline
        are activated (preprocessing, adding features, training, predicting, evaluating).

    Returns
    -------
    None

    Notes
    -----
    The function begins by reading the configuration settings. Based on the command line
    arguments, it executes one or more of the following steps:
    - Data preprocessing to prepare data for feature building or model training.
    - Feature building to enhance the model's input data.
    - Training the model on preprocessed and feature-enhanced data.
    - Making predictions using the trained model.
    - Evaluating the model's performance and generating visualizations such as correlation matrices.
    If no valid command line arguments are provided, the function will exit with a guidance message.
    """
    config: dict[str, Any] = read_config()
    if args.preprocess:
        #_run_preprocessing(args.building, config["data"], args.include_elhub)
        data_preprocessing(config)
        print("hei")
    elif args.add_features:
        #_run_feature_building(args.building, config["data"])
        
        print("hallo")
    elif args.train:
        print("hei")
        train_model(config)

    elif args.predict:
        print("predict")
        predict_model(config)

    elif args.eval:
        print("corr")
        fileName = "correlationMatrix"
        correlation_matrix_make_png(fileName, config)
        eval_plot(config)
        #eval_model(eval_run_args)
    else:
        print("No valid arguments provided. Use --help for usage information.")

def parse_arguments() -> argparse.Namespace:
    """
    Parse command line arguments.

    Returns
    -------
    argparse.Namespace
        Parsed command line arguments.

    Notes
    -----
    This function sets up the argument parser with the following options:
    --preprocess : Flag to enable preprocessing of sensor and HVAC data.
    --building : String specifying the building to run the pipeline on.
    --include_elhub : Flag to include Elhub data in the feature building step.
    --build_features : Flag to enable the feature building step.
    --train : Flag to enable the training step (not implemented yet).
    """
    parser = argparse.ArgumentParser(description="Sensor anomaly detection pipeline")
    parser.add_argument(
        "--preprocess",
        action="store_true",
        help="Enable preprocessing of sensor and HVAC data",
    )
    parser.add_argument(
        "--add_features",
        action="store_true",
        help="Enable the feature building step",
    )
    parser.add_argument(
        "--train",
        action="store_true",
        help="Enable the training step (not implemented yet)",
    )
    parser.add_argument(
        "--predict",
        action="store_true",
        help="Enable the training step (not implemented yet)",
    )

    parser.add_argument(
        "--eval",
        action="store_true",
        help="Enable the evaluation step (not implemented yet)",
    )
    return parser.parse_args()


if __name__ == "__main__":
    args = parse_arguments()
    main(args)
