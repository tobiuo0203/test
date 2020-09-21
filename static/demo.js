//alert("start")

window.onload = function() {

//alert("start2")

axios.get('/home/tobiuo0203/static/data.json')
.then(function (response) {
    // handle success
    id=document.getElementById('id');
    id.textContent = JSON.stringify(response.data) 
})
.catch(function (error) {
    // handle error
 alert(error);
})
.finally(function () {
    // always executed
});
};