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
            document.getElementById('links-output').value = links.join('\n');
        } 
        else {
            document.getElementById('links-output').value = "No links found or error in response.";
        }
    });
}

async function uploadLinks() {
    const linksText = document.getElementById('links-output').value.trim();
    const links = linksText.split('\n').filter(link => link.trim() !== '');
    if (links.length === 0) {
        alert("No links to upload!");
        return;
    }

    const owner = document.getElementById('owner-name').value.trim();
    if (owner === "") {
        alert("Please enter the owner's name!");
        return;
    }

    let classify = [];
    if (document.getElementById('include-read').checked) classify.push("Read");
    if (document.getElementById('include-listen').checked) classify.push("Listen");
    if (document.getElementById('include-grammar').checked) classify.push("Grammar");
    if (document.getElementById('include-vocabulary').checked) classify.push("Vocabulary");
    if (classify.length === 0) {
        alert("Please select at least one classification!");
        return;
    }

    const payload = {
        owner: owner,
        links: links,
        classify: classify.join(', ')
    };

    let url = 'https://script.google.com/macros/s/AKfycbzGFRFhLc3ePpXoVz8ZKFMQ6oRUHwmQ6j9AUzYzxQUt2oXBR6F0GcC1r8Sglz8tiTX2VQ/exec';
    fetch(url, {
        method: 'POST',
        mode: 'no-cors',
        headers: {
            'Content-Type': 'application/json'
        },
        body: JSON.stringify(payload)
    })
    .then(response => {
        console.log('POST request sent successfully');
        alert("Links uploaded successfully!");
    })
    .catch(error => console.error('Error:', error));
};