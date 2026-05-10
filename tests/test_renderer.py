from build.renderer import render


def test_replaces_known_variable():
    result = render("<p>{{BUSINESS_NAME}}</p>", {"BUSINESS_NAME": "Priority Plumbing"})
    assert result == "<p>Priority Plumbing</p>"


def test_missing_variable_renders_empty():
    result = render("<p>{{UNKNOWN}}</p>", {})
    assert result == "<p></p>"


def test_blank_value_renders_empty():
    result = render("<a href='{{FACEBOOK}}'>FB</a>", {"FACEBOOK": ""})
    assert result == "<a href=''>FB</a>"


def test_multiple_variables_in_one_template():
    template = "<title>{{SERVICE_1}} in {{CITY_NAME}} | {{BUSINESS_NAME}}</title>"
    config = {"SERVICE_1": "Plumber", "CITY_NAME": "Cape Coral", "BUSINESS_NAME": "Priority Plumbing"}
    result = render(template, config)
    assert result == "<title>Plumber in Cape Coral | Priority Plumbing</title>"


def test_does_not_touch_css_var_syntax():
    result = render("color: var(--accent);", {"accent": "red"})
    assert result == "color: var(--accent);"
