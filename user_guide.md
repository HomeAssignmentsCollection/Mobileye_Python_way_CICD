# User Guide

## Overview

This guide provides instructions on how to run the Product Delivery Pipeline via the command line. The pipeline is designed to build, deploy, and notify about your product releases in an automated manner.

## Prerequisites

Before running the pipeline, ensure that the following conditions are met:

- **Pipeline Code Location:**  
  The pipeline code is located on your host machine.

- **Python:**  
  Python is installed on the host.

- **Docker:**  
  Docker is installed on the host.

- **Docker Image:**  
  A Docker image (e.g., `python:3.9` or your custom image) has been created and is available.

- **Security & Access:**  
  Environment variables for accessing repositories (e.g., `ARTIFACTORY_USER`, `NEXUS_USER`, etc.) are set and available within the Docker container.

- **Dependency Management:**  
  All dependencies and libraries are managed at the Docker image level, ensuring a consistent environment for the pipeline.

## Running the Pipeline

To run the pipeline from the command line, use the following command:

```bash
python product_pipeline.py --repo_name <ProductName> [--target_branch <branch_name>]

```