var year = 218;
const url = "https://hypixel-skyblock.fandom.com/api.php?action=query&format=json&prop=revisions&titles=Jacob%27s_Farming_Contest/Events/Year%20" + year + "&formatversion=2&rvprop=content&rvslots=*"

$(document).ready(function() {
    $.ajax({
        url: url,
        type: "GET",
        success: function(result) {
            console.log(result);
        },
        error: function(error) {
            console.log(error);
        }
    })
})