# PantryPi

## Overview
_PantryPal_ is a Raspberry Pi based project which classifies fruit and vegetables (in a _Pantry_) using a simplified SqueezeNet CNN with a sliding window for multi-object classification in an image. The resulting image was uploaded to DropBox by the Raspberry Pi and a message containing the contents of the _Pantry_ was sent by the CNN (using PubNub) to a simple Android application. The message (containing the list of classified items) and image was displayed on an Android application which also allowed the user to define their weekly shopping list and compare that list to the list of classified fruit and vegatables from the image.

## Description
This project simply listens for a message from the Android application sent using PubNub, captures an image and uploads the image to DropBox for the computation application to process (_PantryPal_).

## Software Versions
- python    `3.6.1`
- dropbox   `8.4.0`
- json      `2.6.0`
- pubnub    `3.9.0`
