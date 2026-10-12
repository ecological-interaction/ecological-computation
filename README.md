# Ecological computing

Workspace for vegetation-index image and video processing. The three packaged projects are independent Git repositories with their own Python environments and lockfiles; this parent directory is not currently a Git repository.

| Folder | Purpose |
| --- | --- |
| `conir_to_ndvi_image/` | CONIR image processing with an assumed cyan/orange/NIR channel mapping |
| `rgb_to_exg_video/` | Excess Green (ExG) video processing |
| `rgb_to_grvi_video/` | Green-Red Vegetation Index (GRVI) video processing |
| `ndvi_project/` | Earlier NDVI scripts, input images, and generated results |

## Standard project layout

```text
<project>/
├── pyproject.toml
├── uv.lock
├── src/<package>/
├── tests/
├── docs/
├── notebooks/
├── samples/
├── data/
│   ├── raw/
│   └── processed/
└── outputs/
```

Keep reusable code in `src/`, small shareable examples in `samples/`, original local datasets in `data/raw/`, intermediate data in `data/processed/`, and generated results in `outputs/`. Local datasets and outputs are ignored by each project's Git configuration. Full datasets may also remain in external storage.

Run environment and Git commands inside the relevant project directory. See each project's README for its environment setup and script-help command.

The older `ndvi_project/` retains its original layout because its scripts use relative input and output paths. Existing code, media, virtual environments, and external data references have been preserved. The new directories do not redirect existing scripts automatically.
