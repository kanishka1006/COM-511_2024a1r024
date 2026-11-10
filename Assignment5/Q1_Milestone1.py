"""
Assignment 5 - Milestone 1: Represent and Analyse One Listening Item
Course: Python Programming (COM-501)
Course Outcome: CO1 | Bloom's Level: 3

Description:
Captures initial listener metadata and details about a single track or
episode, performs standard type conversions, and calculates total minutes/seconds
along with a slice-based media code.
"""

# Inputs
# Test values: listener='Riya', title='Data Skeptic', creator='Kyle Polich',
# media_type='Podcast', duration_sec=1875, rating=4.5
listener = "Riya"
title = "Data Skeptic"
creator = "Kyle Polich"
media_type = "Podcast"
duration_sec_str = "1875"
rating_str = "4.5"

# Type conversion
duration_sec = int(duration_sec_str)
rating = float(rating_str)

# Calculations
minutes = duration_sec // 60
seconds = duration_sec % 60
media_code = media_type[:3].upper()

# Output
print(f"Listener: {listener} | Track: {title} by {creator}")
print(f"Media Code: {media_code}")
print(f"Duration: {minutes}m {seconds}s (Types: duration={type(duration_sec).__name__}, rating={type(rating).__name__})")
