<!-- source: https://github.com/ccsaltik-photography/GhostMannequinEngine, fetched 2026-11-07, http 200, rendered with Playwright -->
                                                                 GitHub - ccsaltik-photography/GhostMannequinEngine: Industrial Autonomous Ghost Mannequin Engine (SAM 3.1 + TPS) · GitHub                                             

[Skip to content](#start-of-content)               

## Navigation Menu

[](/)

[Sign in](/login?return_to=https%3A%2F%2Fgithub.com%2Fccsaltik-photography%2FGhostMannequinEngine)

[Sign in](/login?return_to=https%3A%2F%2Fgithub.com%2Fccsaltik-photography%2FGhostMannequinEngine)

[Sign up](/signup?ref_cta=Sign+up&ref_loc=header+logged+out&ref_page=%2F%3Cuser-name%3E%2F%3Crepo-name%3E&source=header-repo&source_repo=ccsaltik-photography%2FGhostMannequinEngine)

Appearance settings

You signed in with another tab or window. Reload to refresh your session. You signed out in another tab or window. Reload to refresh your session. You switched accounts on another tab or window. Reload to refresh your session. Dismiss alert

             

## Repository navigation

 [](/ccsaltik-photography/GhostMannequinEngine)

![ccsaltik-photography](https://avatars.githubusercontent.com/u/312382300?s=60&v=4)

**[GhostMannequinEngine](/ccsaltik-photography/GhostMannequinEngine)**

Public

-   [Notifications](/login?return_to=%2Fccsaltik-photography%2FGhostMannequinEngine)You must be signed in to change notification settings
-   [Fork0 (0)](/login?return_to=%2Fccsaltik-photography%2FGhostMannequinEngine)
-   [Star0 (0)](/login?return_to=%2Fccsaltik-photography%2FGhostMannequinEngine)You must be signed in to star a repository

## About

Industrial Autonomous Ghost Mannequin Engine (SAM 3.1 + TPS)

### Resources

[Readme](#readme-ov-file)

[Activity](/ccsaltik-photography/GhostMannequinEngine/activity)

### Stars

**0** stars

### Watchers

**0** watching

### Forks

[**0** forks](/ccsaltik-photography/GhostMannequinEngine/forks)

[Report repository](/contact/report-content?content_url=https%3A%2F%2Fgithub.com%2Fccsaltik-photography%2FGhostMannequinEngine&report=ccsaltik-photography+%28user%29)

[Branches](/ccsaltik-photography/GhostMannequinEngine/branches)[Tags](/ccsaltik-photography/GhostMannequinEngine/tags)

[](/ccsaltik-photography/GhostMannequinEngine/branches)[](/ccsaltik-photography/GhostMannequinEngine/tags)

Open more actions menu

## Latest commit

## History

[2 Commits](/ccsaltik-photography/GhostMannequinEngine/commits/main/)

[](/ccsaltik-photography/GhostMannequinEngine/commits/main/)2 Commits

## Folders and files

Name

Name

Last commit message

Last commit date

[sam3](/ccsaltik-photography/GhostMannequinEngine/tree/main/sam3 "sam3")

[sam3](/ccsaltik-photography/GhostMannequinEngine/tree/main/sam3 "sam3")

[README.md](/ccsaltik-photography/GhostMannequinEngine/blob/main/README.md "README.md")

[README.md](/ccsaltik-photography/GhostMannequinEngine/blob/main/README.md "README.md")

[ghost\_auto.py](/ccsaltik-photography/GhostMannequinEngine/blob/main/ghost_auto.py "ghost_auto.py")

[ghost\_auto.py](/ccsaltik-photography/GhostMannequinEngine/blob/main/ghost_auto.py "ghost_auto.py")

[requirements.txt](/ccsaltik-photography/GhostMannequinEngine/blob/main/requirements.txt "requirements.txt")

[requirements.txt](/ccsaltik-photography/GhostMannequinEngine/blob/main/requirements.txt "requirements.txt")

## Repository files navigation

# Ghost Auto: Industrial Autonomous Mannequin Engine

[](#ghost-auto-industrial-autonomous-mannequin-engine)

This project automates the process of creating "Ghost Mannequin" (invisible mannequin) product photography. It seamlessly fuses an on-hanger product image with an unbuttoned/flat lay back-collar image, completely automatically.

## Core Architecture

[](#core-architecture)

1.  **Torso Silhouette Locking (Global Translation):**
    -   Automatically calculates global `(dx, dy)` shift by aligning the shoulder silhouettes of both images.
2.  **SAM 3.1 Neural Masking:**
    -   Detects the inner collar cavity and generates a hole-free "Waterfall" mask to ensure no background leakage.
3.  **Thin Plate Spline (TPS) Elastomer Warp:**
    -   Uses RBF interpolation to perform a 4-corner warp.
    -   Dynamically detects the actual fabric start (ignoring metal hanger hooks via connected components and run-length filtering).
    -   Warps the donor back collar up to the lapel seam, while applying a 20% counter-balance to the bottom corners to ensure the brand label has zero distortion.
4.  **Closed-Loop QC Bot:**
    -   Automatically inspects the final composite for black pixels, hanger leakage, and seam continuity before passing the final image.

## Requirements

[](#requirements)

Ensure you have `uv` or `pip` installed, then install dependencies:

pip install -r requirements.txt

_(Note: Requires PyTorch, OpenCV, NumPy, SciPy, and SAM 3.1 weights in `weights/sam3.1/`)_

## Usage

[](#usage)

python ghost\_auto.py --hanger "input\_hanger.tif" --flat "input\_flat.tif" --out "output/"

## About

Industrial Autonomous Ghost Mannequin Engine (SAM 3.1 + TPS)

### Resources

[Readme](#readme-ov-file)

[Activity](/ccsaltik-photography/GhostMannequinEngine/activity)

### Stars

**0** stars

### Watchers

**0** watching

### Forks

[**0** forks](/ccsaltik-photography/GhostMannequinEngine/forks)

[Report repository](/contact/report-content?content_url=https%3A%2F%2Fgithub.com%2Fccsaltik-photography%2FGhostMannequinEngine&report=ccsaltik-photography+%28user%29)

## Releases

## Packages

## Contributors

## Languages

You can’t perform that action at this time.
