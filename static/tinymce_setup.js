function djangoFilePicker(callback, value, meta) {
    if (meta.filetype === 'image') {
        const input = document.createElement('input');
        input.setAttribute('type', 'file');
        input.setAttribute('accept', 'image/*');
        input.onchange = function() {
            const file = this.files[0];
            const reader = new FileReader();
            reader.onload = function() {
                const formData = new FormData();
                formData.append('file', file);

                fetch('/upload/', {
                    method: 'POST',
                    body: formData,
                })
                .then(response => response.json())
                .then(result => {
                    callback(result.location, {
                        alt: file.name,
                    });
                })
                .catch(error => {
                    console.error('Error:', error);
                });
            };
            reader.readAsDataURL(file);
        };
        input.click();
    }
}
