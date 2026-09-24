# 4. Run tests automatically with GitHub Actions

[Previous: testing](03-testing.md) · [Next: OOP across languages](05-oop-across-languages.md)

GitHub Actions runs checks on GitHub's machines when your code changes. This is **continuous integration (CI)**: each pushed revision is checked using the same commands your team runs locally.

## Type the workflow

Create `.github/workflows` in your project and type [tests.yml](../.github/workflows/tests.yml) into `.github/workflows/tests.yml`. Keep the indentation exactly as shown; YAML uses indentation to express structure.

| Workflow section | Meaning |
| --- | --- |
| `name` | Labels the workflow as **Tests** in GitHub. |
| `on` | Runs for pushes, pull requests, and manual requests (`workflow_dispatch`). |
| `permissions` | Gives the workflow read access to repository contents. |
| `jobs.test` | Defines the test job. |
| `runs-on` | Uses a fresh GitHub-hosted Ubuntu runner. |
| `strategy.matrix` | Runs a separate job for Python 3.11, 3.12, 3.13, and 3.14. |
| `uses` | Invokes a reusable action to check out code or install Python. |
| `run` | Executes a shell command to install dependencies or run pytest. |

`${{ matrix.python-version }}` selects the Python version for each job. Checking out the code comes first because the runner does not initially contain your project.

The final step runs `python -m pytest`. `pytest.ini` supplies the coverage options: a failed assertion **or coverage below 100%** fails the job. The workflow checks the project; it does not deploy the calculator or automatically prevent merges. Required merge checks are a separate repository setting.

## Publish your own repository

Create an empty repository under your GitHub account. Do not initialize it with extra files. In your local project:

```bash
git init -b main
git add .
git status
git commit -m "Build OOP calculator with tests"
git remote add origin https://github.com/YOUR-USERNAME/YOUR-REPOSITORY.git
git push -u origin main
```

Replace the URL placeholders with your repository details. Before committing, verify that `.venv`, coverage reports, and private files are absent from the staged files. GitHub may require you to sign in when pushing.

## Read a run

Open your repository's **Actions → Tests** page and select the latest run. Each Python version should pass. For a failure, open the failing step and read the first error; reproduce it locally with `python -m pytest`, fix it, commit, and push again.

You can also choose **Run workflow** from the Tests page once the workflow is on the default branch. If you reuse the reference README badge, replace its account and repository with your own.

**Checkpoint:** your own GitHub repository shows all four jobs passing. Explain why a local pass alone does not verify another Python version or a clean machine.
