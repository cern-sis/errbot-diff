{% macro stats(file) -%}
-{{ file.deletions }} ~{{ file.changes }} +{{ file.additions }}
{%- endmacro %}

{% set path = file.filename.split("/")[2] %}
{% set name, kind, extension = path.split(".") %}

**{{ kind }} {{ name }}:** {{ stats(file) }}

[source]({{ file.blob_url }})

``` spoiler diff

````diff

{{ file.patch }}

````

```
