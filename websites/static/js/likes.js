document.querySelectorAll('.like-button').forEach(button => {
    button.addEventListener('click', function (e) {
        e.preventDefault(); // Prevent form submission

        // Get the form and its action URL
        const form = this.closest('form');
        const url = form.action;

        // Fetch the CSRF token from the <meta> tag
        const csrfToken = document.querySelector('meta[name="csrf-token"]').getAttribute('content');

        // Send the AJAX POST request
        fetch('/like/1/', {
            method: 'POST',
            headers: {
                'X-CSRFToken': document.querySelector('meta[name="csrf-token"]').getAttribute('content'),
                'Content-Type': 'application/json',
            },
        })
        .then(response => response.json())
        .then(data => {
            if (data.likes !== undefined) {
                // Update like button text and count
                this.textContent = data.liked ? 'Unlike' : 'Like';
                form.querySelector('.likes-count').textContent = `${data.likes} likes`;
            } else {
                alert(data.error || 'Something went wrong.');
            }
        })
        .catch(error => console.error('Error:', error));
    });
});
