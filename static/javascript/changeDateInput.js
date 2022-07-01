const dateFromInput = document.querySelector("#date_from");
const dateToInput = document.querySelector("#date_to");

function changeDateTo(){
    const dateTo = document.querySelector("#date_to").value;
    dateFromInput.max = dateTo;
}

function changeDateFrom(){
    const dateFrom = document.querySelector("#date_from").value;
    dateToInput.min = dateFrom;
}

dateFromInput.addEventListener("change", changeDateFrom);
dateToInput.addEventListener("change", changeDateTo);