document.getElementById('encodeBtn').addEventListener('click', () => processText('encode'));
document.getElementById('decodeBtn').addEventListener('click', () => processText('decode'));

function processText(action) {
    const text = document.getElementById('inputText').value;
    const cipher = document.getElementById('cipherSelect').value;
    const key = document.getElementById('key').value || (cipher === 'caesar' ? '3' : 'KEY'); // Default values

    fetch(`/${cipher}/${action}`, {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({ text, key })
    })
    .then(response => response.json())
    .then(data => {
        document.getElementById('outputText').value = data.result;
    });
}
