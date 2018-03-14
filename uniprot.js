(document).ready(function(){
$("button").click(function() {
        // Retreives an element (object):
        var sequence = $("#seq");
        var string = sequence.val();
        var out = "";
        var lines = [];
        lines = string.split("\n");
        $.ajax({
            url: "uniprot.cgi",
            type: "POST",
            data: {input_seq: string},
            success: function(response){
                    $("#output_seq").html(response);
                }
       });

        });
});
