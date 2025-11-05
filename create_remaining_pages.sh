#!/bin/bash

# This script will help track which HTML files need to be created
# Arizona, Arkansas, California, Colorado, Connecticut, Delaware, Florida
# Georgia, Hawaii, Idaho, Illinois, Indiana, Iowa

echo "Remaining states to create:"
for state in arizona arkansas california colorado connecticut delaware florida georgia hawaii idaho illinois indiana iowa; do
    if [ ! -f "/Users/cjoh/turtlebook/$state/index.html" ]; then
        echo "- $state"
    fi
done
