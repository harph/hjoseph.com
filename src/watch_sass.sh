#!/bin/sh

# Base directory
BASE_DIR=$(dirname $0)

SASS_DIR="$BASE_DIR/sass"

# output directory
CSS_DIR="$BASE_DIR/static/css"

sass --watch $SASS_DIR:$CSS_DIR

