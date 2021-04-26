$(function(){
    function isValidURL(string) {
        var res = string.match(/(http(s)?:\/\/.)?(www\.)?[-a-zA-Z0-9@:%._\+~#=]{2,256}\.[a-z]{2,6}\b([-a-zA-Z0-9@:%_\+.~#?&//=]*)/g);
        return (res !== null)
    };
    
    $("#scrape_form").submit(function(e){
        
        url = $('input[name="url"]').val();
        chk_if_url = isValidURL(url);
        
        if(chk_if_url == true){
            $(".text-danger").text("");
            
                src_req = {
                    "url": url, 
                    "keywords":"sasas"
                }
            
                $.ajax({
                method: 'post',
                url: 'http://localhost:8000/scraper/',
                data: JSON.stringify(src_req),
                dataType: 'json',
                contentType: 'application/json',
                beforeSend: function(){
                   $('.text-warning').text("Loading.....");
                },
                success: function(data){
                   $('.text-warning').text("");
                    $("#output_src").text(data["data"]);
                    $("#output_container").show();
                },
                error: function(data){
                   $('.text-warning').text("!error happend");
                    console.log(data);
                }

            });
            
        }else{
            $(".text-danger").text("url is not valid");
        }
        
       // console.log(url, chk_if_url);
        
        return false;
    });
})
