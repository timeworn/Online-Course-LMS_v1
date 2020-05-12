var set_trail_link = function(){
    $('#input_video_link').modal('hide');
    var str_url = $('#video_link_url').val()
    $('#id_trailer_video_link').val(str_url)
    $('#trailer_video_preview').attr("src", str_url);
}
var onLoad = function(event){     
    //Check File API support  
    if(window.File && window.FileList && window.FileReader)
    {
        var filesInput = document.getElementById("image_field");
        filesInput.addEventListener("change", function(event){
            var files = event.target.files; //FileList object
            var image_loaded = document.getElementById("image_loaded");
            $('#image_loaded').addClass('display-none')
            $('#image_default').removeClass('display-none');
            for(var i = 0; i< files.length; i++)
            {
                var file = files[i];
                //Only pics
                if(!file.type.match('image'))
                  continue;
                
                var picReader = new FileReader();
                picReader.title = file.name;
                picReader.addEventListener("load",function(event){
                    var picFile = event.target;
                    image_loaded.src=picFile.result;
                    $('#image_loaded').removeClass('display-none')
                    $('#image_default').addClass('display-none');
                });                
                 //Read the image
                picReader.readAsDataURL(file);
            }          
        });
    }
    else
    {
        console.log("Your browser does not support File API");
        alert("Your browser does not support File API");
    }        
    $('.section-edit').click(function(event){            
        var target = event.target;
        console.log(target)
        var section_title = $(target).siblings('.section-title').text();
        var section_id = $(target).attr("section-id");
        var modal_id = '#add_section_modal'
        var form_id = '#add_section_modal form'
        $('#section_input').val(section_title);
        var url = "{% url 'teacher:edit_delete_section' 5 %}";
        var str = url.substr(url.lastIndexOf('/') + 1) + '$';
        url =  url.replace( new RegExp(str), section_id );
        $(form_id).attr("action", url);
        $(modal_id).modal({show:true});
    });

    $('.section-delete').click(function(event){            
        var target = event.target;
        var section_id = $(target).attr("section-id");
        var modal_id = '#delete_modal'
        var form_id = '#delete_modal form'
        var url = "{% url 'teacher:edit_delete_section' 5 %}";
        var str = url.substr(url.lastIndexOf('/') + 1) + '$';
        url =  url.replace( new RegExp(str), section_id );
        $(form_id).attr("action", url);
        $(modal_id).modal({show:true});
    });
}
window.addEventListener("load", onLoad);
