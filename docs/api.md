# API Documentation

## Core Classes

### Product Class

```python
class Product:
    def __init__(self, name, git_repository, scheduled_time, target_branch, 
                 deploy_targets, notification_channels, valid_stages=None):
        """
        Initialize a Product instance.
        
        Args:
            name (str): Product name
            git_repository (str): Git repository URL
            scheduled_time (datetime): Pipeline execution time
            target_branch (str): Target branch for deployment
            deploy_targets (list): List of deployment target objects
            notification_channels (list): List of notification channel objects
            valid_stages (list, optional): List of valid pipeline stages
        """
```

**Methods:**
- `build()`: Execute build stage
- `deploy()`: Execute deploy stage
- `notify()`: Execute notification stage

### Pipeline Class

```python
class Pipeline:
    def __init__(self, product: Product, stages=None):
        """
        Initialize a Pipeline instance.
        
        Args:
            product (Product): Product instance to process
            stages (list, optional): List of stages to execute
        """
```

**Methods:**
- `run()`: Execute all pipeline stages

### DeploymentTarget (Abstract Base)

```python
class DeploymentTarget(ABC):
    @abstractmethod
    def deploy(self, product):
        """
        Deploy the product to the target repository.
        
        Args:
            product (Product): Product instance to deploy
        """
        pass
```

### NotificationChannel (Abstract Base)

```python
class NotificationChannel(ABC):
    @abstractmethod
    def notify(self, product):
        """
        Send notification about the product.
        
        Args:
            product (Product): Product instance to notify about
        """
        pass
```

## Configuration Functions

### load_configuration()

```python
def load_configuration():
    """
    Load configuration from config.yaml and secrets.yaml.
    
    Returns:
        dict: Merged configuration dictionary
        
    Raises:
        FileNotFoundError: If config files are missing
    """
```

### find_product_config()

```python
def find_product_config(config, product_name):
    """
    Find product configuration by name.
    
    Args:
        config (dict): Configuration dictionary
        product_name (str): Name of the product to find
        
    Returns:
        dict: Product configuration
        
    Raises:
        ValueError: If product not found
    """
```

## Main Entry Point

### main()

```python
def main():
    """
    Main entry point for the product delivery pipeline.
    
    Command line arguments:
        --repo_name: Product name (required)
        --target_branch: Target branch (optional)
        --stages: Comma-separated list of stages (optional)
    """
```

## Utility Functions

### get_logger()

```python
def get_logger(name):
    """
    Get a configured logger instance.
    
    Args:
        name (str): Logger name
        
    Returns:
        logging.Logger: Configured logger instance
    """
```

## Configuration Schema

### config.yaml Structure

```yaml
products:
  - product_name: "ProductName"
    git_repository: "https://github.com/example/repo.git"
    default_target_branch: "main"
    repositories:
      artifactory:
        enabled: true
        credentials_ref: "artifactory"
      nexus:
        enabled: false
      s3:
        enabled: true
        credentials_ref: "s3"
    notifications:
      email:
        enabled: true
        config:
          smtp_server: "smtp.example.com"
          port: 587
      slack:
        enabled: true
        config:
          webhook_url: "https://hooks.slack.com/services/xxx"
```

### secrets.yaml Structure

```yaml
artifactory:
  username: "${ARTIFACTORY_USER}"
  password: "${ARTIFACTORY_PASSWORD}"

nexus:
  username: "${NEXUS_USER}"
  password: "${NEXUS_PASSWORD}"

s3:
  access_key: "${S3_ACCESS_KEY}"
  secret_key: "${S3_SECRET_KEY}"
``` 