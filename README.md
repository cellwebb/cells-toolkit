<!-- markdownlint-disable -->

# Cell's CLI Toolkit

**Cell's CLI Toolkit** (CCTK) is a collection of useful scripts for cross-project development. It provides command-line tools to streamline common tasks like generating commit messages and creating changelogs, all with minimal configuration.

---

## Features

- **`gac`**: Automates the process of staging, generating commit messages, and committing changes to your repository.
- **`ach`**: Automatically generates a changelog based on your project's Git history.

---

## Installation

### 1. Using `pipx` (Recommended)

Install the toolkit globally with pipx to ensure isolation:

```bash
pipx install path/to/your_toolkit
```

### 2. Using `pip`

Alternatively, you can install the toolkit using pip:

```bash
pip install path/to/your_toolkit
```

---

## Usage

### Command Overview

Run the following commands in your terminal to execute the respective tools:

#### Auto Commit (`gac`)

```bash
gac
```

This command automates Git commit creation:

- Stages your changes.
- Analyzes the changes to generate a meaningful commit message.
- Creates and executes the commit.

#### Auto Changelog (`ach`)

```bash
ach
```

Generates a changelog based on your Git history:

- Outputs a changelog in markdown format.
- Includes all commits since the last tag.

---

## Configuration

### Environment Variables

Place a `.env` file in the project root or the directory where you're running the tool to customize its behavior.

Example `.env` file:

```env
GITHUB_TOKEN=your_github_token
CHANGELOG_FORMAT=markdown
```

### Shared Functionality

Both `gac` and `ach` share common logic (e.g., environment variable handling, logging) through a shared module. This ensures consistency and reduces code duplication.

---

## Development

### Requirements

- Python 3.12+
- Click (CLI framework)

### Install for Development

1. Clone the repository:

   ```bash
   git clone https://github.com/yourusername/your_toolkit.git
   cd your_toolkit
   ```

2. Create a virtual environment:

   ```bash
   python3.12 -m venv .venv
   source .venv/bin/activate
   ```

3. Install dependencies:

   ```bash
   pip install -e .[dev]
   ```

### Running Commands Locally

Use the CLI commands directly:

```bash
python -m your_toolkit.cli gac
python -m your_toolkit.cli ach
```

---

## Contributing

Contributions are welcome! Please follow these steps to contribute:

1. Fork the repository.
2. Create a new branch for your feature/bugfix.
3. Make your changes and write tests.
4. Submit a pull request.

---

## License

This project is licensed under the [MIT License](LICENSE).

---

## Contact

For questions or support, please open an issue on GitHub or email [your.email@example.com](mailto:your.email@example.com).
