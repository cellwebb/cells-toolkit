<!-- markdownlint-disable -->

# Cell's CLI Toolkit

**Cell's CLI Toolkit** (CCTK) is a collection of useful scripts for cross-project development. It provides command-line tools to streamline common tasks like generating commit messages and creating changelogs, all with minimal configuration.

---

## Features

- **`gac`**: Automates the process of staging, generating commit messages, and committing changes to your repository.
- **`ach`**: Automatically generates a changelog based on your project's Git history.

---

## Installation

### 1. Using Hatch (Recommended for Development and Isolation)
Hatch simplifies environment and dependency management. To use Hatch:

1. Clone the repository:
   ```bash
   git clone https://github.com/yourusername/cells_toolkit.git
   cd cells_toolkit
   ```

2. Create and activate a Hatch-managed environment:
   ```bash
   hatch env create
   hatch shell
   ```

3. Install the toolkit in development mode:
   ```bash
   hatch develop
   ```

### 2. Using `pipx` (Recommended for Global Use)
For global installation and CLI access, use pipx:

```bash
pipx install path/to/cells_toolkit
```

### 3. Using `pip`
For traditional installation without Hatch:
```bash
pip install path/to/cells_toolkit
```

---

## Usage

### Command Overview

Run the following commands in your terminal to execute the respective tools:

#### Auto Commit (`gac`)

```bash
hatch run gac
```

This command automates Git commit creation:

- Stages your changes.
- Analyzes the changes to generate a meaningful commit message.
- Creates and executes the commit.

#### Auto Changelog (`ach`)

```bash
hatch run ach
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
- Hatch (Project Manager)

### Install for Development

Follow these steps to set up your development environment:

1. Clone the repository:
   ```bash
   git clone https://github.com/yourusername/cells_toolkit.git
   cd cells_toolkit
   ```

2. Create and activate a Hatch environment:
   ```bash
   hatch env create
   hatch shell
   ```

3. Install development dependencies:
   ```bash
   hatch develop
   ```

### Running Commands Locally
Run CLI commands directly using Hatch's environment:

```bash
hatch run gac
hatch run ach
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

This project is licensed under the [Mozilla Public License 2.0](LICENSE).

---

## Contact

For questions or support, please open an issue on GitHub or email [your.email@example.com](mailto:your.email@example.com).
