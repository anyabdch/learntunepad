function populatePage(o){
    const on = document.getElementsByClassName("is-active");
    on[0].classList.toggle("is-active");
    o.classList.toggle("is-active");
    let content = o.getAttribute("content");
    let page = document.getElementById("side-offset");
    if (content) {
        document.getElementById("head").innerHTML = o.getAttribute("title");
        page.innerHTML = content;
        }
    else {
        let project = o.getAttribute("name");
        $('#side-offset').load("/e/"+project+" #embeddedProject");
    }
}

function autoScroll(o){
    o.scrollIntoView(true);
}

function toggleHide(o){
    let obj = document.getElementById(o);
    obj.classList.toggle("hidden");
    if (obj.classList.contains("msg")){
        let scroll = document.getElementsByTagName('body')[0];
        if (!obj.classList.contains("hidden")){
            scroll.style.overflowY = "hidden";
        }
        else {
            scroll.style.overflowY = "auto";
        }
    }
}

function printProject(){
    window.frames["toPrint"].focus();
    window.frames["toPrint"].print();
}

function printContent(){
    $('#proj').get(0).contentWindow.print();
}