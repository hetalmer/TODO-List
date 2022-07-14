$(document).ready(function() {
    $("#today").show();
    $("#completed").hide();
    $("#upcoming").hide();
    $("#all").hide();
});
$(document).ready(function() {
    $("#ali").click(function() {
        $("#today").show();
        $("#completed").hide();
        $("#upcoming").hide();
        $("#all").hide();
    });
    $("#bli").click(function() {
        $("#today").hide();
        $("#completed").show();
        $("#upcoming").hide();
        $("#all").hide();
    });
    $("#cli").click(function() {
        $("#today").hide();
        $("#completed").hide();
        $("#upcoming").show();
        $("#all").hide();
    });
    $("#dli").click(function() {
        $("#today").hide();
        $("#completed").hide();
        $("#upcoming").hide();
        $("#all").show();
    });
});