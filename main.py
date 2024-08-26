import argparse
from typing import Any
from utils.config import read_config
from Visualization.visualize import correlation_matrix_make_png
from Preprocessor.preprocessor import data_preprocessing
from model.linearRegression import train_model

def main(args: argparse.Namespace) -> None:
    """
    Main function for the sensor anomaly detection pipeline.

    This function orchestrates the preprocessing, feature building, and training
    steps of the sensor anomaly detection pipeline based on the provided command
    line arguments.

    Parameters
    ----------
    args : argparse.Namespace
        Command line arguments parsed by argparse.

    Returns
    -------
    None

    Notes
    -----
    The function reads the configuration, validates the building name,
    and executes the appropriate pipeline step based on the provided arguments.
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
    elif args.eval:
        print("corr")
        fileName = "correlationMatrix"
        correlation_matrix_make_png(fileName, config)
        #eval_model(eval_run_args)
    else:
        print("No valid arguments provided. Use --help for usage information.")



def _run_preprocessing(
    building: str, data_config: dict[str, Any], include_elhub: bool
) -> None:
    """
    Run the preprocessing step of the pipeline.

    Parameters
    ----------
    building : str
        The name of the building to preprocess data for.
    data_config : dict
        Configuration dictionary for data processing.
    include_elhub : bool
        Flag to include Elhub data in preprocessing.

    Returns
    -------
    None
    """
    print(f"Preprocessing data for building: {building}")
    preprocess_sensor_hvac_and_elhub_data(building, data_config, include_elhub)



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
        "--eval",
        action="store_true",
        help="Enable the evaluation step (not implemented yet)",
    )
    return parser.parse_args()


if __name__ == "__main__":
    args = parse_arguments()
    main(args)
