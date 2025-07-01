document.getElementById('inputSubmit').addEventListener('click', function (e) {
    e.preventDefault();
    const csrfToken = document.querySelector('[name=csrfmiddlewaretoken]').value;

    const data = new URLSearchParams({
        name: document.getElementById('Full-Name').value,
        username: document.getElementById('username').value,
        business_name: document.getElementById('business-name').value,
        directors_name: document.getElementById('director-name').value,
        rc_number: document.getElementById('rc-number').value,
        tin: document.getElementById('tin').value,
        date_of_incorporation: document.getElementById('date-of-inc').value,
        phone_number: document.getElementById('phone-number').value,
        NIN: document.getElementById('NIN').value,
        email: document.getElementById('email-address').value,
        business_address: document.getElementById('Business-address').value,
        state: document.getElementById('state').value,
        city_lga: document.getElementById('city-lga').value
    });

    fetch('/dashboard/manage-account/', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/x-www-form-urlencoded',
            'X-CSRFToken': csrfToken
        },
        body: data.toString()
    })
    .then(response => response.json())
    .then(responseData => {
        if (responseData.redirect_url) {
            alert('Account details successfully updated! Redirecting to login page...');
            window.location.href = responseData.redirect_url;  // ✅ Redirect to login page
        }
    })
    .catch(err => console.error(err));
});







