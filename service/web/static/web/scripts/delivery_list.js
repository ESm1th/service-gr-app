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
            let delivery = xhr.responseText;
            if (xhr.status == 201) {
                
                let delivery_rows = document.getElementsByClassName('deliveries-row');
                let last_row = delivery_rows[delivery_rows.length - 1]
                
                if (last_row.length < 4) {
                    last_row.appendChild(delivery);
                } else {
                    let new_delivery_row = document.createElement('div');
                    new_delivery_row.className = 'deliveries-row d-flex w-100';
                    new_delivery_row.innerHTML = delivery;
                    document.getElementsByClassName('deliveries')[0].appendChild(new_delivery_row);
                };

            } else {
                // to do: error processing
            }
        };
        xhr.send(json_data);
    }
});

