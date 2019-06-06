# tex2svg

```bash
pip3 install tex2svg
```

A simple program to convert a LaTeX equations to SVGs.

```bash
# for "inline mode" LaTeX
echo "x^2" | tex2svg > x2.svg 

# for "block" LaTeX
echo "x^2" | tex2svg --block > x2.svg
```

Depends on `pdflatex`, `pdfcrop`, `pdf2svg`, and `svgo`. On Arch Linux, you can install these with:

```bash
sudo pacman -S pdf2svg texlive-most npm
sudo npm install -g svgo
```

This program automatically caches outputs. The cache is stored in `~/.tex2svg`. 

