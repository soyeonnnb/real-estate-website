const dateFromInput = document.querySelector("#id_basic-date_from");
const dateToInput = document.querySelector("#id_basic-date_to");

const priceFromInput = document.querySelector("#id_basic-price_from");
const priceToInput = document.querySelector("#id_basic-price_to");

function changeFrom(type, toInput){
    const from_value = document.querySelector(`#id_${type}_from`).value;
    toInput.min = from_value;
}

function changeTo(type, FromInput){
    const to_value = document.querySelector(`#id_${type}_to`).value;
    FromInput.max = to_value;
}

dateFromInput.addEventListener("change", function() {changeFrom("date", dateToInput);});
dateToInput.addEventListener("change", function() {changeTo("date", dateFromInput);});
priceFromInput.addEventListener("change", function() {changeFrom("price", dateToInput);});
priceToInput.addEventListener("change", function() {changeTo("price", dateFromInput);});