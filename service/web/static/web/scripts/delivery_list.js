document.addEventListener('DOMContentLoaded', function() {

    var create_delivery_btn = document.getElementById('create_delivery_btn');
    create_delivery_btn.addEventListener('click', createDelivery);

    function createDelivery(event) {
        /*
        * Create delivery by ajax request to rest api and add new delivery card.
        */
        let path = event.target.getAttribute('data-url');
        let form_data = new FormData(document.getElementById('create_delivery_form'));
        let data = {};

        form_data.forEach((value, key) => {data[key] = value});
        let json_data = JSON.stringify(data);
        
        let xhr = new XMLHttpRequest();
        xhr.open('POST', window.location.origin + path + '?format=html');
        xhr.setRequestHeader('Content-Type', 'application/json');
        xhr.setRequestHeader('X-CSRFToken', document.getElementsByName('csrfmiddlewaretoken')[0].value);
        xhr.onload = function () {
            if (xhr.status == 201) {
                let deliveries = document.getElementsByClassName('deliveries')[0];
                let div = document.createElement('div');
                div.innerHTML = xhr.responseText.trim();
                deliveries.appendChild(div.firstChild);
            } else {
                // to do: error processing
            }
        };
        xhr.send(json_data);
    }
});

