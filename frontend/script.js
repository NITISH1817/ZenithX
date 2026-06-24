async function searchScreenshot() {

    const query =
        document.getElementById("query").value;

    const response =
        await fetch(
            `http://127.0.0.1:8000/search?query=${query}`
        );

    const data = await response.json();

    document.getElementById("result").innerHTML =
        `
        <h3>Result</h3>
        <p>${data.result}</p>
        <p>Score: ${data.score}</p>
        `;
}