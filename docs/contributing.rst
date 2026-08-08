============
Contributing
============

This project uses `uv <https://docs.astral.sh/uv/>`_ to manage the development
environment and `ruff <https://docs.astral.sh/ruff/>`_ for linting and formatting.

Setup
=====

Install uv following the `installation guide
<https://docs.astral.sh/uv/getting-started/installation/>`_, then::

    uv sync
    uv run pre-commit install

``uv sync`` creates ``.venv`` and installs the project together with every
development dependency. uv downloads and manages the interpreters itself, so
there is no need to install Python versions separately.

Common tasks
============

Running the tests::

    uv run pytest
    uv run --python 3.10 pytest                        # a specific interpreter
    uv run --python pypy3.11 pytest                    # PyPy
    uv run pytest --cov=aes_pkcs5 --cov-report=term    # with coverage

Linting and formatting::

    uv run ruff check --fix .
    uv run ruff format .

Building the documentation::

    uv run --group docs sphinx-build -W -b html docs docs/_build/html

Building the distribution artifacts::

    uv build

``pre-commit`` runs ruff automatically on commit, so the lint and format steps
are usually taken care of for you.

Dependencies
============

Runtime dependencies are declared in ``[project.dependencies]``. Development
dependencies are `PEP 735 <https://peps.python.org/pep-0735/>`_ groups in
``pyproject.toml``:

.. list-table::
   :header-rows: 1

   * - Group
     - Contents
   * - ``test``
     - pytest, pytest-cov
   * - ``docs``
     - Sphinx, sphinx-rtd-theme
   * - ``lint``
     - ruff
   * - ``dev``
     - all of the above plus pre-commit; installed by default

``uv.lock`` is committed so that CI, Read the Docs and local development all
resolve to the same versions. It is not shipped in the sdist or wheel, so it
places no constraint on anyone installing the published package. After changing
a dependency run ``uv lock`` and commit the result — the ``uv-lock`` pre-commit
hook will remind you if you forget.

.. note::

    Sphinx 9 requires Python 3.12+, so the ``docs`` group carries a
    ``python_version >= '3.12'`` marker. The documentation is only ever built on
    Python 3.13, both in CI and on Read the Docs.

The ruff version is pinned in the ``lint`` group and must match the ``rev`` of
the ``ruff-pre-commit`` hook in ``.pre-commit-config.yaml``. When Dependabot
bumps the pin, follow up with ``uv run pre-commit autoupdate``.

Releasing
=========

Bump the version with ``uv version --bump patch`` (or ``minor`` / ``major``),
commit, then push a tag matching the new version, e.g. ``1.0.5``. The *Publish*
workflow verifies that the tag matches ``pyproject.toml``, builds with
``uv build`` and uploads to PyPI using trusted publishing.
