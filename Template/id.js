function id_return() {
    var e = document.getElementById("brand");
    var strUser = e.value;
    console.log("Mene lazim olan", strUser);
    return e;
}

function generator() {
    var select = document.getElementById("model");
    var options = ["1", "2", "3", "4", "5"];

    for (var i = 0; i < options.length; i++) {
        var opt = options[i];
        var el = document.createElement("option");
        el.textContent = opt;
        el.value = opt;
        select.appendChild(el);
    }
}