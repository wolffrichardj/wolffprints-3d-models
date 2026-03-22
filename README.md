# WolffPrints 3D Models

A personal repository for organizing 3D-printable models, experiments, and printer-ready files.

This repo is intended to be a clean home for:
- original designs
- remixes of existing models
- downloaded models that have been reviewed, tuned, or verified for use

The goal is not to lock this collection to any one printer or slicer. Instead, this repository is meant to make it easy to store, browse, version, and describe the models you keep as part of your 3D printing workflow.

## Repository structure

```text
.
├── originals/
├── remixes/
├── templates/
└── verified-downloads/
```

### Folder purposes

- `originals/` — models you created from scratch, including experiments, prototypes, and one-off personal projects.
- `remixes/` — modified versions of models based on someone else's work.
- `verified-downloads/` — downloaded models you want to keep because they printed well, were adjusted for your setup, or are worth tracking locally.
- `templates/` — reusable documentation templates for project folders.

## Recommended per-project layout

Each model or model family should live in its own folder inside one of the top-level categories.

Example:

```text
remixes/
└── spool-holder-wall-mount/
    ├── README.md
    ├── model.3mf
    ├── bracket_v2.stl
    ├── clamp.scad
    └── images/
```

### Suggested naming style

Use short, descriptive, lowercase folder names with hyphens, for example:
- `hex-drawer-insert`
- `filament-spool-adapter`
- `toolhead-camera-mount`

### Lightweight versioning guidance

Keep versioning simple. If you make a small, non-breaking tweak, it is fine to keep iterating within the same project folder. If you make a major or breaking change that creates a new main version of the model, create a new folder with a suffix such as `-v2`, `-v3`, and so on.

Examples:
- `filament-spool-adapter/`
- `filament-spool-adapter-v2/`

This keeps the repository lightweight while still making it clear when an older model line has been replaced by a new main version.

## File types this repo is intended to store

This repository is designed to hold source and printable files such as:
- `.stl`
- `.3mf`
- `.scad`

You can also optionally keep supporting files like:
- reference images
- notes
- assembly instructions
- print profile notes
- licensing/source attribution details

## Project README guidance

Each project folder should include a lightweight `README.md` describing what the model is, where it came from, and how you use it.

A starter template is available at:
- `templates/project-readme-template.md`

Recommended sections for each project README:
- model name
- short description
- category
- version
- source/origin
- changes made
- printing notes
- assembly/use notes
- file inventory
- status

## Suggested workflow

1. Choose the top-level category that best matches the model.
2. Create a dedicated folder for the model.
3. Add the model files (`.stl`, `.3mf`, `.scad`, etc.).
4. Copy the README template into the project folder.
5. Fill in enough detail so you can understand the model later without opening every file.
6. Commit updates as the design changes or becomes more printable.

## Attribution and licensing

For remixes or downloaded models, it is a good idea to track:
- original creator
- source URL
- license terms
- what was changed

That helps preserve attribution and makes it easier to reuse or share responsibly.

## Getting started

To add a new model:

1. Pick the right category folder.
2. Create a new subfolder for the model.
3. Copy `templates/project-readme-template.md` to `README.md` inside that model folder.
4. Add your model files and any supporting assets.
5. Update the README with a short description and notes.

## Repository defaults

This repository also includes GitHub repository settings in `.github/settings.yml` for a lightweight solo-maintainer workflow:
- changes to `main` should go through pull requests
- squash merge is enabled
- merge commits and rebase merges are disabled
- no required reviews or required status checks are configured yet

That gives the repository basic protection without adding process overhead before automated validation exists.
