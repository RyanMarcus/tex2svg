# < begin copyright > 
# Copyright Ryan Marcus 2016
# 
# This file is part of tex2svg.
# 
# tex2svg is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
# 
# tex2svg is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
# 
# You should have received a copy of the GNU General Public License
# along with tex2svg.  If not, see <http://www.gnu.org/licenses/>.
# 
# < end copyright > 
#! /usr/local/bin/python3

import sqlite3
import sys
import os.path
import os
import subprocess

conn = sqlite3.connect(os.path.expanduser('~/.tex2svg/tex2svg.db'))
c = conn.cursor()
c.execute("""CREATE TABLE IF NOT EXISTS items (latex text, svg text);""")

tex = str(sys.stdin.read()).strip()
c.execute("SELECT svg from items WHERE latex=?", (tex,))
cached_result = c.fetchone()

if cached_result:
    print(cached_result[0])
    exit(0)

    
# we need to create the result and cache it
with open(os.path.expanduser('~/.tex2svg/tmp.tex'), "w") as f:
    f.write("""
\\documentclass{article}
\\usepackage{amsmath}
\\usepackage{amssymb}
\\begin{document}
\\pagestyle{empty}
$$""" + tex + """$$
\\end{document}
""")
os.system("pdflatex -output-directory ~/.tex2svg/ tmp.tex &> /dev/null")
os.system("pdfcrop ~/.tex2svg/tmp.pdf ~/.tex2svg/tmp_crop.pdf &> /dev/null")
os.system("pdf2svg ~/.tex2svg/tmp_crop.pdf ~/.tex2svg/tmp.svg &> /dev/null")
svg = subprocess.check_output("svgo --output - --input ~/.tex2svg/tmp.svg", shell=True).decode("utf-8")
c.execute("INSERT INTO items VALUES(?, ?)", (tex, svg))
print(svg)
conn.commit()
conn.close()

