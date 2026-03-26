document.getElementById("summarizeBtn").addEventListener("click", async () => {
console.log("Button clicked"); 
    const [tab] = await chrome.tabs.query({ active: true, currentWindow: true });

    const url = tab.url;

    document.getElementById("output").innerText = "Loading summary...";

    try {
        const response = await fetch(
            `http://127.0.0.1:5000/summary?url=${encodeURIComponent(url)}`
        );

        const data = await response.json();

        if (data.error) {
            document.getElementById("output").innerText = data.error;
        } else {
            document.getElementById("output").innerText = data.summary;
        }

    } catch (error) {
        document.getElementById("output").innerText = "Error connecting to backend";
    }

});
