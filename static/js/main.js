document.addEventListener('DOMContentLoaded', function() {
    // Music form submission
    document.querySelectorAll('.music-form').forEach(form => {
        form.addEventListener('submit', async (e) => {
            e.preventDefault();
            const formData = new FormData(form);
            
            try {
                const response = await fetch('/update/music', {
                    method: 'POST',
                    body: formData
                });
                const data = await response.json();
                if (data.status === 'success') {
                    form.reset();
                }
            } catch (error) {
                console.error('Error:', error);
            }
        });
    });

    // Dinner form submission
    document.getElementById('dinnerForm').addEventListener('submit', async (e) => {
        e.preventDefault();
        const formData = new FormData(e.target);
        
        try {
            const response = await fetch('/update/dinner', {
                method: 'POST',
                body: formData
            });
            const data = await response.json();
            if (data.status === 'success') {
                e.target.reset();
            }
        } catch (error) {
            console.error('Error:', error);
        }
    });

    // Mood buttons
    document.querySelectorAll('.mood-buttons button').forEach(button => {
        button.addEventListener('click', async () => {
            const form = button.closest('form');
            const formData = new FormData();
            formData.append('user', form.querySelector('[name="user"]').value);
            formData.append('mood', button.dataset.mood);
            
            try {
                const response = await fetch('/update/mood', {
                    method: 'POST',
                    body: formData
                });
                const data = await response.json();
            } catch (error) {
                console.error('Error:', error);
            }
        });
    });
}); 