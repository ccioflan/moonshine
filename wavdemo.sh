#!/bin/bash

export KERAS_BACKEND=torch

python main.py --wav moonshine/assets/Reagan.wav --model tiny
