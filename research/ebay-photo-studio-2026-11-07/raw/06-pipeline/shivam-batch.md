<!-- source: https://github.com/Shivam-Singh-Coder/python-batch-background-remover, fetched 2026-11-07, http 200, rendered with Playwright -->
                                                                 GitHub - Shivam-Singh-Coder/python-batch-background-remover · GitHub                                             

[Skip to content](#start-of-content)               

## Navigation Menu

[](/)

[Sign in](/login?return_to=https%3A%2F%2Fgithub.com%2FShivam-Singh-Coder%2Fpython-batch-background-remover)

[Sign in](/login?return_to=https%3A%2F%2Fgithub.com%2FShivam-Singh-Coder%2Fpython-batch-background-remover)

[Sign up](/signup?ref_cta=Sign+up&ref_loc=header+logged+out&ref_page=%2F%3Cuser-name%3E%2F%3Crepo-name%3E&source=header-repo&source_repo=Shivam-Singh-Coder%2Fpython-batch-background-remover)

Appearance settings

You signed in with another tab or window. Reload to refresh your session. You signed out in another tab or window. Reload to refresh your session. You switched accounts on another tab or window. Reload to refresh your session. Dismiss alert

             

## Repository navigation

 [](/Shivam-Singh-Coder/python-batch-background-remover)

![Shivam-Singh-Coder](https://avatars.githubusercontent.com/u/128234088?s=60&v=4)

**[python-batch-background-remover](/Shivam-Singh-Coder/python-batch-background-remover)**

Public

-   [Notifications](/login?return_to=%2FShivam-Singh-Coder%2Fpython-batch-background-remover)You must be signed in to change notification settings
-   [Fork0 (0)](/login?return_to=%2FShivam-Singh-Coder%2Fpython-batch-background-remover)
-   [Star0 (0)](/login?return_to=%2FShivam-Singh-Coder%2Fpython-batch-background-remover)You must be signed in to star a repository

## About

No description, website, or topics provided.

### Resources

[Readme](#readme-ov-file)

[Activity](/Shivam-Singh-Coder/python-batch-background-remover/activity)

### Stars

**0** stars

### Watchers

**0** watching

### Forks

[**0** forks](/Shivam-Singh-Coder/python-batch-background-remover/forks)

[Report repository](/contact/report-content?content_url=https%3A%2F%2Fgithub.com%2FShivam-Singh-Coder%2Fpython-batch-background-remover&report=Shivam-Singh-Coder+%28user%29)

[Branches](/Shivam-Singh-Coder/python-batch-background-remover/branches)[Tags](/Shivam-Singh-Coder/python-batch-background-remover/tags)

[](/Shivam-Singh-Coder/python-batch-background-remover/branches)[](/Shivam-Singh-Coder/python-batch-background-remover/tags)

Open more actions menu

## Latest commit

## History

[5 Commits](/Shivam-Singh-Coder/python-batch-background-remover/commits/main/)

[](/Shivam-Singh-Coder/python-batch-background-remover/commits/main/)5 Commits

## Folders and files

Name

Name

Last commit message

Last commit date

[.gitignore](/Shivam-Singh-Coder/python-batch-background-remover/blob/main/.gitignore ".gitignore")

[.gitignore](/Shivam-Singh-Coder/python-batch-background-remover/blob/main/.gitignore ".gitignore")

[README.md](/Shivam-Singh-Coder/python-batch-background-remover/blob/main/README.md "README.md")

[README.md](/Shivam-Singh-Coder/python-batch-background-remover/blob/main/README.md "README.md")

[remove\_backgrounds.py](/Shivam-Singh-Coder/python-batch-background-remover/blob/main/remove_backgrounds.py "remove_backgrounds.py")

[remove\_backgrounds.py](/Shivam-Singh-Coder/python-batch-background-remover/blob/main/remove_backgrounds.py "remove_backgrounds.py")

[requirements.txt](/Shivam-Singh-Coder/python-batch-background-remover/blob/main/requirements.txt "requirements.txt")

[requirements.txt](/Shivam-Singh-Coder/python-batch-background-remover/blob/main/requirements.txt "requirements.txt")

## Repository files navigation

# Python Batch Background Remover

[](#python-batch-background-remover)

A simple, locally run Python tool that removes backgrounds from every supported image in a folder and saves the results as transparent PNG files.

It uses [`rembg`](https://github.com/danielgatis/rembg) with the `u2net` model and Pillow for image handling. No API key is required.

## Features

[](#features)

-   Processes multiple images in one folder (not subfolders).
-   Supports `.jpg`, `.jpeg`, `.png`, `.webp`, `.bmp`, `.tif`, and `.tiff` files (case-insensitive).
-   Saves output as PNG in a `background_removed` subfolder inside the selected folder.
-   Leaves the original images unchanged.
-   Continues processing other images if an individual image fails.
-   Prompts for a folder path and accepts paths wrapped in single or double quotes.

## Requirements

[](#requirements)

-   Python installed and available as `python` (or use `python3` on systems where that is the Python command).
-   An internet connection the first time the `u2net` model is needed so it can be downloaded. Once cached, model processing can work offline.

Dependencies are listed in `requirements.txt`:

```
rembg[cpu]
Pillow
```

## Installation

[](#installation)

Clone the repository and enter its directory:

git clone https://github.com/Shivam-Singh-Coder/python-batch-background-remover.git
cd python-batch-background-remover

Install the dependencies:

python -m pip install -r requirements.txt

## Usage

[](#usage)

Run the script:

python remove\_backgrounds.py

When prompted, enter the path to the folder containing the images:

```
Enter the full path of the image folder: "C:\Users\you\Pictures\products"
```

The script scans files directly in that folder, loads the `u2net` model, and writes the results to `background_removed` inside the input folder.

## Example

[](#example)

Before:

```
products/
├── mug.jpg
├── shirt.png
└── logo.webp
```

After running the script:

```
products/
├── mug.jpg
├── shirt.png
├── logo.webp
└── background_removed/
    ├── mug.png
    ├── shirt.png
    └── logo.png
```

When two input files would produce the same output name (for example, `photo.jpg` and `photo.png`), the later output uses the input extension in its name, such as `photo_jpg.png`. Existing outputs may be replaced when the script is run again.

Example terminal output:

```
Enter the full path of the image folder: C:\Users\you\Pictures\products
Found 3 image(s). Loading AI model...
[1/3] OK: logo.webp -> logo.png
[2/3] OK: mug.jpg -> mug.png
[3/3] OK: shirt.png -> shirt.png
Finished: 3/3 successful. Output: C:\Users\you\Pictures\products\background_removed
```

## Notes

[](#notes)

-   The script does not scan subfolders or accept a folder path as a command-line argument; it asks for the path interactively.
-   Processing time depends on image size and computer hardware. Large batches may use substantial memory.
-   Results can vary, especially for fine details, complex backgrounds, or transparent objects.

## Troubleshooting

[](#troubleshooting)

### `Invalid folder` or no supported images found

[](#invalid-folder-or-no-supported-images-found)

Check that the folder path is correct and that the supported image files are directly inside the folder (not only in subfolders).

### Missing module error

[](#missing-module-error)

Install the dependencies with:

python -m pip install -r requirements.txt

### Model download or network error

[](#model-download-or-network-error)

The model may need to download the first time it runs. Check your internet connection and run the script again.

## Contributing

[](#contributing)

Bug reports, suggestions, and pull requests are welcome.

## License

[](#license)

No license is specified yet. Add a `LICENSE` file to define how this project may be used, modified, and distributed.

## About

No description, website, or topics provided.

### Resources

[Readme](#readme-ov-file)

[Activity](/Shivam-Singh-Coder/python-batch-background-remover/activity)

### Stars

**0** stars

### Watchers

**0** watching

### Forks

[**0** forks](/Shivam-Singh-Coder/python-batch-background-remover/forks)

[Report repository](/contact/report-content?content_url=https%3A%2F%2Fgithub.com%2FShivam-Singh-Coder%2Fpython-batch-background-remover&report=Shivam-Singh-Coder+%28user%29)

## Releases

## Packages

## Contributors

## Languages

You can’t perform that action at this time.
