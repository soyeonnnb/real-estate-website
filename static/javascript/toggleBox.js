const toggleBoxBtn = document.querySelectorAll(".manage-toggle-box");

function removeToggleNow(){
    const previousToggleNow = document.querySelector(".manage-toggle__now");
    previousToggleNow.classList.remove("manage-toggle__now");
    if (previousToggleNow.id == "manage-toggle-complex"){
        document.querySelector("#manage-list-complex").classList.remove("manage-toggle-show");
        document.querySelector("#manage-list-complex").className += " manage-toggle-noshow";
    } else if (previousToggleNow.id == "manage-toggle-sale"){
        document.querySelector("#manage-list-sale").classList.remove("manage-toggle-show");
        document.querySelector("#manage-list-sale").className += " manage-toggle-noshow";
    } else{
        document.querySelector("#manage-list-question").classList.remove("manage-toggle-show");
        document.querySelector("#manage-list-question").className += " manage-toggle-noshow";
    }
}

function toggle(){
    removeToggleNow();
    const currentToggleNow = event.currentTarget;
    currentToggleNow.className += " manage-toggle__now";
    if (currentToggleNow.id == "manage-toggle-complex"){
        document.querySelector("#manage-list-complex").classList.remove("manage-toggle-noshow");
        document.querySelector("#manage-list-complex").className += " manage-toggle-show";
    } else if (currentToggleNow.id == "manage-toggle-sale"){
        document.querySelector("#manage-list-sale").classList.remove("manage-toggle-noshow");
        document.querySelector("#manage-list-sale").className += " manage-toggle-show";
    } else{
        document.querySelector("#manage-list-question").classList.remove("manage-toggle-noshow");
        document.querySelector("#manage-list-question").className += " manage-toggle-show";
    }
}

[].forEach.call(toggleBoxBtn,function(btn){ 
	btn.addEventListener("click", toggle); 
});