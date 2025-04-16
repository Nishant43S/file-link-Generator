// copy button
function copyText(event) {
    event.preventDefault();
    const text = document.getElementById("text").innerText;
    const textarea = document.createElement("textarea");
    textarea.value = text;
    document.body.appendChild(textarea);
    textarea.select();
    document.execCommand("copy");
    document.body.removeChild(textarea);
            
    const tooltip = document.getElementById("tooltip");
    tooltip.classList.add("show-tooltip");
    setTimeout(() => {
        tooltip.classList.remove("show-tooltip");
    }, 1000);
}

const fileInput = document.getElementById('fileInput');
const fileNameBox = document.getElementById('file-name-box');

fileInput.addEventListener('change', function () {
if (fileInput.files.length > 0) {
    fileNameBox.textContent = fileInput.files[0].name;
    fileNameBox.style.display = 'block';
} else {
    fileNameBox.style.display = 'none';
    fileNameBox.textContent = '';
}
});