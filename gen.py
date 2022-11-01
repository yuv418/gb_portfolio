#!/usr/bin/python

import jinja2
import mistune
import os
import distutils

pages = ["index", "contact", "blog", "projects", "work_experience"]
try:
        os.mkdir("output")
except FileExistsError:
    # Do nothing, we already have the directory in question.
    pass

j_env = jinja2.Environment(loader=jinja2.FileSystemLoader(searchpath='.'))

for page in pages:
    with open(page + ".md") as md_f:
        md = md_f.read()
        html = mistune.html(md)

    html = "{% extends 'template.html' %}{% block content %}" + html + "{% endblock %}"
    j_page = j_env.from_string(html)
    with open(f"output/{page}.html", 'w') as html_f:
        html_f.write(j_page.render())

distutils.dir_util.copy_tree("assets", "output/assets")

