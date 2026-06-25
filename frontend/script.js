async function searchScreenshot() {
    try {
        // Get the user's search query
        const query = document.getElementById("query").value;

        // Check if query is empty
        if (query.trim() === "") {
            document.getElementById("result").innerHTML =
                "<p style='color:red;'>Please enter a search query.</p>";
            return;
        }

        // Send request to FastAPI backend
        const response = await fetch(
            `https://super-acorn-69w9vj4596rqc5qvx-8000.app.github.dev/search?query=${encodeURIComponent(query)}`
        );

        if (!response.ok) {
            throw new Error("Failed to fetch data from backend");
        }

        // Convert response to JSON
        const data = await response.json();

        // Display result
        document.getElementById("result").innerHTML = `
            <h2>Best Match</h2>

            <p><strong>Text:</strong> ${data.text}</p>

            <img
                src="https://super-acorn-69w9vj4596rqc5qvx-8000.app.github.dev/dataset/${data.image}"
                alt="Matched Screenshot"
                width="400"
                style="border:1px solid #ccc;border-radius:8px;margin-top:10px;"
            >

            <p><strong>Score:</strong> ${data.score}</p>
        `;

    } catch (error) {
        console.error(error);

        document.getElementById("result").innerHTML = `
            <p style="color:red;">
                Error: ${error.message}
            </p>
        `;
    }
}