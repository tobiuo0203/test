
window.onload = function() {

    //alert("start2")
    
    axios.get('/static/data.json')
    .then(function (response) {
        // handle success
        id=document.getElementById('id');
        //id.textContent = JSON.stringify(response.data) 
        // line chart data
         var buyerData = {
            labels : response.data.datetime,
            datasets : [
            {
                fillColor : "rgba(172,194,132,0.4)",
                strokeColor : "#ACC26D",
                pointColor : "#fff",
                pointStrokeColor : "#9DB86D",
                data : response.data.data
    //[381300,447600,366900,337473,301090,268199,247542,278100,281100,310500,324000,293100,260700,261300,275100,224400,268200,291900,246300,223800,232200,245700,243900,229800,257700,253800,211200,205800,206100,218700,187800,196200,194400,159000,184200,162000,169200,177900,173100,169500,193200,162900,162900,171300,171900,169200,197700,204600,]
            }
        ]
        }
        // get line chart canvas
        var buyers = document.getElementById('buyers').getContext('2d');
        // draw line chart
        new Chart(buyers).Line(buyerData);
    
    })
    .catch(function (error) {
        // handle error
     alert(error);
    })
    .finally(function () {
        // always executed
    });
    };
    