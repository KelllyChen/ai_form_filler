from formfiller.llm_api import query_llm
import os

def test_mock_response(monkeypatch):
    monkeypatch.setenv("USE_MOCK", "true")
    result = query_llm("Generate a value for the form field: 'summary_about_you'")
    assert "(Mocked" in result
