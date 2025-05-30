import json
import os
from PyPDF2 import PdfReader
from llm_api import query_llm


def extract_text_from_pdf(pdf_path):
    reader = PdfReader(pdf_path)
    text = "\n".join([page.extract_text() or "" for page in reader.pages])
    return text.strip()

def load_text_file(txt_path):
    with open(txt_path, "r", encoding="utf-8") as f:
        return f.read().strip()


def create_prompt(field, proflie, position, job_description):
    # use user profile to create prompt
    profile_str = json.dumps(proflie, indent=2)
    return f"Given the following user profile:\n{profile_str}\nposition:\n{position}\nand job description:\n{job_description}\nGenerate a value for the form field: '{field}'."


def fill_form(template_path, profile_path, position, jb_path, output_path):
    # load from template
    with open(template_path, "r") as f:
        form_template = json.load(f)

    user_profile = extract_text_from_pdf(profile_path)

    job_description = load_text_file(jb_path)

    filled_form={}

    for field in form_template:
        if form_template[field] == "":
            # create a prompt using profile
            prompt = create_prompt(field, user_profile, position, job_description)
            response = query_llm(prompt)
            filled_form[field] = response
        else:
            filled_form[field] = form_template[field]

    # ensure output directory exists
    output_dir = os.path.dirname(output_path)
    if output_dir and not os.path.exists(output_dir):
        os.makedirs(output_dir)

    
    with open(output_path, "w") as f:
        json.dump(filled_form, f, indent=2)

