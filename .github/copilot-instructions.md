# GitHub Copilot Instructions

This repository is a single-page static web app with a single authoritative source file: `index.html`.

## What to do

- Edit `index.html` for UI, styling, and behavior changes.
- Keep changes compatible with a static file deployment.
- Do not add a build system, package manager, or heavy frontend framework unless explicitly requested.

## Project conventions

- HTML, CSS, and JavaScript are co-located in `index.html`.
- Styling is embedded in a `<style>` block.
- Camera and model logic use CDN-hosted TensorFlow.js + Teachable Machine.
- Preserve the `tmImage`/TensorFlow.js CDN approach unless given an explicit reason to refactor.

## Notes for Copilot

- Prefer simple inline edits over adding new files or tools.
- If a development server is needed, use a simple static server or browser preview.
- Use existing IDs and classes when updating the UI.
