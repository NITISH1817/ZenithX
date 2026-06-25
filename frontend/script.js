async function searchScreenshot() {
    const query = document.getElementById("query").value.trim();

    if (query === "") {
        document.getElementById("result").innerHTML =
            "<p style='color:red;'>Please enter a search query.</p>";
        return;
    }

    try {
        const response = await fetch(
            `https://super-acorn-69w9vj4596rqc5qvx-8000.app.github.dev/search?query=${encodeURIComponent(query)}`
        );

        if (!response.ok) {
            throw new Error("Server Error");
        }

        const data = await response.json();

        // No match
        if (!data.found) {
            document.getElementById("result").innerHTML = `
                <h2>No Matching Screenshot Found</h2>
                <p>${data.message}</p>
            `;
            return;
        }

        // Match found
        const imageUrl =
            `https://super-acorn-69w9vj4596rqc5qvx-8000.app.github.dev/dataset/${data.image}?t=${Date.now()}`;

        document.getElementById("result").innerHTML = `
            <h2>Best Match</h2>

            <p><strong>OCR Text:</strong></p>
            <p>${data.text}</p>

            <img
                src="${imageUrl}"
                alt="Matched Screenshot"
                width="400"
                style="margin-top:15px;border:2px solid #444;border-radius:10px;"
                onerror="this.style.display='none';"
            >

            <p><strong>Similarity Score:</strong> ${data.score}</p>
        `;

    } catch (error) {
        console.error(error);

        document.getElementById("result").innerHTML = `
            <p style="color:red;">
                Error connecting to backend.
            </p>
        `;
    }
}