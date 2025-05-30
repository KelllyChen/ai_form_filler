import pytest
import json
import os
from form_filler import fill_form
from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import letter

def test_fill_form_with_mock(tmp_path, monkeypatch):
    

    def create_dummy_pdf(path, text="Test Resume Content"):
        c = canvas.Canvas(str(path), pagesize=letter)
        c.drawString(100, 750, text)
        c.save()

    monkeypatch.setenv("USE_MOCK", "true")

    template = {
        "full_name": "",
        "summary_about_you": "",
        "position_applied": "AI Intern"
    }

    form_path = tmp_path / "form.json"
    profile_path = tmp_path / "profile.pdf"
    job_path = tmp_path / "job.txt"
    output_path = tmp_path / "filled.json"

    form_path.write_text(json.dumps(template))
    create_dummy_pdf(profile_path, "Kelly Chen\nPython, AI\nProjects: Book Recommender")
    job_path.write_text("We're hiring AI interns to explore LLMs.")

    fill_form(str(form_path), str(profile_path), "AI Intern", str(job_path), str(output_path))

    result = json.loads(output_path.read_text())
    assert result["full_name"].startswith("(Mocked")
    assert result["summary_about_you"].startswith("(Mocked")
    assert result["position_applied"] == "AI Intern"
