// Insert your API key here
const API_KEY = "AIzaSyAi0maGeBp6sTbtp5ED3gqo9ZUGuh-Caes";

// Download JSON file by fileId
async function driveDownloadJSON(fileId) {
    const url = `https://www.googleapis.com/drive/v3/files/${fileId}?alt=media&key=${API_KEY}`;
    const res = await fetch(url);
    return await res.text();
}

// Download binary file
async function driveDownloadFile(fileId) {
    const url = `https://www.googleapis.com/drive/v3/files/${fileId}?alt=media&key=${API_KEY}`;
    const res = await fetch(url);
    const blob = await res.blob();
    return blob;
}