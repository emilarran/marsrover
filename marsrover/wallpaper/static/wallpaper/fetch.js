fetch('http://localhost:8000/wallpaper/get-image/')
    .then(
        function(response) {
            if (response.status !== 200) {
                console.log('Looks like there was a problem. Status Code: ' +
                    response.status);
                alert('Looks like there was a problem. Status Code: ' +
                    response.status);
                return;
            }
            // Examine the text in the response
            response.json().then(function(data) {
                console.log(data);
                console.log(data['img_src']);
                document.getElementById('bod').style.backgroundImage = "url("+data['img_src']+")";
            });
        }
    )
    .catch(function(err) {
        console.log('Fetch Error :-S', err);
    }
);
