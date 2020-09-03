{
    $(document).ready(function(){
        $("a[href='/shop']").remove();
        $("a[href='/mycart']").remove();
        $("a[href='/my/home']").remove();
        $("a[href='/page/contactus']").remove();
        $('.remove_feedback').click(function (){
            var r = confirm("Are u sure ???");
            if (r == true) {
                $.get( "/remove_feedback", { feedback_id: $(this).attr('id')}).done(function(data){if (data){window.location.reload();}});
            }
        });
        $('#dob').datepicker();

        if ($('#uid').val() == 4){
            $("a[href='/scan']").hide();
        }
        else{
            $("a[href='/scan']").show();
        }

        $('.field-db').remove();
    }




);
}
