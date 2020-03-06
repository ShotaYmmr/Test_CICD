$(function(){
    $("#set_finished_date").datepicker();
    var finishDate = $("#set_finished_date").val();
    $("#set_finished_date").datepicker("option", "dateFormat", "yy-mm-dd");
    $("#set_finished_date").datepicker("setDate", finishDate);
});