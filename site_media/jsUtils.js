function mouseClick(nazwa) {
	var sh=document.getElementById(nazwa);
	if(sh) {
		if(sh.style.display=="block") {
			sh.style.display="none";
		} else {
			sh.style.display="block";
		}
	}
}

var isOpera = navigator.userAgent.indexOf("Opera") > -1;  
var isIE = navigator.userAgent.indexOf("MSIE") > 1 && !isOpera;  
var isMoz = navigator.userAgent.indexOf("Mozilla/5.") == 0 && !isOpera;  
  
 function textboxSelect (oTextbox, iStart, iEnd) {  
  
    switch(arguments.length) {  
        case 1:  
            oTextbox.select();  
            break;  
  
        case 2:  
            iEnd = oTextbox.value.length;  
            /* falls through */  
              
        case 3:            
            if (isIE) {  
                var oRange = oTextbox.createTextRange();  
                oRange.moveStart("character", iStart);  
                oRange.moveEnd("character", -oTextbox.value.length + iEnd);        
                oRange.select();                                                
            } else if (isMoz){  
                oTextbox.setSelectionRange(iStart, iEnd);  
            }                      
    }  
  
    oTextbox.focus();  
 }  
  
 function textboxReplaceSelect(oTextbox, sText) {  
  
    if (isIE) {  
        var oRange = document.selection.createRange();  
        oRange.text = sText;  
        oRange.collapse(true);  
        oRange.select();                                  
    } else if (isMoz) {  
        var iStart = oTextbox.selectionStart;  
        oTextbox.value = oTextbox.value.substring(0, iStart) + sText + oTextbox.value.substring(oTextbox.selectionEnd, oTextbox.value.length);  
        oTextbox.setSelectionRange(iStart + sText.length, iStart + sText.length);  
    }  
  
    oTextbox.focus();  
 }  
  
 function autocompleteMatch (sText, arrValues){  
    for (var i=0; i < arrValues.length; i++) {  
        if (arrValues[i].indexOf(sText) == 0) {  
            return arrValues[i];  
        }  
    }  
    return null;  
  
 }  

 function autocomplete(oTextbox, oEvent, arrValues){  
    switch (oEvent.keyCode) {  
        case 38: //up arrow    
        case 40: //down arrow  
        case 37: //left arrow  
        case 39: //right arrow  
        case 33: //page up    
        case 34: //page down    
        case 36: //home    
        case 35: //end                    
        case 13: //enter    
        case 9: //tab    
        case 27: //esc    
        case 16: //shift    
        case 17: //ctrl    
        case 18: //alt    
        case 20: //caps lock  
        case 8: //backspace    
        case 46: //delete  
            return true;  
            break;  
        default:  
            textboxReplaceSelect(oTextbox, String.fromCharCode(isIE ? oEvent.keyCode : oEvent.charCode));  
            var iLen = oTextbox.value.length;  
            var sMatch = autocompleteMatch(oTextbox.value, arrValues);  
            if (sMatch != null) {  
                oTextbox.value = sMatch;  
                textboxSelect(oTextbox, iLen, oTextbox.value.length);  
            }    
            return false;  
    }  
 }


