document.addEventListener('DOMContentLoaded', () => {
    document.getElementById('btn-detect-links').addEventListener('click', () => {
        detectLinks();
    });

    document.getElementById('btn-upload-links').addEventListener('click', () => {
        uploadLinks();
    });

    let tabs = document.querySelectorAll('.tab-item');
    tabs.forEach(tab => {
        tab.addEventListener('click', () => {
            switchTab(tab.id);
        });
    });
});

function switchTab(tabId) {
    const tabs = document.querySelectorAll('.tab-item');
    tabs.forEach(tab => {
         tab.classList.remove('active');
        if (tab.id === tabId) {
            tab.classList.add('active');
        }
    });

    let paneName = tabId.replace('tab-', 'pane-');
    const panes = document.querySelectorAll('.pane');
    panes.forEach(pane => {
        pane.classList.remove('active');
        if (pane.id === paneName) {
            pane.classList.add('active');
        }
    });
}

async function detectLinks() {
    const [tab_focused] = await chrome.tabs.query({ active: true, currentWindow: true });
    if (!tab_focused) {
        return;
    }

    chrome.tabs.sendMessage(tab_focused.id, {action: "DetectLinks"}, (response) => {
        if (chrome.runtime.lastError) {
            alert("Error sending message to content script:", chrome.runtime.lastError);
            return;
        }

        if (response && response.links) {
            const owner = response.owner || "Unknown Owner";
            document.getElementById('owner-name').value = owner;
            const links = response.links;
            document.getElementById('links-output').textContent = links.join('\n');
        } 
        else {
            document.getElementById('links-output').textContent = "No links found or error in response.";
        }
    });
}

async function uploadLinks() {
    const linksText = document.getElementById('links-output').textContent;
    const links = linksText.split('\n').filter(link => link.trim() !== '');
    if (links.length === 0) {
        alert("No links to upload!");
        return;
    }

    alert("Uploading " + links.length + " links...");
};