async function loadData() {
    try {
        const crowdRes = await fetch("http://localhost:8080/crowd");
        const crowd = await crowdRes.json();

        const alertRes = await fetch("http://localhost:8080/alerts");
        const alerts = await alertRes.json();

        // Crowd display (formatted)
        document.getElementById("crowd").innerText =
            Object.entries(crowd)
                .map(([key, value]) => `${key}: ${value}`)
                .join("\n");

        // Alerts display
        document.getElementById("alerts").innerText =
            alerts.message || "No active alerts";

    } catch (error) {
        document.getElementById("alerts").innerText =
            "⚠ Backend not reachable";
    }
}

loadData();
setInterval(loadData, 3000);