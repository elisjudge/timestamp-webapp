function loadPage() {
    const body = document.querySelector('body');

    // Create Page Structure
    const h1 = document.createElement('h1');
    h1.innerText = "Timestamp Logger";

    const timestampContainer = document.createElement('div');
    timestampContainer.id = "timestampContainer";

    body.appendChild(h1);
    body.appendChild(timestampContainer);
}

async function loadTimestamps() {
    const response = await fetch('/timestamps');
    const timestamps = await response.json();

    const container = document.getElementById("timestampContainer");
    container.innerHTML = "";  // Clear previous content

    // Create a grid table with two columns
    const table = document.createElement("div");
    table.style.display = "grid";
    table.style.gridTemplateColumns = "1fr 1fr"; // Two columns: Date | Time
    table.style.gap = "5px"; // Spacing between rows

    // Header Row
    const headerDate = document.createElement("div");
    headerDate.textContent = "Date";
    headerDate.style.fontWeight = "bold";

    const headerTime = document.createElement("div");
    headerTime.textContent = "Time";
    headerTime.style.fontWeight = "bold";

    table.appendChild(headerDate);
    table.appendChild(headerTime);

    timestamps.forEach(ts => {
        const timestamp = new Date(ts);
        
        const dateDiv = document.createElement("div");
        dateDiv.textContent = timestamp.toLocaleDateString(); // Extract Date

        const timeDiv = document.createElement("div");
        timeDiv.textContent = timestamp.toLocaleTimeString(); // Extract Time

        table.appendChild(dateDiv);
        table.appendChild(timeDiv);
    });

    container.appendChild(table);
}

// Ensure the page is loaded before fetching timestamps
document.addEventListener("DOMContentLoaded", () => {
    loadPage();
    loadTimestamps();
});
