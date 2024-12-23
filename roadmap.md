# Project: Local Website for Music, Dinner, and Mood Sharing

## Objective
Create a locally hosted website that allows you and your girlfriend to:
1. See what music each other is playing.
2. Pick dinner options interactively.
3. Share feelings with cute icons and styling.


---

## Milestones and Tasks

### 1. Setting Up the Local Environment
- Install a web server on your Raspberry Pi (e.g., Apache, Nginx, or use Python's `http.server` for simplicity).
- Configure the Raspberry Pi to host the website locally.
- Test with a basic "Hello World" webpage.

### 2. Music Sharing Feature
- **Option 1:** Integrate APIs like Spotify or Last.fm for real-time music data.
  - Create developer accounts on Spotify/Last.fm.
  - Obtain API keys and set up authentication.
  - Fetch and display the currently playing track using the API.
- **Option 2:** Manual Song Input
  - Build a simple form where each of you can enter the song name and artist.
  - Display the latest input on the homepage.

### 3. Dinner Selection Feature
- Create a list or dropdown menu with dinner options.
- Add a "Submit" button to lock in the selection.
- Display the selected dinner option on the homepage.
- Optional: Add randomization with a "Surprise Me" button for fun.

### 4. Mood Tracker Feature
- Design cute mood icons (e.g., happy, tired, excited).
- Use buttons or clickable icons to select a mood.
- Update the homepage with the selected mood and a brief message.

### 5. User Interface and Styling
- Use HTML and CSS to design a clean, playful interface.
- Pick a color palette (soft pastels or warm tones).
- Add animations using CSS or JavaScript for interactivity (e.g., hover effects, smooth transitions).
- Include custom illustrations or icons to personalize the site.

### 6. Backend Integration (Optional)
- Use Flask or Django (Python) or Node.js for handling data.
- Save data (music, dinner, mood) in a JSON file or SQLite database.
- Make the site dynamic by fetching and updating data from the backend.

### 7. Deployment and Testing
- Host the site on the Raspberry Pi and test on multiple devices (phones, laptops, etc.).
- Collect feedback from your girlfriend on usability and design.
- Iterate and refine features based on feedback.

---

## Timeline
- **Week 1:** Set up the local server and design the homepage layout.
- **Week 2:** Implement the music-sharing and dinner selection features.
- **Week 3:** Add the mood tracker feature and polish the styling.
- **Week 4:** Test the site, gather feedback, and finalize.

---

## Tools and Resources
- **Frontend:** HTML, CSS, JavaScript (React.js for dynamic components if needed).
- **Backend (Optional):** Python (Flask/Django) or Node.js.
- **API Integration:** Spotify API or Last.fm API.
- **Database:** JSON file or SQLite.
- **Hosting:** Raspberry Pi.

---

## Stretch Goals
- Add a chat/messaging feature for fun communication.
- Incorporate a calendar for planning weekly dinners.
- Use voice commands for music and dinner selection.
- Allow uploading custom icons for mood tracking.
"""