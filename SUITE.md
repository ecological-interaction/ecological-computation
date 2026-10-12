# Ecological Computing — suite coordination

## Workspace boundaries

The suite consists of three independent local repositories:

| Project folder | Scope | Workspace brief |
| --- | --- | --- |
| `conir_to_ndvi_image/` | CONIR image index and visualization | [Brief](conir_to_ndvi_image/WORKSPACE.md) |
| `rgb_to_exg_video/` | Raw-channel Excess Green video | [Brief](rgb_to_exg_video/WORKSPACE.md) |
| `rgb_to_grvi_video/` | GRVI video and visualization controls | [Brief](rgb_to_grvi_video/WORKSPACE.md) |

Use each folder as its own local app project, working directory, environment, and Git boundary. Use the parent Ecological Computing project for suite coordination. The older `ndvi_project/` is reference material outside these three workspaces.

## Shared publication direction

Retain independent packages and commands, presented together under Ecological Computing. Align documentation structure, installation instructions, option meanings, output conventions, diagnostics, examples, and release quality. Preserve each index's formula, units, sensor assumptions, and appropriate display range. Do not introduce a shared runtime package until a concrete need warrants it.

Each project brief records this common direction locally. Keep the briefs synchronized when suite conventions change. Decide publication destination, license, supported Python versions, versioning policy, and any common visual identity before releasing.

## Inspection findings — 2026-09-28

All three contain uv-based package metadata, lockfiles, src layouts, local virtual environments, and Git directories. No Git remotes are configured. The current file listings are untracked. Test directories currently contain scaffolding documentation, not automated suites.

CONIR and GRVI installed commands point to greeting stubs. ExG points to its processing main function. GRVI's main processing module runs at import time. Both video processors invoke FFmpeg, but their validation and failure handling differ. CONIR uses an assumed orange/NIR mapping and percentile display scaling. ExG uses unnormalized `2G-R-B`; GRVI uses `(G-R)/(G+R)`. These differences must be documented rather than hidden by a uniform interface.

This inspection did not run conversions, install dependencies, modify source, or establish scientific calibration or release readiness.

## App registration

At inspection, only the parent Ecological Computing folder was registered as a Codex local project. Register each child repository as a separate local project, using its folder as the primary working directory. The available app tools cannot add project registrations, and computer control of Codex is blocked. These documentation files prepare project context but do not themselves register sidebar projects.
