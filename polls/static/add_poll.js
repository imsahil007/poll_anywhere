
var counter = 2;
var limit = 10;
var values = new array(10);s
var imagevalues = new array(10);

function addInput(){
     if (counter == limit)  {
          alert("You have reached the limit of adding " + counter + " inputs");
     }
     else {
          counter++;

          document.getElementById("choice_form").innerHTML +='<div class=\"card mb-3\" id=\"option'+counter+'\"><div class=\"card-header\">Option '+counter+'</div><div class=\"card-body\"><div id=\"div_id_'+counter+'-choice_text\" class=\"form-group mt-3\"> <label for=\"id_'+counter+'-choice_text\" class=\" requiredField\">\n'+
                'Choice text<span class=\"asteriskField\">*</span> </label> <div class=\"\"> <input type=\"text\" name=\"'+counter+'-choice_text\" maxlength=\"100\" class=\"textinput textInput form-control\" required id=\"id_'+counter+'-choice_text\"> </div> </div> <div id=\"div_id_'+counter+'-choice_image\" class=\"form-group\"> <label for=\"id_'+counter+'-choice_image\" class=\"\">\n'+
                'Choice image\n'+
            '</label> <div class=\"\"> <input type=\"file\" name=\"'+counter+'-choice_image\" accept=\"image/*\" class=\"clearablefileinput form-control-file\" id=\"id_'+counter+'-choice_image\"> </div> </div>\n</div>\n</div>\n'
          document.getElementById("counter").value = counter.toString();
     }
}
function removeInput(){
     if (counter == 2)  {
          alert("You have reached the minimum limit. You cannot remove any elements now");
     }
     else {
               document.getElementById("option"+counter).remove();
               counter--;
               document.getElementById("counter").value = counter.toString();
     }
}