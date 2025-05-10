# Chatwoot API Testing with Python

This repository is dedicated to testing the [Chatwoot](https://www.chatwoot.com/developers/api/) platform using Python.

The purpose of this project is to explore and validate the capabilities of Chatwoot's APIs in a local development environment. It serves as a sandbox for experimenting with the integration, behavior, and response patterns of the system, primarily focused on developer-oriented use cases.

While the current scope is limited to local testing, the structure and insights gathered here may be extended or adapted for more complex, production-grade implementations in the future.

## About Chatwoot

Chatwoot is an open-source customer engagement suite that offers omnichannel support through a unified messaging interface. More details can be found in their official [API documentation](https://www.chatwoot.com/developers/api/).

## Installation and Environment Setup

Follow these steps to set up the project in a clean and isolated environment using Python virtual environments:

### 1. Clone the Repository

```bash
git clone https://github.com/biagolini/PythonChatwoot
cd PythonChatwoot
```

### 2. Create and Activate a Virtual Environment

```bash
python3 -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

### 3. Install Project Dependencies

```bash
pip install -r requirements.txt
```

### 4. (Optional) Add Jupyter Support

If you intend to develop or test code using Jupyter Notebook, install the following packages to ensure compatibility with the virtual environment:

```bash
pip install notebook jupyterlab ipykernel
```

### 5. (Optional) Register the Virtual Environment with Jupyter

To make the virtual environment available as a kernel in Jupyter:

```bash
python -m ipykernel install --user --name=venv --display-name "Python (venv)"
```

### 6. (Optional) Verify Installed Packages

To list all installed packages within the virtual environment:

```bash
pip freeze
```

## Environment Variables

You must create a `.env` file in the root of the project with the following structure:

```
CHATWOOT_TOKEN=xxxxxxxxxxx
CHATWOOT_BASE_URL=https://app.chatwoot.com
```

The `CHATWOOT_BASE_URL` can be modified if you are working with a self-hosted instance of Chatwoot, such as on-premise installations or cloud deployments (e.g., EC2 instances on AWS).

---

**Note**: This repository is not affiliated with Chatwoot. It is purely for personal testing and learning purposes.
