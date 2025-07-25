#!/usr/bin/env python
"""
This module implements the product delivery pipeline.
It includes classes and functions to manage build, deploy, and notify steps,
as well as helper functions to create deployment targets and notification channels.
"""
import os
import sys
import argparse
import datetime
from product_pipeline.utils.logging import get_logger
from product_pipeline.core.pipeline import Product, Pipeline

# Import configuration loader from utils_py directory
from product_pipeline.utils.config import load_configuration

# Import helper functions from helpers
from product_pipeline.utils.helpers import (
    find_product_config,
    init_deployment_targets,
    init_notification_channels,
)

logger = get_logger("ProductPipeline")


def run_in_container():
    if os.environ.get("INSIDE_DOCKER") is None:
        docker_command = [
            "docker",
            "run",
            "--rm",
            "-v",
            f"{os.getcwd()}:/app",
            "-w",
            "/app",
            "-e",
            "INSIDE_DOCKER=1",
            "python:3.9",
            "python",
            sys.argv[0],
        ]
        print("Emulating Docker container launch:")
        print(" ".join(docker_command))
        # Uncomment the next line to run only inside a container
        # sys.exit(0)
    else:
        print("Running inside Docker container.")


def main():
    run_in_container()

    config = load_configuration()

    parser = argparse.ArgumentParser(description="Run Product Delivery Pipeline")
    parser.add_argument(
        "--repo_name", required=True, help="Product name as specified in config.yaml"
    )
    parser.add_argument(
        "--target_branch", help="Target branch for deployment (overrides config)"
    )
    parser.add_argument(
        "--stages",
        help="Comma-separated list of pipeline stages (e.g. build,deploy,notify)",
    )
    args = parser.parse_args()

    # Find product configuration by name using helper function
    product_config = find_product_config(config, args.repo_name)

    repo_name = product_config.get("product_name")
    git_repository = product_config.get("git_repository")
    default_target_branch = product_config.get("default_target_branch")
    target_branch = args.target_branch if args.target_branch else default_target_branch

    # Initialize deployment targets and notification channels using helper functions
    deploy_targets = init_deployment_targets(product_config)
    notification_channels = init_notification_channels(product_config)

    scheduled_time = datetime.datetime.now()
    valid_stages = ["build", "deploy", "notify"]
    product = Product(
        name=repo_name,
        git_repository=git_repository,
        scheduled_time=scheduled_time,
        target_branch=target_branch,
        deploy_targets=deploy_targets,
        notification_channels=notification_channels,
        valid_stages=valid_stages,
    )

    print(f"[DEBUG] {product.__dict__}")

    # If the --stages argument is provided, parse it into a list of stages and validate them
    stages = None
    if args.stages:
        stages = [s.strip() for s in args.stages.split(",") if s.strip()]
        for stage in stages:
            if stage not in valid_stages:
                print(
                    f"Error: Stage '{stage}' is not valid. Valid stages are: {valid_stages}"
                )
                sys.exit(1)

    # Run the main pipeline (build, deploy, notify)
    pipeline = Pipeline(product, stages)
    pipeline.run()


if __name__ == "__main__":
    main()
