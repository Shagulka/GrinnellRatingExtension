# Grinnell Rating Extension

### I created this extension just to refresh mu coding skills and to learn how to create a chrome extension. But I would be happy if someone finds it useful.

<div style="color: dodgerblue; font-weight: bold; border: 1px solid dodgerblue; padding: 10px; border-radius: 5px; margin-bottom: 15px;">
I strongly believe that professor ratings should not be the sole factor in determining the quality of a course or instructor. I encourage students to use this tool as a supplement to other resources and to consider the limitations of such ratings. Please be respectful and considerate when using this tool.
</div>

<div style="color: red; font-weight: bold; border: 1px solid red; padding: 10px; border-radius: 5px; margin-bottom: 15px;">
Note: I do not promote the use of this extension without understanding the implications of using it. This extension is not officially endorsed by Grinnell College. Use at your own risk. Database may contain errors or outdated information.
</div>

## Description

Grinnell Rating Extension is a Chrome extension that allows students to view instructor ratings and reviews directly on
the <a href="https://colss-prod.ec.grinnell.edu/Student/Courses/">Grinnell College Student Portal</a> website.
The extension displays ratings and reviews from the Rate My Professor
website, providing students with additional information to make informed decisions when selecting courses and
instructors.

## Installation

##### Download the extension from the <a href="chrome://extensions/">Chrome Web Store</a>. (DOESN'T WORK NOW)

##### Alternatively, you can download the source code and load the extension manually by following the instructions below.

- Clone the repository or download the source code as a ZIP file.
- Extract the ZIP file (if downloaded).
- Open Chrome and navigate to `chrome://extensions/`.
- Enable Developer mode by toggling the switch in the top right corner.
- Click on the `Load unpacked` button and select the extracted folder.
- The extension should now be installed and ready to use.

## Screenshots

<div style="display: flex; justify-content: space-around; align-items: center; margin-bottom: 15px;">
  <div style="text-align: center;">
    <img src="screenshots/without_extension.png" width="400" alt="without extension">
    <div style="margin-top: 10px; font-weight: bold;">Without Extension</div>
  </div>
  <div style="text-align: center;">
    <img src="screenshots/with_extension.png" width="400" alt="with extension">
    <div style="margin-top: 10px; font-weight: bold;">With Extension</div>
  </div>
</div>

## Database

This extension has a static database of instructors and ratings that are not updated in real-time. The database is based
on the Rate My Professor website and may contain errors or outdated information. Below are the instructions to update
the database manually.

##### Update the database by following these steps:

- Open the `DatabaseUpdater.py` file in the `Database` folder.
- Run the script to update the database.
- The script will scrape the Rate My Professor website and update the database.
- Database requires manual moderation to ensure accuracy and reliability.
- The updated database will be saved as a JSON file in the `Database` folder.


