#!/usr/bin/env python

# Copyright 2017 Google Inc. All Rights Reserved.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

"""This application demonstrates how to perform basic operations with the
Google Cloud Vision API.

Example Usage:
python detect.py text ./resources/wakeupcat.jpg
python detect.py labels ./resources/landmark.jpg
python detect.py web ./resources/landmark.jpg
python detect.py web-uri http://wheresgus.com/dog.JPG
python detect.py faces-uri gs://your-bucket/file.jpg

For more information, the documentation at
https://cloud.google.com/vision/docs.
"""

import argparse
import io
import time
import numpy
import subprocess

from google.cloud import vision
from google.cloud.vision import types

# format:    [license, make, model, time]
globalList = [None, None, None, None]
car_makes_list = ['bmw', 'volkswagen', 'honda', 'toyota', 'chevrolet', 'chrysler',
            'ford', 'fiat', 'dodge', 'gmc', 'hyundai', 'jeep', 'kia',
            'land rover', 'lexus', 'lincoln', 'mazda', 'mercedes', 'mini',
            'mitsubishi', 'nissan', 'renault', 'scion', 'skoda', 'suzuki',
            'tesla', 'volvo']
car_type = ['hatchback', 'sedan', 'mpv', 'suv', 'crossover', 'coupe',
            'convertible']

# [START def_detect_labels]
def detect_labels(path):
    """Detects labels in the file."""
    client = vision.ImageAnnotatorClient()

    # [START migration_label_detection]
    with io.open(path, 'rb') as image_file:
        content = image_file.read()

    image = types.Image(content=content)

    response = client.label_detection(image=image)
    labels = response.label_annotations
    for label in labels:
        if label in car_makes_list:
            globalList[1] = label
        if label in car_type:
            globalList[2] = model



# [START def_detect_text]
def detect_text(path):
    """Detects text in the file."""
    client = vision.ImageAnnotatorClient()

    # [START migration_text_detection]
    with io.open(path, 'rb') as image_file:
        content = image_file.read()

    image = types.Image(content=content)

    response = client.text_detection(image=image)
    texts = response.text_annotations

    try:
        globalList[0] = texts[0].description
    except:
        pass

    # [END migration_text_detection]
# [END def_detect_text]

def run_local(image):
    detect_labels(image)
    detect_text(image)
    globalList[3] = time.time()

    # Return vector representing this frame

def main(image):
    run_local(image)
    return globalList

if __name__ == '__main__':

    main(image)

    run_local(args)
