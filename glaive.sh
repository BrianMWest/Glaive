#!/bin/bash

function glaive() {
    local SCRIPT=$1
    shift
    python $SCRIPT.py $*
}
