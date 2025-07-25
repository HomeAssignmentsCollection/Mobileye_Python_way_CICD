# Product Delivery Pipeline

## Overview

The Product Delivery Pipeline is an object-oriented Python solution designed to manage the build, deployment, and notification processes for multiple products. Each product is treated as a standalone package that can be built, deployed, and versioned independently. The pipeline is executed within a Docker container to ensure portability, scalability, and isolation.

## Design the Solution

1. **Standalone Products:**  
   Each loaded product is a standalone package that can be built and deployed independently from other products.

2. **Parallel Execution:**  
   The infrastructure has sufficient resources to build and deploy products in parallel when needed. The order in which products finish uploading is not critical—failure of one product's pipeline does not affect the pipelines for other products.

3. **External Scheduling:**  
   The start time for the pipeline is managed by an external system (e.g., cronjob).

4. **Upload Target:**  
   Each product is stored in its own storage repository under a structure such as:  
   `<product_name>/<version>/<date-time>`

5. **Version History:**  
   Every product maintains its own version history.

6. **Build Manifest:**  
   As part of the build pipeline, a universal build identifier and a manifest are created. This manifest stores metadata such as dependencies, the Git commit hash of the product, and the build tools used to generate the deployable artifact.

7. **Execution Environment:**  
   To ensure portability, scalability, and isolation, the pipeline runs within a container.

8. **Security:**  
   Secret management is handled through various methods, such as:  
   - Using third-party tools (like Vault or Secrets Manager)  
   - Storing environment variables in the Docker image  
   - Mounting a credentials folder into the Docker container  
   - Utilizing CI/CD tool Secrets Managers

9. **Pipeline Logic:**  
   The pipeline’s behavior is defined by a configuration file and determined by the product (repository) name and the target branch. Depending on the number of products, the configuration file can be:
   - A universal file (with data parsed by product name)
   - Stored in the product’s repository
   - Kept in a separate repository for build manifests
   - Included as part of the pipeline repository itself

10. **Dependency Pipelines:**  
    In cases where a new or final product depends on several existing products, its build, testing, and release processes will be automated within a separate pipeline. Such dependency handling is outside the scope of the current task.

11. **Stage Functions:**  
    Functions for individual stages (e.g., clone, build, testing, security check, static code analysis, reporting, packaging, versioning, etc.) are currently out of scope and will be implemented in future iterations.


## Prerequisites

Before running the pipeline, ensure that:

- The pipeline code is located on the host machine.
- Python is installed on the host.
- Docker is installed on the host.
- A Docker image (e.g., `python:3.9` or a custom image) has been created and is available.
- Environment variables for repository access (e.g., `ARTIFACTORY_USER`, `NEXUS_USER`, `S3_ACCESS_KEY`, etc.) are set and available inside the Docker container.
- Dependencies and libraries are managed at the Docker image level.


## Workflow

### 1. Script Launch

- The pipeline script is scheduled to run periodically using an external scheduler such as **cron**.
- Example cron entry:
``` bash
0 1 * * * /usr/bin/python /path/to/product_pipeline.py --repo_name ProductA --target_branch main
```
- **Parameters:**
- **Mandatory:** `--repo_name` (the product name as specified in the configuration file)
- **Optional:** `--target_branch` (the target branch to deploy, which overrides the default from the config)

### 2. Pipeline Configuration File

- The pipeline uses a universal configuration file (`config.yaml`) that applies to all products.
- This configuration file is located in the root directory of the pipeline project.
- The configuration includes details such as:
- - Product names and corresponding Git repositories
- - Default target branches
- - Deployment target settings (e.g., Artifactory, Nexus, S3)
- - Notification channel settings (e.g., Email, Slack)

### 3. Pipeline Flow

The pipeline flow is as follows:

#### 3.1. Docker Container Execution

- When the script starts, it checks whether it is running inside a Docker container.
- **If not inside a container:**
- The script will emulate a Docker container launch with the required parameters.
- This ensures that the pipeline runs in a controlled, isolated environment.
- The main execution (`main()`) occurs inside the Docker container rather than on the host OS.

#### 3.2. Pipeline Steps

- **Get Pipeline Configuration:**  
The pipeline loads the configuration and parses it based on the product name provided via `--repo_name`.

- **Build Stage:**  
- The build stage includes operations such as cloning the repository, checking out the appropriate branch, building the product, and performing versioning.
- In the current implementation, these steps are simulated by printing messages to the console.

- **Upload Stage:**  
- The deploy stage handles uploading the build artifact to one or more target repositories (e.g., Artifactory, Nexus, S3).
- The target(s) and credentials are retrieved from the configuration file.

- **Notify Stage:**  
- The notification stage sends notifications to one or more channels (e.g., Email, Slack) as defined in the configuration.

*Note:* Detailed implementations for stages like cloning, testing, security checks, and packaging are out of scope for the current iteration and will be implemented in future versions.