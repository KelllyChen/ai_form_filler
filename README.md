# FormFiller CLI
**FormFiller** is a command-line tool that uses GPT-4 to automatically fill out job application forms based on your resume and the job description.

## Features

- Accepts a form template in JSON
- Uses your resume (PDF) and a job description (TXT)
- Auto-generates responses using GPT-4 or a mock
- Outputs a completed form in JSON
- Packaged as a reusable CLI tool

## Installation
clone the repo and navigate to the project folder:

```bash
git clone https://github.com/KelllyChen/ai_form_filler.git
cd ai_form_filler
```

Create a `.env` file in the root directory and add:

```env
OPENAI_API_KEY=your-openai-api-key
USE_MOCK=false
```

Set `USE_MOCK=true` to test without calling GPT-4.

Then install the tool locally (inside a virtual environment is recommended):
```bash
pip install -e .
```

## Usage

```bash
formfiller fill-form --template example_inputs/form.json --profile example_inputs/resume.pdf --position "AI Intern" --jb example_inputs/jb.txt --output output/filled_form.json
```

## Testing

Run tests:

```bash
pytest
```

Check test coverage:

```bash
coverage run -m pytest
coverage report -m
```



