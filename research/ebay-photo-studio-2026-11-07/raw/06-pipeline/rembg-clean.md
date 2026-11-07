<!-- source: https://github.com/mess/rembg-clean, fetched 2026-11-07, http 200, rendered with Playwright -->
                                                                 GitHub - mess/rembg-clean: Automate background removal for product photography. Includes batch processing, AI masking, and specialized halo removal for white backgrounds. · GitHub                                             

[Skip to content](#start-of-content)               

## Navigation Menu

[](/)

[Sign in](/login?return_to=https%3A%2F%2Fgithub.com%2Fmess%2Frembg-clean)

[Sign in](/login?return_to=https%3A%2F%2Fgithub.com%2Fmess%2Frembg-clean)

[Sign up](/signup?ref_cta=Sign+up&ref_loc=header+logged+out&ref_page=%2F%3Cuser-name%3E%2F%3Crepo-name%3E&source=header-repo&source_repo=mess%2Frembg-clean)

Appearance settings

You signed in with another tab or window. Reload to refresh your session. You signed out in another tab or window. Reload to refresh your session. You switched accounts on another tab or window. Reload to refresh your session. Dismiss alert

             

## Repository navigation

 [](/mess/rembg-clean)

![mess](https://avatars.githubusercontent.com/u/86787?s=60&v=4)

**[rembg-clean](/mess/rembg-clean)**

Public

-   [Notifications](/login?return_to=%2Fmess%2Frembg-clean)You must be signed in to change notification settings
-   [Fork0 (0)](/login?return_to=%2Fmess%2Frembg-clean)
-   [Star1 (1)](/login?return_to=%2Fmess%2Frembg-clean)You must be signed in to star a repository

## About

Automate background removal for product photography. Includes batch processing, AI masking, and specialized halo removal for white backgrounds.

### Topics

[alpha-matting](/topics/alpha-matting)[background-removal](/topics/background-removal)[batch-processing](/topics/batch-processing)[computer-vision](/topics/computer-vision)[defringing](/topics/defringing)[rembg](/topics/rembg)

### Resources

[Readme](#readme-ov-file)

[GPL-3.0 license](#GPL-3.0-1-ov-file)

[Activity](/mess/rembg-clean/activity)

### Stars

**1** star

### Watchers

**0** watching

### Forks

[**0** forks](/mess/rembg-clean/forks)

[Report repository](/contact/report-content?content_url=https%3A%2F%2Fgithub.com%2Fmess%2Frembg-clean&report=mess+%28user%29)

[Branches](/mess/rembg-clean/branches)[Tags](/mess/rembg-clean/tags)

[](/mess/rembg-clean/branches)[](/mess/rembg-clean/tags)

Open more actions menu

## Latest commit

## History

[2 Commits](/mess/rembg-clean/commits/main/)

[](/mess/rembg-clean/commits/main/)2 Commits

## Folders and files

Name

Name

Last commit message

Last commit date

[rembg\_clean](/mess/rembg-clean/tree/main/rembg_clean "rembg_clean")

[rembg\_clean](/mess/rembg-clean/tree/main/rembg_clean "rembg_clean")

[.gitignore](/mess/rembg-clean/blob/main/.gitignore ".gitignore")

[.gitignore](/mess/rembg-clean/blob/main/.gitignore ".gitignore")

[LICENSE](/mess/rembg-clean/blob/main/LICENSE "LICENSE")

[LICENSE](/mess/rembg-clean/blob/main/LICENSE "LICENSE")

[README.md](/mess/rembg-clean/blob/main/README.md "README.md")

[README.md](/mess/rembg-clean/blob/main/README.md "README.md")

[inspect\_save.scm](/mess/rembg-clean/blob/main/inspect_save.scm "inspect_save.scm")

[inspect\_save.scm](/mess/rembg-clean/blob/main/inspect_save.scm "inspect_save.scm")

[pyproject.toml](/mess/rembg-clean/blob/main/pyproject.toml "pyproject.toml")

[pyproject.toml](/mess/rembg-clean/blob/main/pyproject.toml "pyproject.toml")

## Repository files navigation

# rembg-clean

[](#rembg-clean)

**rembg-clean** is a CLI automation tool designed to remove backgrounds from batches of images (PNG, JPG) and optionally process GIMP project files (`.xcf`).

Beyond standard background removal, it includes a **custom edge-cleaning (defringing) algorithm** specifically tuned to prevent "halos" when placing cut-out subjects onto white backgrounds (common for e-commerce).

## 🛠 Tools & Dependencies

[](#-tools--dependencies)

This tool relies on the following libraries and software:

-   **[rembg](https://github.com/danielgatis/rembg)**: Powered by U^2-Net, this performs the AI-based background removal.
-   **Pillow (PIL) & NumPy**: Used for image manipulation and the custom defringing algorithm.
-   **GIMP (Optional)**: Used to convert `.xcf` files to PNG before processing.

## 📦 Installation & Virtual Environment

[](#-installation--virtual-environment)

It is highly recommended to run this tool inside a **Python Virtual Environment (.venv)**.

### Why use a venv?

[](#why-use-a-venv)

A virtual environment creates an isolated container for this project's dependencies. This ensures that the specific versions of libraries (like `numpy` or `onnxruntime`) required by `rembg` do not conflict with other Python projects on your system.

### Setup Guide

[](#setup-guide)

1.  **Clone the repository** (or navigate to the folder):
    
    cd path\\to\\rembg\-clean
    
2.  **Create the virtual environment**:
    
    python \-m venv .venv
    
3.  **Activate the environment**:
    
    -   **Windows**:
        
        \\ .\\venv\\Scripts\\activate
        
    -   _Linux/macOS_:
        
        source .venv/bin/activate
        
4.  **Install the project**:
    
    pip install \-e .
    

* * *

## ⚙️ Configuration: GIMP Setup

[](#️-configuration-gimp-setup)

If you want to process **.xcf** files, you must ensure the tool can find the **GIMP Console** executable.

The tool will look for GIMP in common paths, but for reliability (especially with GIMP 3), you should set the `GIMP_EXECUTABLE` environment variable.

### Setting the Environment Variable

[](#setting-the-environment-variable)

Point this variable to `gimp-console-*.exe` (NOT `gimp.exe` or the UI version).

**Windows Example:**

$env:GIMP\_EXECUTABLE \= "C:\\Program Files\\GIMP 3\\bin\\gimp-console-3.0.exe"

_(To make this permanent, use `setx` or edit your System Environment Variables)._

> **Note:** GIMP installed via the Microsoft Store is **not supported** for headless automation due to sandbox restrictions. Please use the standard installer from gimp.org.

* * *

## 🚀 Usage

[](#-usage)

Once installed and configured, you can run the tool directly from your terminal.

### Basic Syntax

[](#basic-syntax)

rembg\-clean "path\\to\\input\_folder" \[OPTIONS\]

### Examples

[](#examples)

**1\. Basic run (process all images in folder):**

rembg\-clean "C:\\Photos\\Products"

**2\. Specify a separate output folder:**

rembg\-clean "C:\\Photos\\Raw" \--out "C:\\Photos\\Cleaned"

**3\. Adjust cleaning strength (removes more white halo):**

rembg\-clean "C:\\Photos\\Products" \--strength 0.8

### Command Line Arguments

[](#command-line-arguments)

Argument

Description

Default

`folder`

**Required.** Input folder containing images to process.

N/A

`--out`

Output folder. If omitted, saves files next to originals.

Same as input

`--gimp`

Manually specify GIMP path (overrides env var).

None

`--model`

Specific `rembg` model to use (e.g., `isnet-general-use`).

`isnet-general-use`

`--strength`

Edge cleaning strength (0.0 to 1.0). Lower values preserve more edge detail; higher values remove more halo.

`1.0`

`--erode`

Alpha micro-erosion (pixels). Shrinks the mask slightly.

`0`

`--skip-existing`

Skips processing if the output file already exists.

`False`

## ⚠️ Important Notes

[](#️-important-notes)

-   **First Run Delay**: When running `rembg` for the first time, it may appear frozen for 1-2 minutes. This is normal; it is compiling code via Numba and downloading the AI model.
-   **Performance**: Process runs on CPU by default unless a compatible GPU/ONNX Runtime is configured.

## About

Automate background removal for product photography. Includes batch processing, AI masking, and specialized halo removal for white backgrounds.

### Topics

[alpha-matting](/topics/alpha-matting)[background-removal](/topics/background-removal)[batch-processing](/topics/batch-processing)[computer-vision](/topics/computer-vision)[defringing](/topics/defringing)[rembg](/topics/rembg)

### Resources

[Readme](#readme-ov-file)

[GPL-3.0 license](#GPL-3.0-1-ov-file)

[Activity](/mess/rembg-clean/activity)

### Stars

**1** star

### Watchers

**0** watching

### Forks

[**0** forks](/mess/rembg-clean/forks)

[Report repository](/contact/report-content?content_url=https%3A%2F%2Fgithub.com%2Fmess%2Frembg-clean&report=mess+%28user%29)

## Releases

## Packages

## Contributors

## Languages

You can’t perform that action at this time.
