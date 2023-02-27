{% macro stats(file) -%}
$${\textcolor{red}{-}}$$ {{ file.deletions }} $${\textcolor{orange}{\text{\textasciitilde}}}$$ {{ file.changes }} $${\textcolor{green}{+}}$$ {{ file.additions }}
{%- endmacro %}

| Kind | Name | Stats | File |
| --- | --- | --- | --- |
{% for file in files|sort(attribute='filename') -%}
{% set path = file.filename.split("/")[2] %}
{%- set name, kind, extension = path.split(".") -%}
| {{ kind }} | {{ name }} | {{ stats(file) }} | [{{ file.filename }}]({{ file.blob_url }}) |
{% endfor %}
