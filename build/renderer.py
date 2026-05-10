import re

_PATTERN = re.compile(r"\{\{(\w+)\}\}")


def render(template: str, config: dict) -> str:
    return _PATTERN.sub(lambda m: config.get(m.group(1), ""), template)
