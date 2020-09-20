alert("start")

window.onload = function() {

alert("start2")

axios.get('static/data.json')
.then(function (response) {
    // handle success
 alert(response);
})
.catch(function (error) {
    // handle error
 alert(error);
})
.finally(function () {
    // always executed
});
};