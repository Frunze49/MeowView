// document.getElementById('fileInput').addEventListener('change', function(event) {
//     const file = event.target.files[0];
//     if (file) {
//         const reader = new FileReader();
//         reader.onload = function(e) {
//             const byteArray = new Uint8Array(e.target.result);
//             const blob = new Blob([byteArray], { type: 'image/png' });
//             const url = URL.createObjectURL(blob);
//             document.getElementById('image').src = url;
//         };
//         reader.readAsArrayBuffer(file);
//     }
// });
