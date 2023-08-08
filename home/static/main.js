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
        page.innerHTML = "<div id='foot' class='jc c2'>"+
                         "<button class='btn btn-danger' onclick='window.print()'>Print</button>"+
                         "<a href='https://tunepad.com/project/"+project+"'><button class='btn btn-success'>Start Activity</button></a>"+
                         "<a href='#'><button class='btn btn-info'>Share</button></a>"+
                         "</div>"+
                         "<div>" +
                         " <iframe id='toPrint' name='toPrint' src='https://tunepad.space/project/"+project+"?embedded=true' title='TunePad embedded project'></iframe>" +
                         "</div>";
    }
}

function autoScroll(o){
    o.scrollIntoView(true);
}

function hide(o){
    o.classList.toggle("hidden");
}

function printProject(){
    window.frames["toPrint"].focus();
    window.frames["toPrint"].print();
}