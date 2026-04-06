#!/bin/bash

errors=0
logfile="compile-errors.log"
> "$logfile"

for dir in A-*/ B-*/ C-*/ D-*/; do
    for tex in "$dir"*.tex; do
        [ -f "$tex" ] || continue
        echo "Compiling $tex..."
        if ! pdflatex -interaction=nonstopmode -output-directory "$dir" "$tex" >> "$logfile" 2>&1; then
            errors=$((errors + 1))
            echo "  ERROR: see $logfile for details"
        fi
    done
done

echo "Cleaning up..."
for dir in A-*/ B-*/ C-*/ D-*/; do
    for ext in aux fdb* fls log nav out snm synctex.gz toc; do
        rm -f "$dir"*."$ext"
    done
done

if [ "$errors" -gt 0 ]; then
    echo "Done with $errors compilation error(s)."
    exit 1
fi
echo "Done."
