// Function to fetch the professor database
async function fetchDatabase() {
    try {
        const response = await fetch(chrome.runtime.getURL('Database/professors.json'));
        if (!response.ok) {
            console.error('Failed to load database:', response.status, response.statusText);
            return {};
        }
        const data = await response.json();
        console.log('Database loaded:', data); // Debugging statement
        return data;
    } catch (error) {
        console.error('Error fetching the database:', error);
        return {};
    }
}

// Function to format the value, replacing -1.0 with N/A
function formatValue(value) {
    return value === -1.0 ? 'N/A' : value;
}

// Function to replace span text
async function replaceSpanText() {
    const database = await fetchDatabase();

    console.log('Database:', database); // Debugging statement
    // Wait till the page is fully loaded
    await new Promise((resolve) => setTimeout(resolve, 2000));

    const spans = document.querySelectorAll('span[title="Show Office Hours"]:not(.updated)');
    console.log('Found spans:', spans.length); // Debugging statement

    spans.forEach((span) => {
        let professorName = span.textContent.trim();
        professorName = professorName.replace(/\s+/g, '+');
        console.log('Processing professor:', professorName); // Debugging statement

        let content;
        if (database[professorName]) {
            const professorData = database[professorName];
            content = `
                <p><strong>Name: </strong>${professorName.split('+').join(' ')}</p>
                <p><strong>Rating: </strong>${formatValue(professorData.rating)}</p>
                <p><strong>Number of ratings: </strong>${formatValue(professorData.num_ratings)}</p>
                <p><strong>Would take again: </strong>${formatValue(professorData.would_take_again)}%</p>
                <p><strong>Difficulty: </strong>${formatValue(professorData.difficulty)}</p>
                <p><a href="${professorData.link}" target="_blank">RMP Profile</a></p>`;
        } else {
            content = `<p>${professorName.split('+').join(' ')} (No data available)</p>`;
        }

        span.innerHTML = content;
        // Add a class to indicate that this span has been processed
        span.classList.add('updated');
    });
}

// Run the function initially after the document is fully loaded
document.addEventListener('DOMContentLoaded', () => {
    replaceSpanText();
});

// Create a mutation observer to handle dynamically loaded content
const observer = new MutationObserver((mutations) => {
    mutations.forEach((mutation) => {
        if (mutation.type === 'childList' || mutation.type === 'subtree') {
            replaceSpanText();
        }
    });
});

// Observe the document body for changes
observer.observe(document.body, {childList: true, subtree: true});
