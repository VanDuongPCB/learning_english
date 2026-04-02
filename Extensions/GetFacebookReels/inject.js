console.log("Inject.js đã sẵn sàng trên trang này!");

chrome.runtime.onMessage.addListener((message, sender, sendResponse) => {
    if (message.action === "DetectLinks") {
        const links = Array.from(document.querySelectorAll('a'))
                       .map(a => a.href.split('/?')[0])
                       .filter(href => href.includes('/reel/'));
        let owner = 'Unknown Owner';

        for (const span of document.querySelectorAll('span')) {
            if (span.textContent.includes('Thước phim của ')) {
                owner = span.textContent.replace('Thước phim của ', '').trim();
                break;
            }
        }

        sendResponse({ owner: owner, links: links});
    }

    return true;
});