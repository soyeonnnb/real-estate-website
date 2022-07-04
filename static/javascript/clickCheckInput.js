const form = document.querySelector("#search_sale_form");

const typeAllBtn = document.querySelector("#type_all");
const typeNotAllBtn =  document.querySelectorAll(".search-type-btn");

const addressAllBtn = document.querySelector("#address_all")
const addressNotAllBtn = document.querySelectorAll(".search-address-btn")



function clickAll(allBtn, notAllBtn){
    if (allBtn.classList.contains("search_all_checked")){
        allBtn.classList.remove("search_all_checked");
        allBtn.classList.add("search_all_notchecked");
        for (i=0;i<notAllBtn.length;i++){
            notAllBtn[i].checked=false;
        }
    } else {
        allBtn.classList.remove("search_all_notchecked");
        allBtn.classList.add("search_all_checked");
        for (i=0;i<notAllBtn.length;i++){
            notAllBtn[i].checked=true;
        }
    }
}

function clickNotAll(allBtn) {
    if (allBtn.classList.contains("search_all_checked")){
        allBtn.classList.remove("search_all_checked"); 
        allBtn.classList.add("search_all_notchecked");
    }
}


typeAllBtn.addEventListener("click", function() {clickAll(typeAllBtn, typeNotAllBtn);});
[].forEach.call(typeNotAllBtn,function(btn){ 
	btn.addEventListener("click", function() {clickNotAll(typeAllBtn);}); 
});
addressAllBtn.addEventListener("click", function() {clickAll(addressAllBtn, addressNotAllBtn);});
[].forEach.call(addressNotAllBtn,function(btn){ 
	btn.addEventListener("click", function() {clickNotAll(addressAllBtn);}); 
});