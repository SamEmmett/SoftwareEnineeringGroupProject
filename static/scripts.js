m 

//////////////////////////////////////////////////////////////////////////////////////////////////////
function setDoD() { //toggles the date box for DoD being required
        var checkboxs = document.getElementById("death");
        if (checkboxs.checked)
        {document.getElementById("DoD").setAttribute("required", true);
        }else{document.getElementById("DoD").removeAttribute("required", false);}
}
////////////////////////////////////////////////////////////////////////////////////////////////////////
function setOther1() { //toggles the text box for Other being required
    var checkboxs = document.getElementById("other")

        if (checkboxs.checked) //checks to see if other checkbox is checked
        {
            document.getElementById("otherText1").setAttribute("required", true);
        }else{document.getElementById("otherText1").removeAttribute("required", false);}
}

function setOther2() { //toggles the text box for Other being required
    var checkboxs = document.getElementById("Other2")
        if (checkboxs.checked) //checks to see if other checkbox is checked
        {
            document.getElementById("otherText2").setAttribute("required", true);
        }else{document.getElementById("otherText2").removeAttribute("required", false);}
}

function notifiedManu() { //toggles the text box for Other being required
    var checkboxs = document.getElementsByName("chkManu")
    for (var i = 0, l = checkboxs.length; i < l; i++) {
        if (checkboxs[i].checked) //checks to see if other checkbox is checked
        {
            document.getElementById("repManuName").setAttribute("required", true);
        }else{document.getElementById("repManuName").removeAttribute("required", false);}

    }
}

function notifiedFac() { //toggles the text box for Other being required
    var checkboxs = document.getElementsByName("chkRepFac")
    for (var i = 0, l = checkboxs.length; i < l; i++) {
        if (checkboxs[i].checked) //checks to see if other checkbox is checked
        {
            document.getElementById("repUserFac").setAttribute("required", true);
        }else{document.getElementById("repUserFac").removeAttribute("required", false);}

    }
}

function notifiedDistImp(){
    var checkboxs = document.getElementsByName("chkDistImp")
    for (var i = 0, l = checkboxs.length; i < l; i++) {
        if (checkboxs[i].checked) //checks to see if other checkbox is checked
        {
            document.getElementById("repDistImp").setAttribute("required", true);
        }else{document.getElementById("repDistImp").removeAttribute("required", false);}

    }

}

////////////////////////////////////Grouping of Checkboxes///////////////////////////////////////
function AdvOrProb() {
    //Checks that EventOrProblem is checked
    var checkboxs = document.getElementsByName("EventOrProblem");
    var okay = false;
    for (var i = 0, l = checkboxs.length; i < l; i++) {
        if (checkboxs[i].checked) {
            okay = true;
            break;
        }
    }

    if (okay) {
    } else {
        alert("Please check Adverse Event, Product Problem, or Both.");
        return false;
    } //checks if any box in the group is checked
}
function checkOutcome(){
    var checkboxs = document.getElementsByName("outcome")
    var okay =false
    for (var i = 0, l = checkboxs.length; i < l; i++) {

        if (checkboxs[i].checked) //checks to see if other checkbox is checked
        {
            okay = true
        }

    }
    if(okay == true){return true;}
    else{alert("please select at least one outcome"); return false;}

}

function checkOperator(){
    var checkboxs = document.getElementsByName("operator")
    var okay =false
    for (var i = 0, l = checkboxs.length; i < l; i++) {

        if (checkboxs[i].checked) //checks to see if other checkbox is checked
        {
            okay = true
        }

    }
    if(okay == true){return true;}
    else{alert("please select at least one operator"); return false;}

}
function validate() {
    AdvOrProb();
    checkOutcome();
    checkOperator();

}

function loadSig (val) {
    var isAdmin = val

    alert(isAdmin)
    if (isAdmin == 0) //checks to see if other checkbox is checked
    {
        document.getElementById("signature").setAttribute("hidden", true);
        document.getElementById("signatureDate").setAttribute("hidden", true);
    }
    else
    {
        document.getElementById("signature").removeAttribute("hidden", true);
        document.getElementById("signatureDate").removeAttribute("hidden", true);
    }
}
