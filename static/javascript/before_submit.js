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
function inputOnlyNumber(event){
    if(event.key === '.' 
     || event.key === '-'
     || event.key >= 0 && event.key <= 9) {
    return true;
  }
  return false;
}

searchFormSubmit.addEventListener("submit", setSearchAction);
