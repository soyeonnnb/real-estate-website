const toggleBoxBtns = document.querySelectorAll(".toggle-box");

function removeToggleNow(){
    const previousToggleNow = document.querySelector(".toggle__now");
    previousToggleNow.classList.remove("toggle__now");
    for(i=0;i<toggleBoxBtns.length;i++){
        if (previousToggleNow.id == `toggle-${i}`){
            document.querySelector(`#list-${i}`).classList.remove("toggle-show");
            document.querySelector(`#list-${i}`).className += " toggle-noshow";
            continue;
        }
    }
}

function toggle(){
    removeToggleNow();
    const currentToggleNow = event.currentTarget;
    currentToggleNow.className += " toggle__now";
    for(i=0;i<toggleBoxBtns.length;i++){
        if (currentToggleNow.id == `toggle-${i}`){
            document.querySelector(`#list-${i}`).classList.remove("toggle-noshow");
            document.querySelector(`#list-${i}`).className += " toggle-show";
            continue;
        }
    }
}

[].forEach.call(toggleBoxBtns,function(btn){ 
	btn.addEventListener("click", toggle); 
})