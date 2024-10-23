#!/bin/bash

export KERAS_BACKEND=torch

python main.py --wav moonshine/assets/beckett.wav --model tiny
