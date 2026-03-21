let currentStorefront = "Home Storefront";
let homeId = "1m99FhKG-zpNd7VoAOjFV11dyJsDbnUv9";
let currentId = homeId;

const titleEl = document.getElementById("storefront-title");
const menuEl = document.getElementById("menu");
const homeBtn = document.getElementById("home-btn");
const statusEl = document.getElementById("status");

async function loadStorefront(id) {
    statusEl.textContent = "Loading…";

    const json = await driveDownloadJSON(id);
    const menu = JSON.parse(json);

    renderMenu(menu);
    statusEl.textContent = "";
}

function renderMenu(menu) {
    titleEl.textContent = currentStorefront;
    menuEl.innerHTML = "";

    homeBtn.style.display = currentStorefront !== "Home Storefront" ? "block" : "none";

    Object.keys(menu).forEach((key, index) => {
        const li = document.createElement("li");
        li.textContent = key;
        li.onclick = () => handleSelection(menu[key], key);
        menuEl.appendChild(li);
    });
}

async function handleSelection(item, name) {
    const [id, type, path] = item;

    if (type === "storefront") {
        currentId = id;
        currentStorefront = name;
        loadStorefront(id);
    } else {
        statusEl.textContent = "Downloading…";

        const fileBlob = await driveDownloadFile(id);
        const filename = item[1];

        const url = URL.createObjectURL(fileBlob);
        const a = document.createElement("a");
        a.href = url;
        a.download = filename;
        a.click();

        statusEl.textContent = "Download complete.";
    }
}

homeBtn.onclick = () => {
    currentId = homeId;
    currentStorefront = "Home Storefront";
    loadStorefront(homeId);
};

loadStorefront(currentId);