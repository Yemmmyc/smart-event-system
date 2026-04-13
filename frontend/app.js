async function loadData() {
  const res = await fetch("http://localhost:8080/crowd");
  const data = await res.json();

  document.getElementById("data").innerText =
    JSON.stringify(data, null, 2);
}

loadData();
setInterval(loadData, 5000);