import subprocess

tex_file = "vsresume.tex"

subprocess.run(
        ["pdflatex", "-interaction=nonstopmode", "-halt-on-error", tex_file],
        check=True
    )