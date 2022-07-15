const searchFormSubmit = document.querySelector("#search-form");

function setSearchAction(event){
    event.preventDefault();
    const toggleId = document.querySelector(".toggle__now").id;
    let url;
    if (toggleId == "toggle-0") {
        url = "{% url 'sales:list' %}?form=apart";
    } else {
        url = "{% url 'sales:list' %}?form=etc";
    }
    return url;

}
searchFormSubmit.addEventListener("submit", setSearchAction);