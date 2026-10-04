const btn = document.getElementById("loadBtn");
const resultsDiv = document.getElementById("results");

btn.addEventListener("click", loadData);

async function loadData() {
    try {
        const response = await fetch("http://127.0.0.1:8000/");

        if (!response.ok) {
            throw new Error("Failed to fetch data from backend");
        }

        const data = await response.json();
        displayData(data);
    } catch (error) {
        console.error("Error fetching data:", error);
        resultsDiv.innerHTML = "<p>Something went wrong fetching data.</p>";
    }
}

function displayData(data) {
    resultsDiv.innerHTML = ""; // Clear old results

    const card = document.createElement("div");
    card.className = "card";
    
    // Stringify converts the JSON object into readable text on screen
    card.innerHTML = `<p>${JSON.stringify(data)}</p>`;
    
    resultsDiv.appendChild(card);
}
let token = localStorage.getItem("token");
const statusEl = document.getElementById("status");n
document.getElementById("loginBtn").addEventListener("click", login);
document.getElementById("postsBtn").addEventListener("click", loadPosts);

async function login() {
    const body = new URLSearchParams({
        username: document.getElementById("email").value,
        password: document.getElementById("password").value,
    });

    const response = await fetch("http://127.0.0.1:8000/login", {
        method: "POST",
        body: body,
    });

    const data = await response.json();

    if (!response.ok) {
        statusEl.textContent = "Login failed";
        return;
    }

    token = data.access_token;
    localStorage.setItem("token", token);
    statusEl.textContent = "Logged in";
}

async function loadPosts() {
    const response = await fetch("http://127.0.0.1:8000/posts/", {
        headers: { Authorization: `Bearer ${token}` },
    });

    const data = await response.json();
    displayData(data);
}