let searchCounter = 0;
const API_URL = "https://super-acorn-69w9vj4596rqc5qvx-8000.app.github.dev";


async function searchScreenshot() {


    const query = document.getElementById("query").value.trim();
    const resultDiv = document.getElementById("result");
    searchCounter++;

const counter = document.getElementById("searchCount");

if (counter) {
    counter.innerText = searchCounter;
}

    if (query === "") {

        resultDiv.innerHTML = `
            <div class="result-card">
                <h2>⚠️ Please enter a search query</h2>
            </div>
        `;
        return;
    }

    resultDiv.innerHTML = `
        <div class="result-card">
            <h2>🔍 Searching...</h2>
        </div>
    `;

    try {

        const response = await fetch(
            `${API_URL}/search?query=${encodeURIComponent(query)}`
        );

        if (!response.ok) {
            throw new Error("Server Error");
        }

        const data = await response.json();

        if (!data.found) {

            resultDiv.innerHTML = `
                <div class="result-card">
                    <h2>❌ No Matching Screenshot Found</h2>
                    <p>${data.message}</p>
                </div>
            `;
            return;
        }

        const imageUrl =
            `${API_URL}/dataset/${data.image}?t=${Date.now()}`;

        resultDiv.innerHTML = `
            <div class="result-card">

                <h2>✨ Best Match Found</h2>

                <img
                    src="${imageUrl}"
                    alt="Matched Screenshot"
                >

                <div class="score">
                    ⭐ Similarity Score:
                    <strong>${data.score}</strong>
                </div>

            </div>
        `;

    } catch (error) {

        console.error(error);

        resultDiv.innerHTML = `
            <div class="result-card">
                <h2>⚠️ Connection Error</h2>
                <p>Unable to connect to the backend.</p>
            </div>
        `;
    }
}

/* Search when Enter is pressed */

document
    .getElementById("query")
    .addEventListener("keypress", function (event) {

        if (event.key === "Enter") {
            searchScreenshot();
        }

    });

/* Smooth fade-in animation on page load */

window.addEventListener("load", () => {

    document.querySelector(".glass-card").style.opacity = "0";
    document.querySelector(".glass-card").style.transform = "translateY(40px)";

    setTimeout(() => {
        document.querySelector(".glass-card").style.transition = "all .8s ease";
        document.querySelector(".glass-card").style.opacity = "1";
        document.querySelector(".glass-card").style.transform = "translateY(0)";
    }, 100);

});