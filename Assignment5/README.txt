================================================================================
ASSIGNMENT 5: DIGITAL PLAYLIST AND LISTENING ANALYTICS SYSTEM
Course: Python Programming (COM-501) | Semester V
Model Institute of Engineering & Technology (Autonomous), Jammu
Student Name: Kanishka Suri
Roll Number : 2024A1R024
================================================================================

PROJECT OVERVIEW
----------------
This project implements a console-based Python application called the
"Digital Playlist and Listening Analytics System". It models real-world media
consumption (songs and podcasts), classifies listening items, manages playlists
using Object-Oriented Composition, performs analytics using modular functions
and lambdas, and maintains persistent listening history with robust error
and exception handling.

The assignment is developed progressively across five milestones, mapping directly
to Course Outcomes CO1 through CO5 (Bloom's Taxonomy Levels 3 through 5).

================================================================================
DIRECTORY STRUCTURE
================================================================================
Assignment5/
│
├── Q1_Milestone1.py          # Milestone 1: Represent & analyse single listening item (CO1)
│
├── Q2_Milestone2.py          # Milestone 2: Multi-item queue with collections & loops (CO2)
│
├── Q3_Milestone3.py          # Milestone 3: OOP playlist with object composition (CO3)
│
├── Q4_Milestone4/            # Milestone 4: Modular analytics package (CO4)
│   ├── main.py               # Main execution, lambda sorting, dict menu dispatch
│   └── media_utils.py        # Reusable utility functions
│
├── Q5_Milestone5.py          # Milestone 5: Persistent file storage & error recovery (CO5)
│
├── listening_history.txt     # Pipe-delimited persistent listening log file
│
└── README.txt                # Documentation and execution instructions

================================================================================
MILESTONE BREAKDOWN & COURSE OUTCOMES
================================================================================

1. Milestone 1 - Represent and Analyse One Listening Item
   - File: Q1_Milestone1.py
   - Course Outcome: CO1 (Bloom's Level: 3)
   - Concepts: String parsing, data type casting (int, float), arithmetic operators
     (// and %), string slicing (first 3 letters for media code), and formatted strings.
   - Test Input:
       Listener: "Riya"
       Title   : "Data Skeptic"
       Creator : "Kyle Polich"
       Type    : "Podcast"
       Duration: 1875 seconds
       Rating  : 4.5
   - Expected Output:
       Listener: Riya | Track: Data Skeptic by Kyle Polich
       Media Code: POD
       Duration: 31m 15s (Types: duration=int, rating=float)

--------------------------------------------------------------------------------

2. Milestone 2 - Build a Multi-Item Listening Queue
   - File: Q2_Milestone2.py
   - Course Outcome: CO2 (Bloom's Level: 4)
   - Concepts: Lists of dictionaries, sets (unique creators), conditional logic
     (input validation rejecting duration <= 0 or ratings outside 1.0-5.0),
     duration categorization (Quick: <=300s, Standard: 301-1800s, Long-form: >1800s),
     and aggregation (sum, max with lambda).
   - Expected Output:
       [REJECTED] Invalid record: Bad Item
       Total Listening Time: 2200s
       Unique Creators Count: 2
       Top Rated: Talk Episode (4.8)
       Categories: {'Quick': 1, 'Standard': 0, 'Long-form': 1}

--------------------------------------------------------------------------------

3. Milestone 3 - Model a Playlist Using Object-Oriented Composition
   - File: Q3_Milestone3.py
   - Course Outcome: CO3 (Bloom's Level: 4)
   - Concepts: Object-Oriented Programming (OOP), class variables, instance variables,
     dunder methods (__init__, __str__, __len__), and Object Composition.
   - Object Composition Explanation:
     Object composition is a design principle where composite objects are built by
     containing simpler component objects (a "has-a" relationship instead of "is-a").
     Here, Playlist "has-a" collection of MediaItem objects. The Playlist delegates
     formatting to MediaItem.__str__(), while coordinating multi-item behaviors
     such as total duration calculation and top-rated item querying.
   - Expected Output:
       Playlist: Daily Mix (Size: 3)
       Total Duration: 1620s
       Top Rated Item: Track 2
        -  Track 1 by Artist A [Song] - 180s (Rating: 4.5)
        -  Track 2 by Artist B [Song] - 240s (Rating: 4.9)
        -  Episode 1 by Host C [Podcast] - 1200s (Rating: 4.2)

--------------------------------------------------------------------------------

4. Milestone 4 - Modularize Playlist Analytics with Functions
   - Files: Q4_Milestone4/media_utils.py, Q4_Milestone4/main.py
   - Course Outcome: CO4 (Bloom's Level: 4)
   - Concepts: Modular programming (custom module import), reusable helper functions,
     default parameter arguments, lambda expressions for sorting, first-class
     functions dispatched via dictionary key mappings, and execution benchmarking
     using the standard `time` module.
   - Key Functions:
     * media_utils.seconds_to_hms(seconds): Converts seconds to 'Xh Ym Zs'
     * media_utils.filter_by_rating(items, min_rating=4.0): Filters high-rated media
     * media_utils.summarize_by_type(items): Counts items per media type
   - Expected Output:
       Filtered (Rating >= 4.0): ['Song B', 'Podcast X']
       Summary by Type: {'Song': 2, 'Podcast': 1}
       Formatted Total Time: 1h 6m 30s
       Analytics Generated in: <time in seconds>s

--------------------------------------------------------------------------------

5. Milestone 5 - Maintain Listening History and Handle Bad Data
   - Files: Q5_Milestone5.py, listening_history.txt
   - Course Outcome: CO5 (Bloom's Level: 5)
   - Concepts: Persistent file I/O (writing and reading pipe-delimited text data),
     file pointer positioning using `tell()`, robust structured exception handling
     (FileNotFoundError, ValueError), and fault-tolerant parsing.
   - Delimiter: '|'
   - Test Malformed Record:
       "Unknown Episode|Podcast|abc|6"
   - Debugging Note:
       Fault: The string 'abc' cannot be converted to an integer for duration
       (raising ValueError: invalid literal for int() with base 10: 'abc'), and
       the rating 6 is outside the valid 1 to 5 range.
       Correction: An inner try-except block encapsulates each line's parsing.
       When an invalid record is identified, an error is logged and the loop
       continues gracefully to process subsequent lines without crashing.
   - Expected Output:
       Initial file position: 0
       [LOG ERROR] Skipping malformed record 'Unknown Episode|Podcast|abc|6': invalid literal for int() with base 10: 'abc'
       Successfully Loaded 2 Records:
        -  ('Track 1', 'Song', 180, 4.5)
        -  ('Track 2', 'Song', 240, 4.9)

================================================================================
HOW TO RUN THE PROGRAMS
================================================================================
Navigate to the Assignment5 directory or project root in your terminal:

1. Run Milestone 1:
   python Assignment5/Q1_Milestone1.py

2. Run Milestone 2:
   python Assignment5/Q2_Milestone2.py

3. Run Milestone 3:
   python Assignment5/Q3_Milestone3.py

4. Run Milestone 4:
   cd Assignment5/Q4_Milestone4
   python main.py
   cd ../..

5. Run Milestone 5:
   python Assignment5/Q5_Milestone5.py

================================================================================
REQUIREMENTS & ENVIRONMENT
================================================================================
- Python 3.8+ (Standard Library only; no third-party dependencies required)
- Operating System: Cross-platform (Windows, Linux, macOS)
================================================================================

